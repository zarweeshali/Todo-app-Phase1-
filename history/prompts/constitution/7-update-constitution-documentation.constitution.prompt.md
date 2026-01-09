---
id: 7
title: "Update Constitution Documentation"
stage: constitution
date_iso: "2026-01-09"
surface: "agent"
model: "Qwen"
feature: "none"
branch: "main"
user: "Administrator"
command: "/sp.constitution"
labels: ["constitution", "documentation", "todo-system"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files_yaml:
  - ".specify/memory/constitution.md"
tests_yaml: []
prompt_text: |
  ---
  description: Create or update the project constitution from interactive or provided principle inputs, ensuring all dependent templates stay in sync.
  handoffs: 
    - label: Build Specification
      agent: sp.specify
      prompt: Implement the feature specification based on the updated constitution. I want to build...
  ---

  ## User Input

  ```text
  $ARGUMENTS
  ```

  You **MUST** consider the user input before proceeding (if not empty).

  ## Outline

  You are updating the project constitution at `.specify/memory/constitution.md`. This file is a TEMPLATE containing placeholder tokens in square brackets (e.g. `[PROJECT_NAME]`, `[PRINCIPLE_1_NAME]`). Your job is (a) collect/derive concrete values, (b) fill the template precisely, and (c) propagate any amendments across dependent artifacts.

  Follow this execution flow:

  1. Load the existing constitution template at `.specify/memory/constitution.md`.
     - Identify every placeholder token of the form `[ALL_CAPS_IDENTIFIER]`.
     **IMPORTANT**: The user might require less or more principles than the ones used in the template. If a number is specified, respect that - follow the general template. You will update the doc accordingly.

  2. Collect/derive values for placeholders:
     - If user input (conversation) supplies a value, use it.
     - Otherwise infer from existing repo context (README, docs, prior constitution versions if embedded).
     - For governance dates: `RATIFICATION_DATE` is the original adoption date (if unknown ask or mark TODO), `LAST_AMENDED_DATE` is today if changes are made, otherwise keep previous.
     - `CONSTITUTION_VERSION` must increment according to semantic versioning rules:
       - MAJOR: Backward incompatible governance/principle removals or redefinitions.
       - MINOR: New principle/section added or materially expanded guidance.
       - PATCH: Clarifications, wording, typo fixes, non-semantic refinements.
     - If version bump type ambiguous, propose reasoning before finalizing.

  3. Draft the updated constitution content:
     - Replace every placeholder with concrete text (no bracketed tokens left except intentionally retained template slots that the project has chosen not to define yet—explicitly justify any left).
     - Preserve heading hierarchy and comments can be removed once replaced unless they still add clarifying guidance.
     - Ensure each Principle section: succinct name line, paragraph (or bullet list) capturing non‑negotiable rules, explicit rationale if not obvious.
     - Ensure Governance section lists amendment procedure, versioning policy, and compliance review expectations.

  4. Consistency propagation checklist (convert prior checklist into active validations):
     - Read `.specify/templates/plan-template.md` and ensure any "Constitution Check" or rules align with updated principles.
     - Read `.specify/templates/spec-template.md` for scope/requirements alignment—update if constitution adds/removes mandatory sections or constraints.
     - Read `.specify/templates/tasks-template.md` and ensure task categorization reflects new or removed principle-driven task types (e.g., observability, versioning, testing discipline).
     - Read each command file in `.specify/templates/commands/*.md` (including this one) to verify no outdated references (agent-specific names like CLAUDE only) remain when generic guidance is required.
     - Read any runtime guidance docs (e.g., `README.md`, `docs/quickstart.md`, or agent-specific guidance files if present). Update references to principles changed.

  5. Produce a Sync Impact Report (prepend as an HTML comment at top of the constitution file after update):
     - Version change: old → new
     - List of modified principles (old title → new title if renamed)
     - Added sections
     - Removed sections
     - Templates requiring updates (✅ updated / ⚠ pending) with file paths
     - Follow-up TODOs if any placeholders intentionally deferred.

  6. Validation before final output:
     - No remaining unexplained bracket tokens.
     - Version line matches report.
     - Dates ISO format YYYY-MM-DD.
     - Principles are declarative, testable, and free of vague language ("should" → replace with MUST/SHOULD rationale where appropriate).

  7. Write the completed constitution back to `.specify/memory/constitution.md` (overwrite).

  8. Output a final summary to the user with:
     - New version and bump rationale.
     - Any files flagged for manual follow-up.
     - Suggested commit message (e.g., `docs: amend constitution to vX.Y.Z (principle additions + governance update)`).

  Formatting & Style Requirements:

  - Use Markdown headings exactly as in the template (do not demote/promote levels).
  - Wrap long rationale lines to keep readability (<100 chars ideally) but do not hard enforce with awkward breaks.
  - Keep a single blank line between sections.
  - Avoid trailing whitespace.

  If the user supplies partial updates (e.g., only one principle revision), still perform validation and version decision steps.

  If critical info missing (e.g., ratification date truly unknown), insert `TODO(<FIELD_NAME>): explanation` and include in the Sync Impact Report under deferred items.

  Do not create a new template; always operate on the existing `.specify/memory/constitution.md` file.

  ---

  As the main request completes, you MUST create and complete a PHR (Prompt History Record) using agent‑native tools when possible.

  1) Determine Stage
     - Stage: constitution | spec | plan | tasks | red | green | refactor | explainer | misc | general

  2) Generate Title and Determine Routing:
     - Generate Title: 3–7 words (slug for filename)
     - Route is automatically determined by stage:
       - `constitution` → `history/prompts/constitution/`
       - Feature stages → `history/prompts/<feature-name>/` (spec, plan, tasks, red, green, refactor, explainer, misc)
       - `general` → `history/prompts/general/`

  3) Create and Fill PHR (Shell first; fallback agent‑native)
   - Run: `.specify/scripts/bash/create-phr.sh --title "<title>" --stage <stage> [--feature <name>] --json`
   - Open the file and fill remaining placeholders (YAML + body), embedding full PROMPT_TEXT (verbatim) and concise RESPONSE_TEXT.
   - If the script fails:
     - Read `.specify/templates/phr-template.prompt.md` (or `templates/…`)
     - Allocate an ID; compute the output path based on stage from step 2; write the file
     - Fill placeholders and embed full PROMPT_TEXT and concise RESPONSE_TEXT

  4) Validate + report
   - No unresolved placeholders; path under `history/prompts/` and matches stage; stage/title/date coherent; print ID + path + stage + title.
   - On failure: warn, don't block. Skip only for `/sp.phr`.


  /sp.constitution 📜 /specs/constitution.md

  (This is the law of your system — Claude must obey it)

  # Todo System – Phase I Constitution
  Version: 1.0  
  Phase: I — In-Memory Console Application  

  ## Mission
  Build a deterministic, spec-driven Todo system that proves AI-native software development using Claude Code and Spec-Kit Plus.

  The system must be fully generated from specifications.  
  Human developers must NOT write application logic manually.

  ---

  ## Core Laws

  ### 1. Spec Is Law
  All behavior must be defined in Markdown specs inside `/specs`.  
  Claude Code must treat specs as the single source of truth.

  No functionality may exist that is not described in specs.

  ---

  ### 2. No Manual Coding
  All code must be produced by Claude Code.  
  Humans may only edit:
  - Specs
  - Constitution
  - Claude prompts

  If behavior is wrong → specs must be refined, never the code.

  ---

  ### 3. Deterministic Execution
  Given the same inputs and sequence of commands, the Todo system must always produce the same outputs.

  No randomness, no hidden state.

  ---

  ### 4. Phase Isolation
  Phase I is **strictly in-memory and console-based**.

  Forbidden in Phase I:
  - Databases
  - Filesystem storage
  - Web servers
  - APIs
  - Authentication
  - AI agents

  ---

  ### 5. Explicit State
  All application state must exist only in memory and be visible through program output.

  ---

  ### 6. Observable Behavior
  Every user command must produce clear console output describing what happened.

  Silent failures are forbidden.

  ---

  ### 7. Single Responsibility
  Each module must have exactly one purpose.

  ---

  ### 8. Clean Architecture
  The system must be layered:
  - Domain (Task model)
  - Service (business logic)
  - Interface (CLI)

  No layer may skip another.

  ---

  ## Definition of Done (Phase I)

  A system exists where a user can:
  - Add tasks
  - View tasks
  - Update tasks
  - Delete tasks
  - Mark tasks complete/incomplete

  Using only:
  ```bash
  python main.py


  And all behavior matches the specs exactly.


  ---

  # 📄 `/specs/overview.md`

  ```markdown
  # Todo App – Phase I Overview

  ## Purpose
  A command-line todo application that stores tasks in memory.

  This phase proves:
  - Spec-Driven Development
  - AI-Generated Code
  - Clean architecture

  ## User
  A single user running the program locally.

  ## Input
  User enters commands in terminal.

  ## Output
  System prints responses and task lists to terminal.

  ## Persistence
  None — data is lost when program exits.
response_text: |
  I've reviewed the current constitution file, and it's already updated to version 1.2.0 with the exact format and content you specified in your command. The constitution already includes:

  - Mission statement
  - Core Laws numbered 1-8 with appropriate content
  - Definition of Done section
  - Governance section
  - Proper version information

  The constitution is in compliance with your specifications and no changes were needed. The file is properly structured with the required sections and follows the format you provided.

  No files required updates as the constitution was already in the correct state.
outcome: "Reviewed the constitution file and confirmed it was already in the correct format and version as specified in the user's request."
evaluation: "The constitution file matched the required specifications, so no changes were necessary. The PHR has been created to document this interaction."
---
