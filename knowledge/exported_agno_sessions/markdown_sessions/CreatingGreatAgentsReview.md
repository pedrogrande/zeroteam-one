<!-- @format -->

# Creating great agents: Key insights for your Agentic Development Framework

Yes, this GitHub article contains several valuable insights that directly apply to your Agentic Development Framework. Here are the key learnings and how they map to your work:

## Critical Design Principles

### Specificity Over Generality

The article's core finding—that "most agent files fail because they're too vague"—directly validates your capability-based approach. The successful pattern is **"You are a test engineer who writes tests for React components, follows these examples, and never modifies source code"** rather than vague descriptions. This maps perfectly to your Child Task Contracts that specify "Required capabilities: code-generation-python, aws-lambda, trust-score code-quality ≥70". [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/42141261/14d7f752-3ed7-4fe5-9da8-99d2d662b0a6/How-to-write-a-great-agents.md)

### Commands Before Explanations

The finding that successful agents **"put commands early"** with specific flags (`npm test`, `pytest -v`) rather than just tool names has direct implications for your Task Specifications. Your Child Task Contracts should include: [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_f8ffc8cb-ddc4-4340-8bce-21d7722606ba/24ddec05-e67f-42ba-83f2-e3437e870098/CoreConcepts-AgenticDevelopmentFramework.md)

- Executable verification commands upfront
- Specific tool invocations with parameters
- Expected output formats

For example, instead of "verification-capable agents run tests," specify: `pytest tests/api/test_auth.py --coverage-min=85 --output=json`. [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_f8ffc8cb-ddc4-4340-8bce-21d7722606ba/0ed3a6bc-adf7-4827-9e3d-563a38175bc5/AgenticFrameworkDetails.md)

### Code Examples Over Abstract Descriptions

The article emphasizes: **"One real code snippet showing your style beats three paragraphs describing it"**. This validates shifting from descriptive task requirements to example-driven specifications in your framework. Your Acceptance Criteria in Child Task Contracts should include: [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/42141261/14d7f752-3ed7-4fe5-9da8-99d2d662b0a6/How-to-write-a-great-agents.md)

```
✅ Good output example:
async function fetchUserData(id: string): Promise<User> {
  if (!id) throw new Error('ID required');
  return await api.get(`/users/${id}`);
}

❌ Bad output (what to avoid):
async function get(x) { return api.get('/users/'+x).data; }
```

## Three-Tier Boundary System

The article's **"always do / ask first / never do"** structure is directly applicable to your agent capability specifications. This provides a practical pattern for encoding trust boundaries: [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_f8ffc8cb-ddc4-4340-8bce-21d7722606ba/24ddec05-e67f-42ba-83f2-e3437e870098/CoreConcepts-AgenticDevelopmentFramework.md)

**For Code Generation Agents:**

- ✅ Always: Write to `src/`, run tests, follow naming conventions
- ⚠️ Ask first: Database schema changes, adding dependencies
- 🚫 Never: Commit secrets, modify vendor directories [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/42141261/14d7f752-3ed7-4fe5-9da8-99d2d662b0a6/How-to-write-a-great-agents.md)

**For Verification Agents:**

- ✅ Always: Run full test suite, check coverage thresholds
- ⚠️ Ask first: Override failed tests requiring human judgment
- 🚫 Never: Remove failing tests, skip security scans [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/42141261/14d7f752-3ed7-4fe5-9da8-99d2d662b0a6/How-to-write-a-great-agents.md)

This maps directly to your trust score domains and verification levels. [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_f8ffc8cb-ddc4-4340-8bce-21d7722606ba/24ddec05-e67f-42ba-83f2-e3437e870098/CoreConcepts-AgenticDevelopmentFramework.md)

## Six Core Areas Framework

