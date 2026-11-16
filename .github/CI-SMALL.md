# CI-small execution

GitHub is the canonical source repository. GitHub-hosted Actions are disabled for this fork to avoid repeated metered-run startup failures.

The private GitLab control project `robert526/awesome-federal-tech-ci-control` receives GitHub `push` events for `main` via an external pipeline trigger. Its `ci-small` jobs run only on runner `56236216`; GitLab shared runners are disabled.

## Verified checks

- Compare the event's repository, ref, and 40-character commit SHA against the actual GitHub `main` head. Clone and verify the exact commit.
- Validate resource data using Python 3.12 and PyYAML.
- Lint Markdown using markdownlint-cli2 on Node 22.
- Check live links using Lychee, preserving the repository's configured exclusions.

Evidence and result: see the private GitLab pipeline jobs. Do not interpret a skipped or missing job as a passing check.

## Scope and limitations

This route handles **main-branch pushes**. Pull-request head validation and GitHub branch-protection status reporting are **not yet wired**. Do not merge a PR solely because CI-small passed on `main`.

Secrets and pipeline trigger tokens are deliberately not committed to this repository.

## Pull-request verification acceptance criteria

The PR-head gate must reject webhook data that does not match the repository's current GitHub pull-request record. Only same-repository PRs targeting `main` are accepted in this first iteration; fork PRs remain unsupported. Validation must check the GitHub PR number, exact head commit SHA, repository identity, and base branch before any tests run.

A successful `main` pipeline never substitutes for a successful PR-head pipeline. GitHub required-check reporting is a separate integration and remains unimplemented until independently verified.
