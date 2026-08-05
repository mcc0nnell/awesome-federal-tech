# Maintenance Policy

## Cadence

- **Weekly**: Automated link health and YAML validation via GitHub Actions.
- **Quarterly**: Full human review of every entry for continued relevance,
  accuracy of descriptions, and status updates.
- **As needed**: Rapid response to broken primary links, security disclosures
  affecting listed tools, or major official updates (new NIST revisions,
  FedRAMP changes, etc.).

## Status Values

Used in `data/resources.yml`:

- `active` – Regular meaningful updates
- `maintenance` – Occasional updates, still usable
- `archived` – Officially archived but retained for historical/reference value
- `unknown` – Activity cannot be reliably determined (should be rare)

## Removal

Resources may be removed when they:

- Become abandoned with no viable successor
- Are superseded by a clearly superior official source
- Introduce unacceptable risk that cannot be mitigated by documentation
- Fail repeated link checks and the maintainer cannot locate a replacement URL

Removal decisions are documented in issues or pull-request discussion.

## Community Input

Users are encouraged to open issues for broken links, outdated descriptions, or
new candidate resources. Maintainers retain final editorial control.