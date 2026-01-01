---
id: 1
title: Create Todo Constitution
stage: constitution
date: 2026-01-01
surface: agent
model: claude-sonnet-4-5-20250929
feature: none
branch: main
user: user
command: /sp.constitution
labels: [constitution,spec-driven,todo]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - .specify/memory/constitution.md
tests:
 - none
---

## Prompt

```
/sp.constitution

Project Name

Evolution of Todo – Phase I (In-Memory CLI Application)

Objective

Is phase ka objective ek command-line based Todo application develop karna hai jo "Evolution of Todo" project ki foundation serve kare.

Project ka primary focus strict Spec-Driven Development par hoga, jahan engineer sirf intent, rules aur architecture define karega aur implementation exclusively Claude Code ke zariye hogi.

Development Philosophy

Development sirf Spec-Driven approach par hogi

Engineer ka role system architect ka hoga, code writer ka nahi

Har line of code ka reference kisi na kisi spec aur task se hoga

Over-engineering se parhez, clarity aur simplicity ko priority

Code readable aur review-friendly hona chahiye

Mandatory Workflow Rules

Koi bhi code Task ID ke baghair likha nahi ja sakta

Har feature ka process hoga:

Specify → Plan → Tasks → Implement

Saari code generation Claude Code ke zariye hogi

Specs single source of truth hongi

Code kabhi bhi specs ko override nahi karega

Har feature independently spec aur traceable hoga
System Architecture Guidelines

Application type: Python Console (CLI)

Data handling: In-memory only

Persistence: Allowed nahi (no files, no database)

State management: Python native structures (list, dict, classes)

User model: Single-user application

Structure: Clear separation of concerns

Data models

Business logic

CLI interface
Phase I – Feature Scope

Is phase mein sirf neeche diye gaye features allowed hain:

Task add karna (title + description)

Task list dekhna (completion status ke sath)

Task update karna

Task delete karna (ID ke zariye)

Task complete / incomplete mark karna

Phase I ke bahar koi feature implement nahi kiya ja sakta.
Strict Constraints

External databases allowed nahi

File-based persistence mana hai

Web frameworks ka use mana hai

Async ya concurrency allowed nahi

AI / chatbot functionality is phase ka hissa nahi

Defined scope ke ilawa koi feature add nahi hoga
Technology Stack Rules

Python version: 3.13+

Package management: UV

Tools: Claude Code + Spec-Kit Plus only

Code Quality Standards

Clear aur meaningful naming

Small, focused functions

Predictable CLI behavior

Consistent formatting

Koi unused ya dead code nahi

Required Project Structure

/src → Python source code

/specs-history → saari specs ka record

constitution → project rules ka official document

README.md → setup aur run instructions

CLAUDE.md → Claude Code usage instructions

Validation & Success Criteria

Project successful mana jayega jab:

CLI ke through tamam 5 features correctly kaam kar rahe hon

Har task ka unique ID ho

Task completion status clearly visible ho

Saara code specs aur tasks se trace ho sakta ho

Manual coding ka koi evidence na mile

Claude prompts se spec refinement clearly visible ho

Failure Conditions

Project fail mana jayega agar:

Koi bhi manually written code mile

Specs missing ya incomplete hon

Feature bina task ke implement kiya gaya ho

Phase I scope se bahar feature add kiya gaya ho

Direct coding Claude Code ke baghair ki gayi ho

Definition of Done

Phase I tab complete mana jayega jab:

Console-based Todo application fully functional ho

Saare defined features expected behavior follow karen

Spec-Driven Development workflow clearly demonstrated ho

Project architecture clean, simple aur traceable ho
```

## Response snapshot

Created the constitution file for the "Evolution of Todo – Phase I" project based on the provided specifications. The constitution establishes core principles including Spec-Driven Development, Python CLI application requirements, in-memory data management, single-user application design, Phase I scope adherence, and technology stack compliance. The constitution serves as the foundational governance document for the project.

## Outcome

- ✅ Impact: Created project constitution at .specify/memory/constitution.md with 6 core principles and governance rules
- 🧪 Tests: none
- 📁 Files: Updated .specify/memory/constitution.md
- 🔁 Next prompts: Proceed with specifying the todo application features
- 🧠 Reflection: Constitution clearly defines project constraints and development workflow

## Evaluation notes (flywheel)

- Failure modes observed: none
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Begin feature specification process