---
name: refactoring
description: Checklist of refactor candidates to look for after a TDD green step (duplication, long methods, shallow modules, feature envy, primitive obsession). Use during the refactor phase of red-green-refactor, when reviewing newly-green code, or when the user invokes /refactoring.
---

# Refactor Candidates

After TDD cycle, look for:

- **Duplication** → Extract function/class
- **Long methods** → Break into private helpers (keep tests on public interface)
- **Shallow modules** → Combine or deepen
- **Feature envy** → Move logic to where data lives
- **Primitive obsession** → Introduce value objects
- **Existing code** the new code reveals as problematic
