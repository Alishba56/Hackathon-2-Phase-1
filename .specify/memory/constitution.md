<!-- SYNC IMPACT REPORT:
Version change: N/A → 1.0.0
List of modified principles: N/A (new constitution)
Added sections: All sections (new constitution)
Removed sections: N/A
Templates requiring updates:
  - .specify/templates/plan-template.md: ✅ updated
  - .specify/templates/spec-template.md: ✅ updated
  - .specify/templates/tasks-template.md: ✅ updated
  - .specify/templates/commands/*.md: ✅ updated
  - README.md: ⚠ pending
Follow-up TODOs: None
-->

# Evolution of Todo – Phase I Constitution

## Core Principles

### I. Spec-Driven Development (NON-NEGOTIABLE)
All development must follow the Spec-Driven approach: Specify → Plan → Tasks → Implement. No code shall be written without a corresponding task ID and traceability to a spec. Engineers act as system architects, not code writers, with Claude Code handling all implementation.

### II. Python Console Application
The application must be a command-line interface (CLI) application built in Python. All user interaction occurs through the console, with text-based input/output following standard protocols: stdin/args → stdout, errors → stderr.

### III. In-Memory Data Management
All data handling must be in-memory only. No external databases, file-based persistence, or external storage systems are allowed. State management uses Python native structures (list, dict, classes) exclusively.

### IV. Single-User Application
The application is designed for single-user operation. No multi-user features, authentication systems, or user management beyond the single local user are permitted in Phase I.

### V. Phase I Scope Adherence
Only the following five features are allowed in Phase I: (1) Task add (title + description), (2) Task list (with completion status), (3) Task update, (4) Task delete (by ID), (5) Task complete/incomplete marking. No additional features may be implemented.

### VI. Technology Stack Compliance
Use only Python 3.13+, UV for package management, and Claude Code + Spec-Kit Plus tools. No external frameworks, libraries beyond standard Python, or web frameworks are permitted.

## Additional Constraints

Strict constraints apply: No external databases, no file persistence, no web frameworks, no async/concurrency, no AI/chatbot functionality. Over-engineering is prohibited - all code must prioritize clarity and simplicity.

## Development Workflow

All code generation must be performed exclusively through Claude Code. Manual coding is prohibited. Each feature must be independently specifiable and traceable. Clear separation of concerns required: data models, business logic, and CLI interface must be distinct.

## Governance

This constitution supersedes all other practices. Amendments require explicit documentation and approval. All implementation must trace back to specs and tasks. Compliance with Spec-Driven Development workflow is mandatory.

**Version**: 1.0.0 | **Ratified**: 2026-01-01 | **Last Amended**: 2026-01-01
