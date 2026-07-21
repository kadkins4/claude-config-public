---
name: grill-me
description: Interview the user relentlessly about a plan or design until reaching shared understanding, resolving each branch of the decision tree. Use when user wants to stress-test a plan, get grilled on their design, or mentions "grill me".
---

# Grill Me

Interview me relentlessly about every aspect of this plan until we reach a shared understanding. Walk down each branch of the design tree, resolving dependencies between decisions one-by-one. For each question, provide your recommended answer.

If a question can be answered by exploring the codebase, explore the codebase instead.

## Prefer visuals over text

When a question involves UI, layout, structure, or anything that can be represented visually, show it instead of describing it. Prose descriptions of interfaces are slow to read and easy to misinterpret — a quick mockup resolves ambiguity instantly.

- **UI/layout questions**: render an ASCII mockup or an HTML snippet showing the actual structure.
- **Component options**: use `AskUserQuestion` with the `preview` field to show side-by-side previews of each option.
- **Data shapes / API responses**: show the JSON/object literal, not a paragraph describing the fields.
- **Flow / state transitions**: a small diagram (mermaid, ASCII boxes-and-arrows) beats a numbered list.
- **Code-shaped decisions**: show the code snippet for each option rather than describing the approaches.

Default to "show, don't tell." Only fall back to prose when the decision is genuinely non-visual (naming, semantics, trade-offs without structural difference).
