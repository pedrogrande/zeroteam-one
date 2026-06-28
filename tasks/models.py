"""
Task Contract ORM Models
========================

SQLAlchemy ORM models for the polymorphic contract store.

**Hybrid strategy**: scalar columns for indexed/queryable fields + JSONB
``document`` for the full embedded aggregate. ``actors`` and ``audit_events``
are normalised tables shared across all contract types.

Tables:
- ``contracts`` — polymorphic root aggregate (one row per version)
- ``actors`` — normalised actor records (shared across contract types)
- ``audit_events`` — append-only audit log with hash chain (shared)
- ``contract_versions`` — fast version-history index
"""

from sqlalchemy import (
    BigInteger,
    CheckConstraint,
    Column,
    DateTime,
    Float,
    ForeignKey,
    Index,
    Integer,
    String,
    Text,
    UniqueConstraint,
    func,
)
from sqlalchemy.dialects.postgresql import JSONB, UUID as PGUUID
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """Declarative base for all contract tables."""

    pass


# ---------------------------------------------------------------------------
# Actors — normalised, shared across all contract types
# ---------------------------------------------------------------------------


class ActorModel(Base):
    __tablename__ = "actors"

    actor_id = Column(PGUUID(as_uuid=True), primary_key=True, nullable=False)
    actor_type = Column(String(50), nullable=False)
    display_name = Column(String(255), nullable=False, index=True)
    trust_score = Column(Float, nullable=True)
    reputation_score = Column(Float, nullable=True)
    public_key = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updated_at = Column(DateTime(timezone=True), nullable=True, onupdate=func.now())


# ---------------------------------------------------------------------------
# Contracts — polymorphic root aggregate (one row per version)
# ---------------------------------------------------------------------------


class ContractModel(Base):
    __tablename__ = "contracts"

    # Surrogate PK for ordering
    row_id = Column(Integer, primary_key=True, autoincrement=True)

    # Logical identity (stable across versions)
    contract_id = Column(PGUUID(as_uuid=True), nullable=False, index=True)

    # Semver version string
    version = Column(String(32), nullable=False)

    # Polymorphic discriminator
    contract_kind = Column(String(32), nullable=False, index=True)

    # Scalar columns promoted from JSONB for fast filtering
    status = Column(String(32), nullable=False, index=True)
    contract_type = Column(String(32), nullable=False, index=True)
    created_at = Column(DateTime(timezone=True), nullable=False, index=True)
    due_date = Column(DateTime(timezone=True), nullable=True, index=True)

    # Actor references (FK to actors table)
    requester_actor_id = Column(PGUUID(as_uuid=True), ForeignKey("actors.actor_id"), nullable=True, index=True)
    performer_actor_id = Column(PGUUID(as_uuid=True), ForeignKey("actors.actor_id"), nullable=True, index=True)

    # Self-referencing for decomposition lineage
    parent_contract_id = Column(PGUUID(as_uuid=True), nullable=True, index=True)

    # The full embedded aggregate
    document = Column(JSONB, nullable=False)

    # SHA-256 of the JSONB document for integrity checking
    document_hash = Column(String(64), nullable=False)

    # Immutable versioning — one row per (contract_id, version)
    __table_args__ = (
        UniqueConstraint("contract_id", "version", name="uq_contracts_id_version"),
        CheckConstraint(
            "contract_kind IN ('task', 'workflow', 'goal')",
            name="ck_contracts_contract_kind",
        ),
        Index("ix_contracts_kind_status", "contract_kind", "status"),
        # GIN index on document for @> containment queries
        Index("ix_contracts_document_gin", "document", postgresql_using="gin"),
    )


# ---------------------------------------------------------------------------
# Audit events — append-only, shared across all contract types
# ---------------------------------------------------------------------------


class AuditEventModel(Base):
    __tablename__ = "audit_events"

    event_id = Column(PGUUID(as_uuid=True), primary_key=True, nullable=False)
    contract_id = Column(PGUUID(as_uuid=True), nullable=False, index=True)
    contract_kind = Column(String(32), nullable=False, index=True)
    event_type = Column(String(32), nullable=False, index=True)
    actor_id = Column(PGUUID(as_uuid=True), ForeignKey("actors.actor_id"), nullable=False)
    timestamp = Column(DateTime(timezone=True), nullable=False, index=True)
    reason = Column(Text, nullable=True)
    before_snapshot = Column(JSONB, nullable=True)
    after_snapshot = Column(JSONB, nullable=True)
    immutable_hash = Column(String(64), nullable=False)
    previous_hash = Column(String(64), nullable=True)

    __table_args__ = (Index("ix_audit_events_contract_timestamp", "contract_id", "timestamp"),)


# ---------------------------------------------------------------------------
# Contract versions — fast version-history index
# ---------------------------------------------------------------------------


class ContractVersionModel(Base):
    __tablename__ = "contract_versions"

    contract_id = Column(PGUUID(as_uuid=True), nullable=False, primary_key=True)
    version = Column(String(32), nullable=False, primary_key=True)
    contract_kind = Column(String(32), nullable=False)
    row_id = Column(BigInteger, ForeignKey("contracts.row_id"), nullable=False)
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())

    __table_args__ = (Index("ix_contract_versions_contract", "contract_id"),)
