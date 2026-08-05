# awesome-federal-tech

Curated **code repositories** for people who deliver federal technology.

Not policy portals. Not marketplaces. Not slideware. Repos you can clone, inspect, and run through your own security process.

Focus areas: RMF / FedRAMP / ATO automation, DevSecOps, supply chain, containers, accessibility, continuous monitoring, and experimental cyber infrastructure.

**Inclusion is not endorsement.** Evaluate license, supply chain, and fitness for your environment yourself.

---

## Table of Contents

- [RMF, OSCAL & ATO automation](#rmf-oscal--ato-automation)
- [Continuous monitoring & assessment](#continuous-monitoring--assessment)
- [Supply chain & SBOM](#supply-chain--sbom)
- [DevSecOps, policy-as-code & IaC](#devsecops-policy-as-code--iac)
- [Containers & platforms](#containers--platforms)
- [Observability](#observability)
- [Accessibility](#accessibility)
- [AI tooling](#ai-tooling)
- [Experimental infrastructure](#experimental-infrastructure)
- [Federal digital service code](#federal-digital-service-code)
- [Contributing](#contributing)
- [Security & disclaimer](#security--disclaimer)
- [License](#license)

---

## RMF, OSCAL & ATO automation

- **[OSCAL](https://github.com/usnistgov/OSCAL)** – Machine-readable controls, SSPs, assessment plans/results. The path off Word/Excel packages.
- **[OSCAL Content](https://github.com/usnistgov/oscal-content)** – NIST catalogs and profiles in OSCAL.
- **[FedRAMP Automation](https://github.com/GSA/fedramp-automation)** – Official OSCAL baselines and templates. Check maturity before you bet a process on it.
- **[Heimdall2](https://github.com/mitre/heimdall2)** – Store and visualize assessment results (HDF).
- **[SAF CLI](https://github.com/mitre/saf)** – Convert/filter/report assessment data in pipelines.
- **[Lula](https://github.com/defenseunicorns/lula)** – OSCAL validation aimed at cloud-native systems.
- **[GovReady-Q](https://github.com/GovReady/govready-q)** – Open GRC for security documentation workflows.
- **[ComplianceAsCode Content](https://github.com/ComplianceAsCode/content)** – SCAP/Ansible/Bash content mapped to baselines.
- **[OpenSCAP](https://github.com/OpenSCAP/openscap)** – SCAP evaluation engine.
- **[CSET](https://github.com/cisagov/cset)** – Structured assessments against multiple frameworks.

## Continuous monitoring & assessment

- **[InSpec ecosystem via SAF/Heimdall](https://github.com/mitre/saf)** – Infrastructure testing results into a federal-friendly reporting path.
- **[OpenSCAP](https://github.com/OpenSCAP/openscap)** / **[ComplianceAsCode](https://github.com/ComplianceAsCode/content)** – Configuration and baseline scanning.
- **[CSET](https://github.com/cisagov/cset)** – Facilitated/self assessment tooling from CISA.

## Supply chain & SBOM

- **[Trivy](https://github.com/aquasecurity/trivy)** – Vulns, misconfigs, secrets, IaC, images.
- **[Syft](https://github.com/anchore/syft)** – SBOM generation.
- **[Grype](https://github.com/anchore/grype)** – Scan images and SBOMs.
- **[Cosign](https://github.com/sigstore/cosign)** – Sign and verify artifacts.
- **[OpenSSF Scorecard](https://github.com/ossf/scorecard)** – Upstream project hygiene signals.
- **[Semgrep](https://github.com/semgrep/semgrep)** – Fast SAST / custom rules.
- **[OWASP Dependency-Check](https://github.com/dependency-check/DependencyCheck)** – SCA for known vulnerable dependencies.
- **[Gitleaks](https://github.com/gitleaks/gitleaks)** – Secrets in git history and pipelines.

## DevSecOps, policy-as-code & IaC

- **[OPA](https://github.com/open-policy-agent/opa)** – Portable policy engine.
- **[Kyverno](https://github.com/kyverno/kyverno)** – Kubernetes-native policy.
- **[Checkov](https://github.com/bridgecrewio/checkov)** – IaC and pipeline static analysis.
- **[Cloud Custodian](https://github.com/cloud-custodian/cloud-custodian)** – Cloud policy-as-code and remediation.
- **[Terraform](https://github.com/hashicorp/terraform)** – Still the default IaC in many agencies. Confirm current license terms for your org.
- **[OWASP ZAP](https://github.com/zaproxy/zaproxy)** – DAST for web apps.

## Containers & platforms

- **[Kubernetes](https://github.com/kubernetes/kubernetes)** – Default orchestration target. Hardening and admission control are not optional.
- **[Platform One Big Bang](https://github.com/DoD-Platform-One/bigbang)** – DoD reference packaging/GitOps for hardened stacks. Reference architecture, not a free ATO.
- **[Falco](https://github.com/falcosecurity/falco)** – Runtime detection for containers and hosts.

## Observability

- **[OpenTelemetry](https://github.com/open-telemetry/opentelemetry-specification)** – Vendor-neutral telemetry specs.
- **[Prometheus](https://github.com/prometheus/prometheus)** – Metrics and alerting.
- **[Grafana](https://github.com/grafana/grafana)** – Dashboards. Confirm edition/license fit.
- **[Wazuh](https://github.com/wazuh/wazuh)** – Open monitoring/XDR-style stack. Evaluate agent privilege and rules before wide deploy.

## Accessibility

- **[USWDS](https://github.com/uswds/uswds)** – Federal design system and accessible components.
- **[axe-core](https://github.com/dequelabs/axe-core)** – Automated accessibility testing. Necessary; not sufficient.

## AI tooling

- **[Atlas UI 3](https://github.com/sandialabs/atlas-ui-3)** – Governed AI agents (MCP, access control, audit) for high-trust environments.
- **[TalkPipe](https://github.com/sandialabs/talkpipe)** – Streaming AI pipelines and composable RAG.
- **[AI Verify](https://github.com/IMDA-BTG/aiverify)** – Testing toolkit for AI governance and model behavior.

## Experimental infrastructure

Cyber ranges, emulation, and scientific experiment tooling. Not general-purpose app hosting.

- **[minimega](https://github.com/sandia-minimega/minimega)** – VMs, containers, SDN. Laptop to cluster.
- **[FIREWHEEL](https://github.com/sandialabs/firewheel)** – Modular, repeatable experiment orchestration (Emulytics).
- **[phenix](https://github.com/sandialabs/sceptre-phenix)** – Topology/orchestration UI for minimega (including SCEPTRE workflows).
- **[wiretap](https://github.com/sandialabs/wiretap)** – Privilege-light WireGuard tunneling for segmented experiment networks.

Expect operational overhead. Read licenses and deployment assumptions before you commit a range design to them.

## Federal digital service code

- **[18F GitHub](https://github.com/18F)** – Public digital service patterns and historical implementations. Check activity; some repos are archival.

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) and [inclusion criteria](docs/inclusion-criteria.md).

**Scope rule:** code repositories only (GitHub and other public forges). No policy portals, marketplaces, or documentation-only sites.

Submit via the Resource Submission issue template. Canonical data: `data/resources.yml` (validated in CI).

## Security & disclaimer

**Inclusion is not endorsement by the U.S. Government or any agency.**

You must evaluate third-party code for security, supply chain, license, and fitness; follow your agency authorization process; prefer SBOMs, signed releases, and clear security contacts; track NVD, CISA KEV, and project advisories.

See [SECURITY.md](SECURITY.md).

## License

Repository content: [CC BY 4.0](LICENSE). Listed projects keep their own licenses.
