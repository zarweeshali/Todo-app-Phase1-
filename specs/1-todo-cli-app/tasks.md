---

description: "Task list template for feature implementation"
---

# Tasks: Todo CLI App

**Input**: Design documents from `/specs/1-todo-cli-app/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- **Web app**: `backend/src/`, `frontend/src/`
- **Mobile**: `api/src/`, `ios/src/` or `android/src/`
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Create project structure per implementation plan
- [x] T002 Initialize Python project with requirements.txt
- [x] T003 [P] Configure linting and formatting tools (flake8, black)

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

Examples of foundational tasks (adjust based on your project):

- [x] T004 Create Task entity model in src/models/task.py
- [x] T005 [P] Implement TaskService in src/services/task_service.py
- [x] T006 [P] Setup CLI interface framework in src/cli/main.py
- [x] T007 Create in-memory storage mechanism (no filesystem/database in Phase I)
- [x] T008 Configure error handling and logging infrastructure
- [x] T009 Setup command parsing for CLI interface

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add and Manage Tasks (Priority: P1) 🎯 MVP

**Goal**: Enable users to add, view, update, and delete tasks using a command-line interface

**Independent Test**: Can be fully tested by adding tasks, viewing them, updating them, and deleting them to verify the system works end-to-end.

### Tests for User Story 1 (OPTIONAL - only if tests requested) ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [x] T010 [P] [US1] Unit test for Task entity in tests/unit/models/test_task.py
- [x] T011 [P] [US1] Integration test for add command in tests/integration/cli/test_add_command.py

### Implementation for User Story 1

- [x] T012 [P] [US1] Create Task model in src/models/task.py
- [x] T013 [US1] Implement TaskService with add_task method in src/services/task_service.py
- [x] T014 [US1] Implement add command handler in src/cli/main.py
- [x] T015 [US1] Implement list command handler in src/cli/main.py
- [x] T016 [US1] Implement update command handler in src/cli/main.py
- [x] T017 [US1] Implement delete command handler in src/cli/main.py
- [x] T018 [US1] Add validation for required title in src/models/task.py

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Complete and Incomplete Tasks (Priority: P2)

**Goal**: Allow users to mark tasks as complete or incomplete as their status changes throughout the day

**Independent Test**: Can be tested by marking tasks as complete/incomplete and verifying the status updates in the list view.

### Tests for User Story 2 (OPTIONAL - only if tests requested) ⚠️

- [x] T019 [P] [US2] Unit test for complete/incomplete functionality in tests/unit/services/test_task_service.py
- [x] T020 [P] [US2] Integration test for complete/incomplete commands in tests/integration/cli/test_complete_command.py

### Implementation for User Story 2

- [x] T021 [P] [US2] Add complete_task method to TaskService in src/services/task_service.py
- [x] T022 [P] [US2] Add incomplete_task method to TaskService in src/services/task_service.py
- [x] T023 [US2] Implement complete command handler in src/cli/main.py
- [x] T024 [US2] Implement incomplete command handler in src/cli/main.py
- [x] T025 [US2] Update list command to show completion status ([ ] vs [x]) in src/cli/main.py

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Remove Completed Tasks (Priority: P3)

**Goal**: Allow users to remove tasks they no longer need to keep the list clean and focused

**Independent Test**: Can be tested by deleting tasks and verifying they no longer appear in the list.

### Tests for User Story 3 (OPTIONAL - only if tests requested) ⚠️

- [x] T026 [P] [US3] Unit test for delete functionality in tests/unit/services/test_task_service.py
- [x] T027 [P] [US3] Integration test for delete command in tests/integration/cli/test_delete_command.py

### Implementation for User Story 3

- [x] T028 [P] [US3] Enhance delete_task method in src/services/task_service.py
- [x] T029 [US3] Add error handling for non-existent tasks in src/services/task_service.py
- [x] T030 [US3] Add error handling for invalid commands in src/cli/main.py

**Checkpoint**: All user stories should now be independently functional

---

## Phase N: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [x] T031 [P] Documentation updates in README.md
- [x] T032 Code cleanup and refactoring
- [x] T033 Performance optimization across all stories
- [x] T034 [P] Additional unit tests (if requested) in tests/unit/
- [x] T035 Security hardening
- [x] T036 Run quickstart.md validation

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable

### Within Each User Story

- Tests (if included) MUST be written and FAIL before implementation
- Models before services
- Services before endpoints
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- All tests for a user story marked [P] can run in parallel
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
# Launch all tests for User Story 1 together (if tests requested):
Task: "Unit test for Task entity in tests/unit/models/test_task.py"
Task: "Integration test for add command in tests/integration/cli/test_add_command.py"

# Launch all models for User Story 1 together:
Task: "Create Task model in src/models/task.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence