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
| Orchestration | Experiment graph, scheduling, automation | FIREWHEEL, phēnix / SCORCH |
| Provenance | Capture of workflow and result lineage | Flowcept |
| Uncertainty / design | Campaign design, sensitivity, UQ | Dakota |
| Assessment | Result normalization and evidence | Heimdall2, SAF CLI |

**Notes.** FIREWHEEL and phēnix both operate in the Sandia experimentation ecosystem around minimega. SCORCH adds repeatable scenario pipelines, breakpoints, and artifact-producing stages to phēnix experiments. GHOSTS and CALDERA could participate as model components or external actors, but those compositions require integration adapters. Flowcept is a candidate provenance layer for multi-tool campaigns.

## Reference Architecture 2: Cyber-Physical Resilience

**Purpose.** High-fidelity emulation of critical infrastructure coupled to cyber attack, control-system behavior, physical-process simulation, and measurable consequences.

| Layer | Role | Representative components |
|-------|------|---------------------------|
| Experiment control | Topology, lifecycle, repeatable campaign stages | phēnix, SCORCH, FIREWHEEL |
| Cyber environment | VMs, networks, traffic, attacker and defender systems | minimega, phēnix topologies |
| Field-device / ICS boundary | Virtual RTUs, SCADA interfaces, HIL integration | Bennu / Pybennu |
| Co-simulation / provider boundary | Connect process models and distributed simulators | HELICS, Bennu providers |
| Physical / domain models | Power, process, waterway, grid, custom simulation | PowerWorld, OpenDSS, PyPower, Simulink, GenericPython, other solvers |
| Optimization / UQ | Parameter studies, reliability, design | Dakota, Pyomo |
| Provenance | Reproducibility of multi-stage runs | Flowcept and experiment artifacts |

**Notes.** Public SCEPTRE material is distributed across phēnix, Bennu, images, apps, documentation, and reusable topologies. The architecture is modular: phēnix/minimega instantiate the environment, Bennu exposes control-system and field-device state, and providers couple that state to process solvers or external systems. The GenericPython provider is a particularly useful extension seam for lightweight domain models that do not require a commercial or heavyweight engineering simulator.

This makes SCEPTRE best treated as a **lower-world execution substrate**, not a complete human or societal world model. It can produce and perturb infrastructure state while separate layers model information availability, human behavior, accessibility burden, decisions, and outcomes.

## Reference Architecture 3: High-Assurance AI Operations

**Purpose.** Governed agentic workflows with audit, tool approval, provenance, and authorization evidence suitable for regulated environments.

| Layer | Role | Representative components |
|-------|------|---------------------------|
| Governed access | Multi-LLM agents, MCP, access control, audit | Atlas UI 3 |
| Pipeline composition | Reproducible AI / RAG pipelines | TalkPipe |
| Evidence graph | Relationships among artifacts and controls | Polar (or equivalent) |
| Provenance | Runtime capture of agent and workflow steps | Flowcept |
| Authorization evidence | OSCAL / assessment packaging | SAF, Heimdall2, eMASSer, OSCAL |

**Notes.** Atlas UI 3 is designed for high-trust engineering environments. TalkPipe could supply a composable pipeline layer. Flowcept and the MITRE SAF family are candidate provenance and evidence layers; integration would require project-specific adapters.

## Maturity distinctions

- **Mature / production-oriented:** minimega, CALDERA, GHOSTS, Conduit, Dakota, SAF/Heimdall, eMASSer.
- **Actively evolving research platforms:** FIREWHEEL, phēnix/SCEPTRE, Bennu, Atlas UI 3, TalkPipe, Flowcept, TopoMojo / Crucible components.
- **Domain-specific or early-stage:** many ARCADE / gait / protonuke components and individual research topologies; treat them as research artifacts until evaluated.

Always confirm current license, last meaningful activity, privilege model, image provenance, authentication defaults, and isolation assumptions before range or production use.
