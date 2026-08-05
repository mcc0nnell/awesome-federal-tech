# Security Policy

## Supported Versions

This repository is a curated collection of links and metadata. There is no
"software version" in the traditional sense. Security issues related to the
repository itself (malicious pull requests, compromised CI, link injection,
etc.) will be addressed promptly.

## Reporting a Vulnerability

Do **not** open a public GitHub issue for security concerns related to this
repository or to tools listed herein that contain sensitive details.

Instead:

1. Email the maintainers (see GOVERNANCE.md or the repository "About" section
   for contact information once published).
2. Provide a clear description of the issue, steps to reproduce (if applicable),
   and any relevant impact assessment.
3. Allow reasonable time for response before any public disclosure.

## Third-Party Tools

**Inclusion of any third-party tool or project is not an endorsement and does
not imply that the tool is free of vulnerabilities.**

Users of this repository **must**:

- Independently evaluate every tool for security, license compliance, supply-
  chain risk, and fitness for purpose in a federal environment.
- Prefer projects that publish SBOMs, signed releases, and OpenSSF Scorecard
  results.
- Follow agency-specific processes for authorizing open-source software.
- Monitor for known vulnerabilities (NVD, CISA KEV, project advisories).

Executable tools listed in this repository should include security notes in
`data/resources.yml`. Review those notes carefully.

## Supply-Chain Considerations

This repository itself uses GitHub Actions with pinned versions where practical.
Contributions that introduce new Actions or scripts are subject to review for
supply-chain risk. The validation script (`scripts/validate-resources.py`) is intentionally
simple and dependency-light.