The article identifies that top-tier agents **"cover six core areas: commands, testing, project structure, code style, git workflow, and boundaries"**. This provides a template for structuring your Agent Capability Profiles: [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_f8ffc8cb-ddc4-4340-8bce-21d7722606ba/24ddec05-e67f-42ba-83f2-e3437e870098/CoreConcepts-AgenticDevelopmentFramework.md)

### Your Framework Mapping

1. **Commands** → Tool specifications in Child Task Contracts
2. **Testing** → Verification requirements and acceptance criteria
3. **Project structure** → Dependency graph context and artifact locations
4. **Code style** → Pattern Library examples from Knowledge Graph [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_f8ffc8cb-ddc4-4340-8bce-21d7722606ba/24ddec05-e67f-42ba-83f2-e3437e870098/CoreConcepts-AgenticDevelopmentFramework.md)
5. **Git workflow** → State transitions in smart contracts (UNCLAIMED → CLAIMED → VERIFIED) [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_f8ffc8cb-ddc4-4340-8bce-21d7722606ba/0ed3a6bc-adf7-4827-9e3d-563a38175bc5/AgenticFrameworkDetails.md)
6. **Boundaries** → Trust thresholds and capability constraints [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_f8ffc8cb-ddc4-4340-8bce-21d7722606ba/24ddec05-e67f-42ba-83f2-e3437e870098/CoreConcepts-AgenticDevelopmentFramework.md)

## Agent Specialization Strategy

The article's examples (@docs-agent, @test-agent, @security-agent) align with your capability-based approach rather than role-based agents. The key insight: **"Pick one simple task. Don't build a 'general helper'"**. [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/42141261/14d7f752-3ed7-4fe5-9da8-99d2d662b0a6/How-to-write-a-great-agents.md)

### Application to Your Framework

Instead of defining broad "Builder Agent" or "Manager Agent" roles, your marketplace should encourage agents that claim narrow, well-defined task types:

- **Documentation Synthesis Agent**: Claims tasks requiring `synthesis + documentation + markdown`
- **Security Verification Agent**: Claims tasks requiring `verification + security-analysis + adversarial-testing`
- **API Development Agent**: Claims tasks requiring `code-generation + REST-APIs + openapi-spec` [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/42141261/14d7f752-3ed7-4fe5-9da8-99d2d662b0a6/How-to-write-a-great-agents.md)

This matches your vision of "capability composition" where agents dynamically team mid-task. [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_f8ffc8cb-ddc4-4340-8bce-21d7722606ba/24ddec05-e67f-42ba-83f2-e3437e870098/CoreConcepts-AgenticDevelopmentFramework.md)

## Iterative Specification Design

The article emphasizes: **"The best agent files grow through iteration, not upfront planning"**. This has profound implications for your Ideation Phase: [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_f8ffc8cb-ddc4-4340-8bce-21d7722606ba/57b1e1af-74e6-440f-a995-8df3fd792fd2/ConceptPaper-AgenticDevelopmentFramework.md)

### Recommendation

Instead of creating perfect Task Dependency Graphs upfront, implement a **specification evolution mechanism**:

1. **Initial TDG**: Minimal task specs with basic requirements
2. **Learning Loop**: As agents claim tasks, capture failure modes
3. **Spec Refinement**: Automatically update task requirements based on verification failures
4. **Pattern Extraction**: Successful task completions create reusable specification templates [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/42141261/14d7f752-3ed7-4fe5-9da8-99d2d662b0a6/How-to-write-a-great-agents.md)

This creates a feedback loop where your Knowledge Graph not only captures _solutions_ but also evolves _task specifications_ based on what actually works. [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_f8ffc8cb-ddc4-4340-8bce-21d7722606ba/24ddec05-e67f-42ba-83f2-e3437e870098/CoreConcepts-AgenticDevelopmentFramework.md)

## Project Knowledge as Context

