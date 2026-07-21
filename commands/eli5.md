---
name: eli5
description: Use when user asks to explain a concept simply, wants something broken down, says "explain like I'm 5", "ELI5", or asks for a simple explanation of technical topics.
---

# ELI5 - Explain Like I'm 5

Break down concepts into easily understandable pieces, starting simple and optionally building up.

## Core Pattern

**Start at the simplest level (5-year-old).** Use:

- Everyday analogies (toys, food, games)
- Short sentences
- No jargon

**For complex technical concepts, offer cascading depth:**

| Level                     | Audience           | Style                            |
| ------------------------- | ------------------ | -------------------------------- |
| 5-year-old                | Child              | Analogies, no jargon             |
| Non-technical contributor | PM, designer, exec | Real examples, business context  |
| Junior Dev                | New programmer     | Code concepts, practical context |
| Expert                    | Experienced dev    | Nuances, edge cases, tradeoffs   |

## When to Cascade

**Default behavior:** Always provide ALL four levels (5-year-old → Non-technical → Junior Dev → Expert) unless the user explicitly requests a specific level.

**If user specifies a level** (e.g., "explain like I'm a junior dev"): Only provide that level.

## Format

Keep explanations concise. Each level should be 2-4 sentences max.

## Example

**User:** "What is a database index?"

**5-year-old:** "Imagine a big book with no table of contents. To find something, you'd flip through every page. An index is like adding a table of contents - it tells you exactly where to look so you don't have to check everything."

**Non-technical contributor:** "An index speeds up database searches. Without one, the system checks every record to find what you need. With an index, it jumps straight to the right spot - turning a 10-second query into milliseconds. The tradeoff is they take up storage space and slow down writes slightly."

**Junior Dev:** "An index creates a sorted reference to your data, typically using a B-tree structure. When you query `WHERE email = 'x'`, an index on `email` lets the DB do a binary search instead of a full table scan."

**Expert:** "Indexes trade write performance and storage for read speed. B-tree indexes work well for range queries; hash indexes are faster for equality but can't do ranges. Partial indexes, covering indexes, and index-only scans are tools for optimization. Watch for index bloat in high-churn tables."
