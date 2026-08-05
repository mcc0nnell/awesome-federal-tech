# Contributing to awesome-federal-tech

Thank you for helping improve this curated collection.

## Before You Start

1. Read the [inclusion criteria](docs/inclusion-criteria.md).
2. Search existing issues and the current `data/resources.yml` to avoid
   duplicates.
3. Prefer primary sources and actively maintained projects.

## How to Propose a Resource

Use the **Resource Submission** issue template. Provide:

- Name and canonical URL
- Organization / maintainer
- Short description (1–3 sentences)
- Categories (from the taxonomy)
- License (if applicable)
- Why it belongs (federal relevance)
- Any known limitations or security notes

After discussion, open a pull request that:

1. Adds the entry to `data/resources.yml` following the schema.
2. Updates the relevant section of `README.md` if needed.
3. Passes the validation workflow.

## Pull Request Expectations

- Keep changes focused.
- Run `python scripts/validate-resources.py` locally if possible.
- Do not add marketing language or unsupported claims.
- Include security notes for any executable tool.

## Code of Conduct

All participation is governed by the [Code of Conduct](CODE_OF_CONDUCT.md).

## Questions

Open a plain issue or start a Discussion. We prefer public conversation so the
community can benefit.
