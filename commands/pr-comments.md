---
name: pr-comments
description: Use when user asks to review, analyze, or fetch PR comments. Triggers include "PR comments", "review comments", "unresolved comments", "what do reviewers think", or referencing feedback on a pull request.
---

# PR Comments Review

Fetch and analyze PR comments with context, providing verdicts and recommendations.

## Parameters

| Parameter    | Description                                          |
| ------------ | ---------------------------------------------------- |
| `unresolved` | (Default) Only fetch unresolved/open comment threads |
| `all`        | Fetch all comment threads (resolved and unresolved)  |

**Usage:** `/pr-comments` or `/pr-comments unresolved` or `/pr-comments all`

## Workflow

1. **Find the PR**

   ```bash
   # By branch name
   gh pr list --head <branch> --json number,title,url --jq '.[0]'

   # Current branch
   gh pr view --json number,title,url
   ```

2. **Understand the PR context BEFORE analyzing comments**

   Review the branch's intentions and completed work to avoid misjudging comments:

   ```bash
   # Get commit history to understand what was done and WHY
   git log main..HEAD --oneline

   # Read key commit messages for design decisions
   git show <commit> --stat

   # Get PR description for stated goals
   gh pr view <number> --json body
   ```

   **Why this matters:** Automated reviewers (Copilot, bots) lack context about intentional design decisions. A comment saying "you removed X" may be flagging an intentional removal, not an oversight. Understanding the work completed helps distinguish valid feedback from false positives.

3. **Get review threads** (based on parameter)

   ```bash
   gh api graphql -f query='
     query($owner: String!, $repo: String!, $pr: Int!) {
       repository(owner: $owner, name: $repo) {
         pullRequest(number: $pr) {
           reviewThreads(first: 100) {
             nodes {
               isResolved
               path
               line
               comments(first: 1) {
                 nodes { body author { login } }
               }
             }
           }
         }
       }
     }
   ' -f owner="{owner}" -f repo="{repo}" -F pr={number} \
     --jq '<FILTER>'
   ```

   **Filter by parameter:**
   - `unresolved` (default): `--jq '.data.repository.pullRequest.reviewThreads.nodes[] | select(.isResolved == false)'`
   - `all`: `--jq '.data.repository.pullRequest.reviewThreads.nodes[]'`

   When using `all`, include the resolution status in your analysis (e.g., "✓ Resolved" or "○ Unresolved").

4. **Read referenced files** for context (parallel reads)

5. **Analyze each comment** with this format:

   ```
   ## Comment N: [Brief Title]
   **File:** `path/to/file.ts:line`
   **Author:** username

   **The Comment:** [Summary of what they're saying]

   **Assessment:** [Correct/Incorrect/Depends] + reasoning

   | Pros of Current Code | Cons of Current Code |
   |---------------------|---------------------|
   | ... | ... |

   | Pros of Suggestion | Cons of Suggestion |
   |--------------------|-------------------|
   | ... | ... |

   **Recommendation:** [Accept/Dismiss/Clarify] + action
   ```

6. **Provide summary table**
   ```
   | Comment | Verdict | Action |
   |---------|---------|--------|
   | 1. ... | Accept | Quick fix |
   | 2. ... | Dismiss | Code is correct |
   | 3. ... | Clarify | Ask PM |
   ```

## Notes

- **Context first:** Always review commit history and PR description before judging comments. Commit messages often document intentional design decisions that reviewers (especially bots) miss.
- Always verify comment accuracy against actual code (Copilot/bots can be outdated)
- "Depends" verdicts need stakeholder input - identify WHO to ask
- Offer to implement accepted changes immediately
