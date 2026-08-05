# awesome-federal-tech

Curated primary sources, official guidance, and maintained open-source projects for people who actually deliver federal technology.

Covers the hard joins: requirements → acquisition → architecture → authorization (RMF / FedRAMP / ATO) → accessibility (Section 508) → deployment → continuous monitoring.

**Not a link dump.** Inclusion is not endorsement. Evaluate every third-party tool yourself—security, license, fitness for your environment.

---

## Table of Contents

- [Start Here by Persona](#start-here-by-persona)
- [Foundations & Standards](#foundations--standards)
- [NIST RMF & SP 800-53](#nist-rmf--sp-800-53)
- [FedRAMP, OSCAL & ATO Automation](#fedramp-oscal--ato-automation)
- [Continuous Monitoring & Assessment](#continuous-monitoring--assessment)
- [Supply-Chain Security & SBOM](#supply-chain-security--sbom)
- [DevSecOps, Policy-as-Code & IaC](#devsecops-policy-as-code--iac)
- [Zero Trust & Identity](#zero-trust--identity)
- [Cloud Platforms](#cloud-platforms)
- [Experimental Infrastructure](#experimental-infrastructure)
- [Containers, Kubernetes & Platforms](#containers-kubernetes--platforms)
- [Observability & Incident Response](#observability--incident-response)
- [Accessibility & Section 508](#accessibility--section-508)
- [AI Governance & Security](#ai-governance--security)
- [Privacy, Records & Data Governance](#privacy-records--data-governance)
- [Acquisition, COR & Vendor Oversight](#acquisition-cor--vendor-oversight)
- [Open Source Policy](#open-source-policy)
- [Training, Communities & Case Studies](#training-communities--case-studies)
- [Contributing](#contributing)
- [Security & Disclaimer](#security--disclaimer)
- [License](#license)

---

## Start Here by Persona

**System Owner / ISSO / ISSM chasing or holding an ATO**  
[RMF & 800-53](#nist-rmf--sp-800-53) → [FedRAMP / OSCAL / ATO](#fedramp-oscal--ato-automation) → [Continuous Monitoring](#continuous-monitoring--assessment) → [Supply-Chain](#supply-chain-security--sbom). Heimdall, SAF, ComplianceAsCode, and official OSCAL content are the working set.

**Cloud architect or DevSecOps engineer**  
[Cloud](#cloud-platforms), [Containers](#containers-kubernetes--platforms), [DevSecOps](#devsecops-policy-as-code--iac), [Supply-Chain](#supply-chain-security--sbom). Platform One / Big Bang, Trivy, Syft/Grype, Cosign, OPA, Checkov, Cloud Custodian.

**Accessibility specialist or digital service team**  
[Accessibility & Section 508](#accessibility--section-508). Section508.gov, USWDS, axe-core, WCAG. Start there; ignore the rest until the service is usable.

**COR or program manager**  
[Acquisition](#acquisition-cor--vendor-oversight) and the FedRAMP Marketplace. Know the security and accessibility evidence you will demand from vendors.

**Small business selling into government**  
FedRAMP readiness, Section 508 procurement language, CISA OSS principles, acquisition section. Prioritize artifacts you can produce: SBOMs, assessment results, VPAT/ACR.

**AI system owner or evaluator**  
[AI Governance](#ai-governance--security), then supply-chain and continuous monitoring. Do not treat model risk as separate from the rest of the stack.

---

## Foundations & Standards

- **[NIST CSRC](https://csrc.nist.gov/)** – Where the actual publications live. Start here before secondary blogs.
- **[NIST Cybersecurity Framework](https://www.nist.gov/cyberframework)** – Shared vocabulary for risk. Useful for cross-org conversation; not a control set.
- **[CISA Binding Operational Directives](https://www.cisa.gov/news-events/directives)** – Mandatory for federal civilian agencies. Not optional guidance.
- **[cio.gov](https://www.cio.gov/)** – CIO Council / OMB IT policy direction.
- **[CISA GitHub](https://github.com/cisagov)** – Official CISA tooling and content.

## NIST RMF & SP 800-53

- **[SP 800-37 Rev. 2](https://csrc.nist.gov/publications/detail/sp/800-37/rev-2/final)** – The RMF process itself.
- **[SP 800-53 Rev. 5](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final)** – The control catalog most federal systems still map to.
- **[OSCAL](https://github.com/usnistgov/OSCAL)** – Machine-readable controls, SSPs, assessment plans/results. The long-term path off Word/Excel authorization packages.
- **[OSCAL Content](https://github.com/usnistgov/oscal-content)** – NIST-maintained catalogs and profiles in OSCAL.
- **[ComplianceAsCode Content](https://github.com/ComplianceAsCode/content)** – SCAP / Ansible / Bash content mapped to baselines. Practical automation fuel.
- **[OpenSCAP](https://github.com/OpenSCAP/openscap)** – SCAP evaluation engine.
- **[CIS Benchmarks](https://www.cisecurity.org/cis-benchmarks)** – Configuration baselines often crosswalked to NIST.
- **[DISA STIGs](https://public.cyber.mil/stigs/)** – DoD hardening guides. Frequently imposed on civilian systems via contract.

## FedRAMP, OSCAL & ATO Automation

- **[FedRAMP.gov](https://www.fedramp.gov/)** – Program rules, baselines, templates.
- **[FedRAMP Marketplace](https://marketplace.fedramp.gov/)** – What is actually authorized or in process. Use this for market research, not vendor decks.
- **[GSA FedRAMP Automation](https://github.com/GSA/fedramp-automation)** – Official OSCAL baselines and templates. Check maturity before building process around it.
- **[Heimdall2](https://github.com/mitre/heimdall2)** – Visualize and store assessment results (HDF). Pairs with InSpec/SAF.
- **[SAF CLI](https://github.com/mitre/saf)** – Convert, filter, and report assessment data in pipelines.
- **[Lula](https://github.com/defenseunicorns/lula)** – OSCAL-oriented validation aimed at cloud-native systems.
- **[GovReady-Q](https://github.com/GovReady/govready-q)** – Open GRC for security documentation workflows.
- **[OSCAL Foundation](https://github.com/OSCAL-Foundation)** – Community around OSCAL adoption.

## Continuous Monitoring & Assessment

- **[CISA CSET](https://github.com/cisagov/cset)** – Structured assessment tool against multiple frameworks.
- **[InSpec](https://github.com/inspec/inspec)** – Infrastructure testing. Feeds Heimdall/SAF.
- **[MITRE ATT&CK](https://attack.mitre.org/)** – Adversary tradecraft model. Useful for detection engineering and threat-informed assessments.
- **[CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)** – Known exploited vulns with federal remediation deadlines (BOD 22-01).
- **[NVD](https://nvd.nist.gov/)** – Vulnerability metadata. Necessary but not sufficient; pair with KEV and asset context.

## Supply-Chain Security & SBOM

- **[Trivy](https://github.com/aquasecurity/trivy)** – Vulns, misconfigs, secrets, IaC, images. Broad and practical.
- **[Syft](https://github.com/anchore/syft)** – SBOM generation (SPDX / CycloneDX).
- **[Grype](https://github.com/anchore/grype)** – Scan SBOMs and images for known vulns.
- **[Cosign](https://github.com/sigstore/cosign)** – Sign and verify artifacts.
- **[OpenSSF Scorecard](https://github.com/ossf/scorecard)** – Automated signals on upstream project hygiene.
- **[SLSA](https://slsa.dev/)** – Provenance and build integrity levels.
- **[SPDX](https://spdx.dev/)** / **[CycloneDX](https://cyclonedx.org/)** – Dominant SBOM formats.
- **[CISA SBOM](https://www.cisa.gov/sbom)** – Federal SBOM expectations.
- **[SP 800-218 (SSDF)](https://csrc.nist.gov/publications/detail/sp/800-218/final)** – Secure software development practices. Increasingly tied to attestation requirements.
- **[Semgrep](https://github.com/semgrep/semgrep)** – Fast SAST for custom rules and secure patterns.

## DevSecOps, Policy-as-Code & IaC

- **[OPA](https://github.com/open-policy-agent/opa)** – Policy engine. Use when you need portable rules outside a single platform.
- **[Checkov](https://github.com/bridgecrewio/checkov)** – Static analysis for Terraform, K8s, pipelines.
- **[Cloud Custodian](https://github.com/cloud-custodian/cloud-custodian)** – Cloud policy-as-code and remediation.
- **[Terraform](https://github.com/hashicorp/terraform)** – Still the default IaC for many agencies. Confirm current license terms for your org.
- **[Kyverno](https://github.com/kyverno/kyverno)** – Kubernetes-native policy (validate / mutate / generate).

## Zero Trust & Identity

- **[SP 800-207](https://csrc.nist.gov/publications/detail/sp/800-207/final)** – Zero Trust Architecture reference.
- **[CISA Zero Trust Maturity Model](https://www.cisa.gov/zero-trust-maturity-model)** – Practical maturity framing for agencies.
- **[FICAM / idmanagement.gov](https://www.idmanagement.gov/)** – Federal identity and credential management.

## Cloud Platforms

Provider marketing pages are not a strategy. Use these as entry points, then verify current FedRAMP status in the Marketplace.

- **[AWS GovCloud](https://aws.amazon.com/govcloud-us/)**
- **[Azure Government](https://azure.microsoft.com/en-us/explore/global-infrastructure/government)**
- **[Google Cloud for Government](https://cloud.google.com/solutions/government)**
- **[FedRAMP Marketplace](https://marketplace.fedramp.gov/)** – Authoritative list of authorized and in-process offerings.
- **[CISA Cloud Security TRA](https://www.cisa.gov/resources-tools/resources/cloud-security-technical-reference-architecture)** – Federal reference architecture for cloud adoption.
- **[CISA TIC 3.0](https://www.cisa.gov/resources-tools/programs/trusted-internet-connections-tic)** – How agencies are expected to secure modern network/cloud traffic.

## Experimental Infrastructure

High-fidelity cyber experimentation, emulation, and scientific analysis. Relevant if you are building ranges, digital twins, resilience exercises, or ICS testbeds—not general-purpose app hosting.

**Orchestration**
- **[minimega](https://github.com/sandia-minimega/minimega)** – Launch and manage VMs, containers, and SDN. Laptop to cluster. The low-level engine.
- **[FIREWHEEL](https://github.com/sandialabs/firewheel)** – Modular experiment definition and orchestration on top of Emulytics. Use when you need repeatable, parameterized campaigns—not one-off lab setups.
- **[phenix](https://github.com/sandialabs/sceptre-phenix)** – Topology, orchestration, and GUI for minimega environments (including SCEPTRE workflows).

**Cyber-physical**
- **[SCEPTRE](https://sandialabs.github.io/sceptre-docs/)** – ICS/SCADA and cyber-physical emulation. For OT impact analysis, not enterprise IT ranges.

**Analysis**
- **[Dakota](https://dakota.sandia.gov/)** – Design of experiments, UQ, sensitivity, calibration. Pair with expensive simulations so you are not guessing parameter space.
- **[Pyomo](https://www.pyomo.org/)** – Optimization modeling in Python.

**AI tooling for regulated environments**
- **[Atlas UI 3](https://github.com/sandialabs/atlas-ui-3)** – Governed AI agents: MCP, access control, audit trails. Built for high-trust engineering contexts.
- **[TalkPipe](https://github.com/sandialabs/talkpipe)** – Streaming AI pipelines and composable RAG. Scriptable, not chat-demo oriented.

**Networking**
- **[wiretap](https://github.com/sandialabs/wiretap)** – WireGuard-based tunneling without privileged server setup. Useful in constrained or segmented experiment networks.

These are research/ops infrastructure projects. Expect operational overhead. Read licenses and deployment assumptions before you commit a range design to them.

## Containers, Kubernetes & Platforms

- **[Kubernetes](https://github.com/kubernetes/kubernetes)** – Default orchestration target for many federal platforms. Hardening and admission control are not optional.
- **[Platform One Big Bang](https://github.com/DoD-Platform-One/bigbang)** – DoD reference packaging and GitOps delivery for hardened cloud-native stacks. Treat as a reference architecture, not a free ATO.
- **[Falco](https://github.com/falcosecurity/falco)** – Runtime detection for containers and hosts.

## Observability & Incident Response

- **[OpenTelemetry](https://opentelemetry.io/)** – Vendor-neutral telemetry. Prefer this over proprietary agent lock-in where you can.
- **[Prometheus](https://github.com/prometheus/prometheus)** – Metrics and alerting. Common in cloud-native continuous monitoring.
- **[Grafana](https://github.com/grafana/grafana)** – Dashboards. Confirm edition/license fit for your agency.
- **[Wazuh](https://github.com/wazuh/wazuh)** – Open XDR/SIEM-style monitoring. Evaluate agent privilege and rule quality before wide deploy.
- **[MITRE ATT&CK](https://attack.mitre.org/)** – Already listed under continuous monitoring; also the backbone for many detection programs.
- **[CISA cyber threat resources](https://www.cisa.gov/topics/cyber-threats-and-advisories)** – Advisories and incident-response material.

## Accessibility & Section 508

- **[Section508.gov](https://www.section508.gov/)** – Authoritative federal accessibility policy, testing, and procurement language.
- **[USWDS](https://github.com/uswds/uswds)** / **[designsystem.digital.gov](https://designsystem.digital.gov/)** – Component system for consistent, accessible federal sites.
- **[WCAG](https://www.w3.org/WAI/standards-guidelines/wcag/)** – The technical standard Section 508 points at.
- **[axe-core](https://github.com/dequelabs/axe-core)** – Automated testing. Necessary; not sufficient. Still do manual and AT testing.
- **[18F Accessibility Guide](https://accessibility.18f.gov/)** – Practical delivery guidance.
- **[Digital.gov](https://digital.gov/)** – Broader digital service practice.

## AI Governance & Security

- **[NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework)** – Primary federal frame for AI risk.
- **[NIST AI 600-1 (Generative AI Profile)](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf)** – Generative-AI-specific application of the RMF.
- **[MITRE ATLAS](https://atlas.mitre.org/)** – Adversary tactics against ML systems.
- **[OWASP Top 10 for LLM Apps](https://genai.owasp.org/llm-top-10/)** – Practical risk list for LLM-integrated applications.
- **[CISA OSS Security Principles](https://www.cisa.gov/resources-tools/resources/open-source-software-security-principles-and-practices)** – Includes OSS/AI considerations for agencies.

## Privacy, Records & Data Governance

- **[NIST Privacy Framework](https://www.nist.gov/privacy-framework)** – Privacy risk management parallel to the CSF.
- **[NARA Records Management](https://www.archives.gov/records-mgmt)** – Federal records obligations do not go away because the system is modern.

## Acquisition, COR & Vendor Oversight

- **[Acquisition.gov](https://www.acquisition.gov/)** – FAR and agency supplements.
- **[Federal Acquisition Institute](https://www.fai.gov/)** – COR and acquisition workforce training.
- **[FedRAMP Marketplace](https://marketplace.fedramp.gov/)** – Authorized cloud services for market research.
- **[TechFAR Handbook](https://techfarhub.cio.gov/)** – Using the FAR to buy digital services without performing ritual theater.
- Section 508 procurement language lives on [Section508.gov](https://www.section508.gov/). Use it in solicitations.

## Open Source Policy

- **[CISA OSS Security Principles and Practices](https://www.cisa.gov/resources-tools/resources/open-source-software-security-principles-and-practices)** – Current authoritative agency guidance on using OSS.
- **[Federal Source Code Policy](https://sourcecode.cio.gov/)** – Code reuse and release expectations.
- **[Code.gov](https://code.gov/)** – Discovery for published federal code.
- **[OpenSSF](https://openssf.org/)** – Cross-industry OSS security initiatives (Scorecard, SLSA, etc.).

## Training, Communities & Case Studies

- **[Digital.gov](https://digital.gov/)** – Communities of practice and case studies.
- **[18F GitHub](https://github.com/18F)** – Patterns and historical digital service work. Some repos are archival; check activity.
- **[Digital Services Playbook](https://playbook.cio.gov/)** – Thirteen practices that still describe the gap between good and typical delivery.
- OWASP materials for application security education.
- NIST and CISA training portals on their respective sites.

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) and [inclusion criteria](docs/inclusion-criteria.md).

Submit via the Resource Submission issue template. Canonical data lives in `data/resources.yml` and is validated in CI.

## Security & Disclaimer

**Inclusion is not endorsement by the U.S. Government or any agency.**

You must:

- Evaluate third-party tools for security, supply-chain risk, license, and fitness yourself
- Follow your agency’s authorization process for open-source software
- Prefer projects that publish SBOMs, signed releases, and clear security contacts
- Track NVD, CISA KEV, and project advisories

See [SECURITY.md](SECURITY.md) for issues with this repository.

## License

Repository content: [CC BY 4.0](LICENSE).

Listed projects keep their own licenses. Read them before use.
