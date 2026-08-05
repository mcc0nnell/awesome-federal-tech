# awesome-federal-tech

A curated, practitioner-focused collection of primary sources, official guidance, and actively maintained open-source projects that support the full lifecycle of federal technology delivery.

**This is not a link dump.**  
It emphasizes the practical bridges between requirements, acquisition, architecture, security authorization (NIST RMF / FedRAMP / ATO), accessibility (Section 508), deployment, operations, and continuous monitoring.

Inclusion is never an endorsement. Users must independently evaluate every third-party tool and resource for security, license compliance, and fitness for purpose in their environment.

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

**System Owner or ISSO / ISSM pursuing or maintaining an ATO**  
Begin with [NIST RMF & SP 800-53](#nist-rmf--sp-800-53), then [FedRAMP, OSCAL & ATO Automation](#fedramp-oscal--ato-automation), [Continuous Monitoring](#continuous-monitoring--assessment), and [Supply-Chain Security](#supply-chain-security--sbom). Review Heimdall, SAF, ComplianceAsCode, and official OSCAL content.

**Cloud Architect or DevSecOps Engineer**  
Start with [Cloud Platforms](#cloud-platforms), [Containers & Kubernetes](#containers-kubernetes--platforms), [DevSecOps](#devsecops-policy-as-code--iac), and [Supply-Chain](#supply-chain-security--sbom). Platform One / Big Bang, Trivy, Syft/Grype, Cosign, OPA, Checkov, and Cloud Custodian are high-value.

**Accessibility Specialist or Digital Service Team**  
Go directly to [Accessibility & Section 508](#accessibility--section-508). USWDS, axe-core, Section508.gov, and WCAG are foundational.

**Contracting Officer’s Representative (COR) or Program Manager**  
See [Acquisition, COR & Vendor Oversight](#acquisition-cor--vendor-oversight) and the FedRAMP Marketplace. Understand the security and accessibility requirements you will oversee.

**Small Business entering federal markets**  
Review FedRAMP readiness materials, Section 508 procurement guidance, CISA open-source software principles, and the acquisition section. Focus on evidence you can produce (SBOMs, assessment results, accessibility conformance).

**AI System Owner or Evaluator**  
See [AI Governance & Security](#ai-governance--security) and the CISA OSS / AI-related guidance. Pair with supply-chain and continuous monitoring practices.

---

## Foundations & Standards

- **[NIST Computer Security Resource Center](https://csrc.nist.gov/)** – Central portal for NIST cybersecurity and privacy publications.
- **[NIST Cybersecurity Framework](https://www.nist.gov/cyberframework)** – Common language and methodology for managing cybersecurity risk.
- **[CISA Binding Operational Directives](https://www.cisa.gov/news-events/directives)** – Mandatory cybersecurity requirements for federal agencies.
- **[cio.gov](https://www.cio.gov/)** – Federal CIO Council and OMB IT policy direction.
- **[CISA GitHub Organization](https://github.com/cisagov)** – Official CISA open-source tools and content.

## NIST RMF & SP 800-53

- **[NIST SP 800-37 Rev. 2](https://csrc.nist.gov/publications/detail/sp/800-37/rev-2/final)** – Risk Management Framework process guidance.
- **[NIST SP 800-53 Rev. 5](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final)** – Security and Privacy Controls catalog.
- **[NIST OSCAL](https://github.com/usnistgov/OSCAL)** – Open Security Controls Assessment Language models and tooling.
- **[NIST OSCAL Content](https://github.com/usnistgov/oscal-content)** – Machine-readable SP 800-53 catalog and baselines.
- **[ComplianceAsCode Content](https://github.com/ComplianceAsCode/content)** – SCAP, Ansible, and Bash content mapped to NIST and STIG baselines.
- **[OpenSCAP](https://github.com/OpenSCAP/openscap)** – SCAP evaluation engine.
- **[CIS Benchmarks](https://www.cisecurity.org/cis-benchmarks)** – Consensus configuration guidelines frequently mapped to NIST controls.
- **[DISA STIGs](https://public.cyber.mil/stigs/)** – DoD Security Technical Implementation Guides.

## FedRAMP, OSCAL & ATO Automation

- **[FedRAMP.gov](https://www.fedramp.gov/)** – Official program site, baselines, templates, and guidance.
- **[FedRAMP Marketplace](https://marketplace.fedramp.gov/)** – Authorized and in-process cloud service offerings.
- **[GSA FedRAMP Automation](https://github.com/GSA/fedramp-automation)** – OSCAL baselines, templates, and registry (check current status).
- **[MITRE Heimdall2](https://github.com/mitre/heimdall2)** – Visualization and storage of assessment results in HDF.
- **[MITRE SAF CLI](https://github.com/mitre/saf)** – Conversion, reporting, and pipeline integration for security automation.
- **[Lula](https://github.com/defenseunicorns/lula)** – OSCAL-based compliance validation, especially for cloud-native systems.
- **[GovReady-Q](https://github.com/GovReady/govready-q)** – Self-service GRC and compliance documentation platform.
- **[OSCAL Foundation](https://github.com/OSCAL-Foundation)** – Community resources supporting OSCAL adoption.

## Continuous Monitoring & Assessment

- **[CISA CSET](https://github.com/cisagov/cset)** – Cyber Security Evaluation Tool.
- **[InSpec](https://github.com/inspec/inspec)** – Infrastructure testing and compliance framework (pairs with SAF/Heimdall).
- **[MITRE ATT&CK](https://attack.mitre.org/)** – Adversary tactics and techniques knowledge base.
- **[CISA KEV Catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)** – Known Exploited Vulnerabilities (binding under BOD 22-01).
- **[NIST NVD](https://nvd.nist.gov/)** – National Vulnerability Database.

## Supply-Chain Security & SBOM

- **[Trivy](https://github.com/aquasecurity/trivy)** – Comprehensive vulnerability and misconfiguration scanner.
- **[Syft](https://github.com/anchore/syft)** – SBOM generation.
- **[Grype](https://github.com/anchore/grype)** – Vulnerability scanning from SBOMs.
- **[Cosign](https://github.com/sigstore/cosign)** – Signing and verification of artifacts (Sigstore).
- **[OpenSSF Scorecard](https://github.com/ossf/scorecard)** – Automated security posture checks for open-source projects.
- **[SLSA](https://slsa.dev/)** – Supply-chain Levels for Software Artifacts.
- **[SPDX](https://spdx.dev/)** and **[CycloneDX](https://cyclonedx.org/)** – Primary SBOM standards.
- **[CISA SBOM Resources](https://www.cisa.gov/sbom)** – Federal guidance on Software Bills of Materials.
- **[NIST SP 800-218 (SSDF)](https://csrc.nist.gov/publications/detail/sp/800-218/final)** – Secure Software Development Framework.
- **[Semgrep](https://github.com/semgrep/semgrep)** – Lightweight static analysis.

## DevSecOps, Policy-as-Code & IaC

- **[Open Policy Agent (OPA)](https://github.com/open-policy-agent/opa)** – General-purpose policy engine.
- **[Checkov](https://github.com/bridgecrewio/checkov)** – Infrastructure-as-code static analysis.
- **[Cloud Custodian](https://github.com/cloud-custodian/cloud-custodian)** – Cloud policy-as-code and automated remediation.
- **[Terraform](https://github.com/hashicorp/terraform)** – Infrastructure-as-code (confirm current license terms for your organization).
- **[Kyverno](https://github.com/kyverno/kyverno)** – Kubernetes-native policy engine.

## Zero Trust & Identity

- **[NIST SP 800-207](https://csrc.nist.gov/publications/detail/sp/800-207/final)** – Zero Trust Architecture.
- **[CISA Zero Trust Maturity Model](https://www.cisa.gov/zero-trust-maturity-model)** – Implementation maturity guidance.
- **[FICAM / idmanagement.gov](https://www.idmanagement.gov/)** – Federal identity, credential, and access management resources.

## Cloud Platforms

- Official guidance from **AWS GovCloud**, **Azure Government**, and **Google Public Sector** (consult current provider documentation for federal regions and compliance programs).
- **[FedRAMP Marketplace](https://marketplace.fedramp.gov/)** remains the primary discovery mechanism for authorized offerings.

## Experimental Infrastructure

These projects provide foundational capabilities for high-fidelity cyber experimentation and scientific analysis. Rather than duplicating their functionality, they can serve as the underlying infrastructure for resilience simulations, digital twins, accessibility research, cyber ranges, and operational exercises.

### Experiment Orchestration

- **[FIREWHEEL](https://github.com/sandialabs/firewheel)** – Modular experiment definition, orchestration, and repeatable cyber experimentation (Sandia Emulytics).
- **[phenix](https://github.com/sandialabs/sceptre-phenix)** – Experiment topology management, orchestration, and visualization for minimega-based environments.
- **[minimega](https://github.com/sandia-minimega/minimega)** – Lightweight VM, container, and software-defined network orchestration at laptop-to-cluster scale.

### Cyber-Physical Systems

- **[SCEPTRE](https://sandialabs.github.io/sceptre-docs/)** – ICS/SCADA and cyber-physical system emulation for industrial control research.

### Analysis & Scientific Computing

- **[Dakota](https://dakota.sandia.gov/)** – Design of experiments, uncertainty quantification, sensitivity analysis, optimization, and model calibration.
- **[Pyomo](https://www.pyomo.org/)** – Mathematical optimization modeling for engineering and operations research.

### AI & Automation

- **[Atlas UI 3](https://github.com/sandialabs/atlas-ui-3)** – Governed AI assistants, MCP integration, access control, and auditability for regulated environments.
- **[TalkPipe](https://github.com/sandialabs/talkpipe)** – Streaming AI pipelines and composable RAG workflows.

### Networking & Connectivity

- **[wiretap](https://github.com/sandialabs/wiretap)** – Privilege-light WireGuard-based networking for constrained or segmented environments.

These projects support reproducible cyber experimentation and are relevant for digital twins, resilience platforms, cyber ranges, accessibility research environments, and operational exercises.

## Containers, Kubernetes & Platforms

- **[Kubernetes](https://github.com/kubernetes/kubernetes)** – Core orchestration platform.
- **[DoD Platform One Big Bang](https://github.com/DoD-Platform-One/bigbang)** – Hardened package set and continuous delivery approach for DoD DevSecOps reference architectures.
- **[Falco](https://github.com/falcosecurity/falco)** – Runtime security detection for containers and hosts.

## Observability & Incident Response

- **[OpenTelemetry](https://opentelemetry.io/)** – Vendor-neutral telemetry standards.
- **[Prometheus](https://github.com/prometheus/prometheus)** and **[Grafana](https://github.com/grafana/grafana)** – Common monitoring and visualization stack (confirm license acceptability for Grafana).

## Accessibility & Section 508

- **[Section508.gov](https://www.section508.gov/)** – Authoritative federal accessibility resources and procurement guidance.
- **[USWDS](https://github.com/uswds/uswds)** and **[designsystem.digital.gov](https://designsystem.digital.gov/)** – U.S. Web Design System.
- **[W3C WCAG](https://www.w3.org/WAI/standards-guidelines/wcag/)** – Web Content Accessibility Guidelines.
- **[axe-core](https://github.com/dequelabs/axe-core)** – Automated accessibility testing engine.
- **[18F Accessibility Guide](https://accessibility.18f.gov/)** – Practical federal digital service accessibility guidance.
- **[Digital.gov](https://digital.gov/)** – Broader federal digital service resources.

## AI Governance & Security

- **[NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)** – Primary federal reference for AI risk management.
- **[CISA Open Source Software Security Principles and Practices](https://www.cisa.gov/resources-tools/resources/open-source-software-security-principles-and-practices)** – Includes considerations for open-source AI systems.

## Privacy, Records & Data Governance

- **[NIST Privacy Framework](https://www.nist.gov/privacy-framework)** – Privacy risk management.
- **[NARA Records Management](https://www.archives.gov/records-mgmt)** – Federal records requirements.

## Acquisition, COR & Vendor Oversight

- **[Acquisition.gov](https://www.acquisition.gov/)** – Federal Acquisition Regulation and related content.
- **[Federal Acquisition Institute](https://www.fai.gov/)** – COR and acquisition workforce training and resources.
- **[FedRAMP Marketplace](https://marketplace.fedramp.gov/)** – Market research for authorized cloud services.
- Section 508 procurement language and accessibility requirements (via Section508.gov).

## Open Source Policy

- **[CISA Open Source Software Security Principles and Practices](https://www.cisa.gov/resources-tools/resources/open-source-software-security-principles-and-practices)** – Current authoritative guidance for federal agencies.
- **[OpenSSF](https://openssf.org/)** – Cross-industry open-source security initiatives.

## Training, Communities & Case Studies

- **[Digital.gov](https://digital.gov/)** – Communities of practice and case studies.
- **[18F / TTS-related public repositories](https://github.com/18F)** – Patterns and historical digital service work.
- OWASP materials for application security education.
- NIST and CISA training portals (see respective agency sites).

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) and the [inclusion criteria](docs/inclusion-criteria.md).

Use the Resource Submission issue template. All entries live in `data/resources.yml` and are validated automatically.

## Security & Disclaimer

**Inclusion of any resource is not an endorsement by the United States Government or any agency thereof.**

Users of this repository **must**:

- Independently evaluate every third-party tool for security, supply-chain risk, license terms, and fitness for purpose.
- Follow their agency’s processes for authorizing open-source software.
- Prefer projects that publish SBOMs, signed releases, and transparent security practices.
- Monitor for known vulnerabilities (NVD, CISA KEV, project advisories).

See [SECURITY.md](SECURITY.md) for reporting issues related to this repository itself.

## License

Content in this repository is licensed under [Creative Commons Attribution 4.0 International](LICENSE).

Individual projects retain their own licenses. Always review the license of any tool before use.
