"""
Prompts Module
==============

Dedicated directory for agent system prompts and instruction constants.
Extracting prompts from agent files enables prompt iteration without
touching agent wiring code.
"""

from prompts.thinking_partner_instructions import INSTRUCTIONS

__all__ = ["INSTRUCTIONS"]
