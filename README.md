# awesome-federal-tech

Curated **code repositories** for people who deliver federal technology.

Not policy portals. Not marketplaces. Not slideware. Repos you can clone, inspect, and run through your own security process.

Focus areas: RMF / FedRAMP / ATO automation, DevSecOps, supply chain, containers, accessibility, telecommunications and real-time communications, continuous monitoring, and experimental cyber infrastructure.

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
- [Telecommunications & real-time communications](#telecommunications--real-time-communications)
- [AI tooling](#ai-tooling)
- [Experimental Infrastructure and Scientific Assurance](#experimental-infrastructure-and-scientific-assurance)
- [Federal digital service code](#federal-digital-service-code)
- [Contributing](#contributing)
- [Security & disclaimer](#security--disclaimer)
- [License](#license)

---

## RMF, OSCAL & ATO automation

- **[OSCAL](https://github.com/usnistgov/OSCAL)** – Machine-readable controls, SSPs, assessment plans/results. The path off Word/Excel packages.
- **[OSCAL Content](https://github.com/usnistgov/oscal-content)** – NIST catalogs and profiles in OSCAL.
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

## Telecommunications & real-time communications

- **[NIST JAIN-SIP (JSIP)](https://github.com/usnistgov/jsip)** – Official JAIN-SIP 1.2 Java reference implementation from NIST. Useful for SIP protocol interoperability, controlled telecom integration, and reference work around accessible real-time calling systems. Treat it as a mature maintenance/reference codebase: assess current Java dependencies, TLS/cipher support, parser hardening, and production fit before deployment.

## AI tooling

- **[Atlas UI 3](https://github.com/sandialabs/atlas-ui-3)** – Governed AI agents (MCP, access control, audit) for high-trust environments.
- **[TalkPipe](https://github.com/sandialabs/talkpipe)** – Streaming AI pipelines and composable RAG.
- **[TalkPipe Vault](https://github.com/sandialabs/talkpipe-vault)** – Local-first document search and grounded Q&A built on TalkPipe, with local embeddings and selectable local/cloud chat providers.
- **[AI Verify](https://github.com/IMDA-BTG/aiverify)** – Testing toolkit for AI governance and model behavior.

## Experimental Infrastructure and Scientific Assurance

High-fidelity cyber experimentation, cyber ranges, synthetic users, cyber-physical systems, scientific workflow provenance, uncertainty quantification, and authorization evidence pipelines. These tools form **capability stacks**, not isolated links.

See also:

- [Reference architectures](docs/reference-architectures/experimental-infrastructure.md)
- [Accessible Information Emulytics](docs/reference-architectures/accessible-information-emulytics.md)
- [Sandia Emulytics ecosystem](docs/ecosystems/sandia-emulytics.md)
- [CMU SEI Crucible ecosystem](docs/ecosystems/cmu-sei-crucible.md)
- [MITRE SAF ecosystem](docs/ecosystems/mitre-saf.md)

### Environment & orchestration

- **[minimega](https://github.com/sandia-minimega/minimega)** – Lightweight VMs, containers, SDN; scales from laptop to large clusters.
- **[FIREWHEEL](https://github.com/sandialabs/firewheel)** – Modular experiment orchestration and model-component framework (Emulytics).
- **[phenix](https://github.com/sandialabs/sceptre-phenix)** – Topology and orchestration UI/workflow engine for minimega, including SCEPTRE ICS workflows.
- **[TopoMojo](https://github.com/cmu-sei/TopoMojo)** – Virtual lab builder/player for training topologies (Crucible).
- **[wiretap](https://github.com/sandialabs/wiretap)** – Privilege-light WireGuard tunneling for segmented experiment networks.

### Synthetic users & adversary behavior

- **[GHOSTS](https://github.com/cmu-sei/GHOSTS)** – Realistic NPC / synthetic-user framework spanning cyber, social, and cognitive domains.
- **[Apache CALDERA](https://github.com/apache/caldera)** – ATT&CK-based adversary emulation, now incubating at Apache after originating at MITRE.
- **[CALDERA for OT](https://github.com/mitre/caldera-ot)** – OT/ICS protocol plugins for CALDERA.

### Cyber-physical & domain models

- **[SCEPTRE documentation](https://github.com/sandialabs/sceptre-docs)** + phenix apps – High-fidelity ICS and critical-infrastructure Emulytics.
- **[ExaGO](https://github.com/ORNL/ExaGO)** – Exascale power-grid optimization (consequence modeling).
- **[Conduit](https://github.com/LLNL/conduit)** – Hierarchical scientific data exchange for multi-physics coupling.

### Scientific assurance, provenance & UQ

- **[Flowcept](https://github.com/ORNL/flowcept)** – Runtime provenance for scientific and AI workflows.
- **[Dakota](https://github.com/snl-dakota/dakota)** – Optimization, uncertainty quantification, sensitivity analysis.
- **[Pyomo](https://github.com/Pyomo/pyomo)** – Python optimization modeling language (Sandia roots).

### Governed AI & assessment evidence

- **[Atlas UI 3](https://github.com/sandialabs/atlas-ui-3)** – Governed multi-LLM agents with MCP, access control, and audit.
- **[TalkPipe](https://github.com/sandialabs/talkpipe)** – Streaming AI / RAG pipeline composition.
- **[TalkPipe Vault](https://github.com/sandialabs/talkpipe-vault)** – Local-first retrieval and grounded document Q&A; useful as an inspectable reference for provider choice, local embeddings, and controlled knowledge access.
- **[Heimdall2](https://github.com/mitre/heimdall2)** / **[SAF CLI](https://github.com/mitre/saf)** – Assessment result storage, visualization, and pipeline tooling.
- **[eMASSer](https://github.com/mitre/emasser)** – CLI automation against the eMASS RMF API.
- **[Vulcan](https://github.com/mitre/vulcan)** – STIG authoring and InSpec profile development.

### Reference capability stacks (summary)

1. **Cyber Experimentation** – A proposed stack combining CALDERA, GHOSTS, minimega/TopoMojo, FIREWHEEL/phenix, Flowcept, Dakota, and SAF/Heimdall through project-specific adapters.
2. **Cyber-Physical Resilience** – A proposed composition of SCEPTRE/phenix, ExaGO, Conduit, Dakota/Pyomo, and Flowcept.
3. **High-Assurance AI Operations** – A proposed composition of Atlas UI 3, TalkPipe/TalkPipe Vault, Flowcept, and SAF/Heimdall/eMASSer/OSCAL.

Expect operational overhead, privileged components, and isolation requirements. Read licenses, security notes, and deployment assumptions before committing a range or analysis design to any of these platforms.

## Federal digital service code

- **[18F GitHub](https://github.com/18F)** – Public digital service patterns and historical implementations. Check activity; some repos are archival.

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) and [inclusion criteria](docs/inclusion-criteria.md).

**Scope rule:** public code and official technical repositories containing deployable software, schemas, models, reference implementations, or essential project documentation. Policy portals, marketplaces, and standalone guidance are out of scope.

Submit via the Resource Submission issue template. Canonical data: `data/resources.yml` (validated in CI).

## Security & disclaimer

**Inclusion is not endorsement by the U.S. Government or any agency.**

You must evaluate third-party code for security, supply chain, license, and fitness; follow your agency authorization process; prefer SBOMs, signed releases, and clear security contacts; track NVD, CISA KEV, and project advisories.

See [SECURITY.md](SECURITY.md).

## License

Repository content: [CC BY 4.0](LICENSE). Listed projects keep their own licenses.