The article's emphasis on providing **"tech stack with versions (React 18, TypeScript, Vite, Tailwind CSS) and exact file locations"** highlights a gap in your current framework. Your Child Task Contracts should include structured project context: [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/42141261/14d7f752-3ed7-4fe5-9da8-99d2d662b0a6/How-to-write-a-great-agents.md)

```yaml
project_context:
  tech_stack:
    - framework: FastAPI
      version: "0.104.1"
    - database: PostgreSQL
      version: "15.3"
  file_structure:
    src/: "Application code (READ/WRITE)"
    tests/: "Test suites (READ for context, WRITE for new tests)"
    docs/: "Documentation (WRITE only)"
```

This reduces context ambiguity and improves task-capability matching in your marketplace. [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/42141261/14d7f752-3ed7-4fe5-9da8-99d2d662b0a6/How-to-write-a-great-agents.md)

## Risk Management Through Boundaries

The finding that **"'Never commit secrets' was the most common helpful constraint"** validates your Risk Budget and Verification Levels approach. However, the article suggests implementing graduated boundaries: [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_f8ffc8cb-ddc4-4340-8bce-21d7722606ba/24ddec05-e67f-42ba-83f2-e3437e870098/CoreConcepts-AgenticDevelopmentFramework.md)

### Enhanced Trust Model

Instead of binary trust scores, implement multi-dimensional boundary constraints:

- **Low-risk tasks**: Auto-verify, no human review required
- **Medium-risk tasks**: Require peer agent verification
- **High-risk tasks**: Require human expert approval before VERIFIED state
- **Critical tasks**: Multi-signature verification + attack bounty validation [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_f8ffc8cb-ddc4-4340-8bce-21d7722606ba/0ed3a6bc-adf7-4827-9e3d-563a38175bc5/AgenticFrameworkDetails.md)

## Observable Failure Modes

The article's pattern of showing **"what good output looks like"** alongside bad examples suggests adding an **Anti-Pattern Library** to complement your Pattern Library: [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/42141261/14d7f752-3ed7-4fe5-9da8-99d2d662b0a6/How-to-write-a-great-agents.md)

When Learning Agents extract patterns, they should also document:

- ✅ **Pattern**: Keep-Warm Script for 500ms ML Inference
- ❌ **Anti-Pattern**: Synchronous model loading in Lambda handler [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_f8ffc8cb-ddc4-4340-8bce-21d7722606ba/24ddec05-e67f-42ba-83f2-e3437e870098/CoreConcepts-AgenticDevelopmentFramework.md)

This accelerates agent learning by teaching "what not to do" as explicitly as "what to do."

## Starter Template Advantage

The article provides a practical starter template that could be adapted as your **Child Task Contract Template**. Currently your framework describes task structure abstractly, but providing concrete templates would accelerate marketplace adoption: [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/42141261/14d7f752-3ed7-4fe5-9da8-99d2d662b0a6/How-to-write-a-great-agents.md)

```markdown
## Task: [TASK-ID]

**Bounty:** 800 tokens
**Required Capabilities:** infrastructure-as-code, aws, terraform
**Trust Threshold:** technical-execution ≥70%

## Your Role

You are a cloud infrastructure engineer specializing in...

## Commands

- Deploy: `terraform apply -var-file=dev.tfvars`
- Validate: `terraform validate && tflint`

## Acceptance Criteria

[Concrete examples with ✅ Good / ❌ Bad patterns]

## Boundaries

- ✅ Always: Run terraform plan before apply, tag all resources
- ⚠️ Ask first: Changes to production VPC, IAM role modifications
- 🚫 Never: Hardcode credentials, modify shared state files
```

This practical format makes your task marketplace immediately actionable. [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_f8ffc8cb-ddc4-4340-8bce-21d7722606ba/57b1e1af-74e6-440f-a995-8df3fd792fd2/ConceptPaper-AgenticDevelopmentFramework.md)

The article's empirical findings from 2,500+ agent specifications provide concrete validation for your capability-based, boundary-explicit, example-driven approach to agent design.
