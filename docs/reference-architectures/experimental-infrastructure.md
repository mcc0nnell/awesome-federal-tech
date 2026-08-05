# Experimental Infrastructure and Scientific Assurance

This note describes how mature federal and national-laboratory platforms compose into usable capability stacks for cyber experimentation, cyber-physical resilience analysis, and high-assurance AI operations.

These are not product recommendations. They are patterns observed across Sandia Emulytics, CMU SEI Crucible, MITRE SAF/Caldera, and DOE laboratory scientific infrastructure. Operators must still perform their own authorization, isolation, and supply-chain evaluation.

## Reference Architecture 1: Cyber Experimentation

**Purpose.** Repeatable, instrumented campaigns that combine adversary behavior, synthetic users, virtualized environments, and provenance for analysis.

| Layer | Role | Representative components |
|-------|------|---------------------------|
| Adversary behavior | Automated ATT&CK-aligned actions | CALDERA (and OT plugins) |
| Synthetic users | Realistic traffic, artifacts, cognitive models | GHOSTS |
| Environment | VMs, containers, SDN topologies | minimega, TopoMojo |
| Orchestration | Experiment graph, scheduling, automation | FIREWHEEL, Steamfitter / phenix |
| Provenance | Capture of workflow and result lineage | Flowcept |
| Uncertainty / design | Campaign design, sensitivity, UQ | Dakota |
| Assessment | Result normalization and evidence | Heimdall2, SAF CLI |

**Notes.** FIREWHEEL and phenix sit naturally on minimega. GHOSTS and CALDERA can be injected as model components or as external actors. Flowcept provides the missing reproducibility layer for multi-tool campaigns.

## Reference Architecture 2: Cyber-Physical Resilience

**Purpose.** High-fidelity emulation of critical infrastructure (ICS/OT, power, process control) coupled to cyber attack and consequence modeling.

| Layer | Role | Representative components |
|-------|------|---------------------------|
| Physical fidelity | Process simulation and field-device models | SCEPTRE / ARCADE-style components |
| Orchestration | Topology + experiment control | phenix, FIREWHEEL |
| Domain models | Grid or infrastructure optimization / consequence | ExaGO (power), other domain codes |
| Data exchange | In-core and file-based scientific data | Conduit |
| Optimization / UQ | Parameter studies, reliability, design | Dakota, Pyomo |
| Provenance | Reproducibility of multi-physics runs | Flowcept |

**Notes.** SCEPTRE workflows are commonly driven through phenix on minimega. Conduit is the established LLNL data model for coupling simulation packages. Dakota/Pyomo close the analysis loop.

## Reference Architecture 3: High-Assurance AI Operations

**Purpose.** Governed agentic workflows with audit, tool approval, provenance, and authorization evidence suitable for regulated environments.

| Layer | Role | Representative components |
|-------|------|---------------------------|
| Governed access | Multi-LLM agents, MCP, access control, audit | Atlas UI 3 |
| Pipeline composition | Reproducible AI / RAG pipelines | TalkPipe |
| Evidence graph | Relationships among artifacts and controls | Polar (or equivalent) |
| Provenance | Runtime capture of agent and workflow steps | Flowcept |
| Authorization evidence | OSCAL / assessment packaging | SAF, Heimdall2, eMASSer, OSCAL |

**Notes.** Atlas UI 3 is explicitly designed for high-trust engineering environments. TalkPipe supplies the composable pipeline layer. Flowcept and the MITRE SAF family close the assurance and evidence loop.

## Maturity distinctions

- **Mature / production-oriented:** minimega, CALDERA, GHOSTS, Conduit, Dakota, SAF/Heimdall, eMASSer.
- **Actively evolving research platforms:** FIREWHEEL, phenix/SCEPTRE, Atlas UI 3, TalkPipe, Flowcept, TopoMojo / Crucible components.
- **Domain-specific or early-stage:** many ARCADE / gait / protonuke components; treat as research artifacts until evaluated.

Always confirm current license, last meaningful activity, privilege model, and isolation assumptions before range or production use.
