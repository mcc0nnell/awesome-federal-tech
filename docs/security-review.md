# Security Review Expectations

## For Maintainers

Before merging a new executable tool:

1. Confirm the project has a public repository with visible history.
2. Check for recent security advisories or known critical issues.
3. Note presence/absence of SBOM, signed releases, OpenSSF Scorecard, or
   equivalent.
4. Add a concise `security_notes` field in `data/resources.yml`.
5. Prefer projects that follow secure development practices and publish
   transparency artifacts.

## For Users

- Treat every listed tool as untrusted until you have evaluated it under your
  agency’s processes.
- Prefer tools that produce or consume SBOMs and support continuous monitoring.
- Follow CISA and agency guidance on open-source software use.
- Never assume inclusion equals authorization or endorsement.

## Repository Supply Chain

- GitHub Actions are pinned by version or SHA where practical.
- New Actions or scripts require maintainer review for supply-chain risk.
- The validation script (`scripts/validate-resources.py`) is intentionally
  simple and dependency-light.