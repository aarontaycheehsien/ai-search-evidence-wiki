# How this wiki is maintained

Place a paper in `incoming/papers/` and ask Codex Desktop to process it according to the repository's `AGENTS.md`. The assistant reads the source and existing claims, proposes classifications, and updates structured records only where justified.

After a change, validate records, regenerate pages, run tests, inspect affected pages and the Git diff, then commit manually after review. There are no automatic commits or hosted model calls.
