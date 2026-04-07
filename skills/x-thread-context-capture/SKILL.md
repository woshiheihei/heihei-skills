---
name: x-thread-context-capture
description: Build a single-file research context pack around one X/Twitter post by browsing `x.com` in Chrome and extracting the root post, author follow-ups, key replies, key participants, and important internal/external references. Save the result into `cwd/x-thread-contexts/` using a structured filename. Use when the user shares an `x.com` or `twitter.com` status URL and wants the complete thread, author replies, key comments, or a model-ready context package for later deep research, analysis, or agent workflows.
---

# X Thread Context Capture

Produce a high-density context package for one X post, not an opinion piece. Preserve original text, preserve source boundaries, and give the next model enough first-hand material to continue the research without reopening X.

The output contract is strict: deliver one Markdown file that stands on its own, saving it under `cwd/x-thread-contexts/` with the default filename structure `x-thread-context-<author_handle>-<root_status_id>.md`.

## Output Contract

- Deliver a single Markdown file under `cwd/x-thread-contexts/`, named `x-thread-context-<author_handle>-<root_status_id>.md` by default.
- Preserve raw text over summary whenever possible.
- Separate author content, comments, X-internal referenced content, and third-party links.
- Record visible metadata for important items: author, handle, timestamp, and visible interaction counts when available.
- Treat counts as unstable page snapshots, not durable facts.
- Add a short coverage note when the visible page suggests the thread may be incomplete or when no more author replies can be found.
- Use the root-post author handle without `@`, lowercase it, and use the root status id from the URL. If the handle is temporarily unavailable, use `unknown-author` and rename once confirmed.
- Create `x-thread-contexts/` under the current working directory if it does not already exist.

Read [references/final-template.md](references/final-template.md) right before drafting the deliverable.

## Workflow

1. Open the root status URL on `x.com` in Chrome DevTools MCP and read it from snapshots first.
2. Capture the root post text, author, canonical URL, timestamp, and visible interaction signals.
3. Prefer author context before broad comment harvesting.
4. Open the author's thread view at `https://x.com/<handle>/thread/<root_status_id>` when it exists.
5. Run an X site search for `from:<handle> conversation_id:<root_status_id>` in `Latest` to find author replies that do not appear cleanly in the default conversation view.
6. Open high-value author replies individually when needed so you can capture both the upstream comment and the author's reply with exact text.
7. Collect a selective set of high-value comments after author coverage is solid.
8. Capture X-internal quoted or linked posts directly inside the deliverable file; keep third-party links as URLs plus visible preview text unless the user explicitly asks for more.
9. Stop when the root post, author follow-ups, key comments, and key references form a clear research context pack and additional scrolling is mostly repetitive.
10. Save the deliverable into `cwd/x-thread-contexts/`.
11. After saving the deliverable, close the X tabs opened for this task so the browser does not accumulate research tabs over time.

## Required Rules

- Use Chrome browsing behavior as the primary source of truth. Stay within ordinary browsing, scrolling, clicking, waiting, and reading.
- Do not rely on X APIs, unofficial APIs, network interception, or DOM scraping as the main acquisition path.
- Prefer X snapshots and individual post pages over third-party mirrors for post reconstruction.
- If login walls, rate limits, deleted posts, or region blocks prevent access, state exactly what is blocked and what was still recovered.
- Do not merge different source types together. Keep root post, author replies, comments, quoted posts, and external references distinct.
- Do not let system explanation dominate the deliverable. The Markdown file is a context package, not a commentary essay.
- Close only tabs opened for the task. Do not close unrelated pages the user may already have open.
- Do not scatter result files across the cwd root. Use the dedicated output directory unless the user explicitly asks for a different location.

## Selection Rules

- Cover all author-originated material first: root post, self-thread entries, clarifications, and direct replies that materially change understanding.
- Prefer comments from high-signal participants: verified/high-profile accounts, comments with strong interaction signals, comments the author replied to, and comments that introduce a new frame, example, objection, or resource.
- Skip low-information replies such as applause, pure emotion, repetition, and obvious topic drift unless they matter because the author engaged with them.
- When in doubt about comment selection or stopping conditions, read [references/selection-rubric.md](references/selection-rubric.md).

## Writing Rules For The Deliverable

- Use short, stable section headings.
- Put the exact URL on every important item.
- Use absolute dates or the exact timestamp as shown on X when available.
- Quote the raw post text in fenced `text` blocks when that improves fidelity.
- Add a short "coverage boundary" section at the end if you had to infer completeness from what X exposed.
- Explicitly say when you searched for more author replies and did not find any further visible results.
- Save to `cwd/x-thread-contexts/x-thread-context-<author_handle>-<root_status_id>.md` unless the user explicitly requests a different location or filename.

## Useful Tactics

- On long posts, use the expanded post view and individual status pages to avoid truncated text.
- On author replies, the individual status page is often the easiest place to recover both the upstream comment and the response cleanly.
- The search pattern `from:<handle> conversation_id:<root_status_id>` is the fastest way to discover author replies scattered through the conversation.
- The `/thread/<root_status_id>` route is the fastest way to check whether the author published a continuous self-thread.

## References

- Read [references/final-template.md](references/final-template.md) before writing the deliverable.
- Read [references/selection-rubric.md](references/selection-rubric.md) when choosing comments, references, and stop conditions.
