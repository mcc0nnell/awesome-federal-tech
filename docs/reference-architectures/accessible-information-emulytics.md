# Accessible Information Emulytics

## Definition

**Accessible Information Emulytics** is a rigorous experimentation framework for measuring how infrastructure failures, communications systems, accessibility barriers, and information quality affect human decisions and emergency outcomes.

It extends classic Emulytics (high-fidelity cyber and cyber-physical experimentation) with an explicit human-centered information-burden layer.

## Causal chain

```text
World → People → Information → Burden → Decision → Outcome
```

- **World**: physical and cyber infrastructure state (outages, attacks, degraded sensors).
- **People**: operators, first responders, public, D/HH communities, limited-English speakers.
- **Information**: alerts, captions, ASL interpretation, sensor feeds, status messages.
- **Burden**: delay, intelligibility, device access, cognitive load, trust, language, literacy.
- **Decision**: whether and how a person acts.
- **Outcome**: safety, recovery time, equity of impact.

## How existing platforms support the lower layers

Existing federal and laboratory tools offer candidate building blocks for the *World* and early *People/Information* layers:

| Layer support | Tools |
|---------------|-------|
| Experiment orchestration | FIREWHEEL, phēnix / SCORCH |
| Environments / ranges | minimega, TopoMojo |
| Cyber-physical fidelity | SCEPTRE, Bennu / Pybennu, HELICS-connected providers |
| Lightweight custom process models | Bennu GenericPython provider |
| Synthetic users | GHOSTS (behavior, traffic, artifacts) |
| Adversary behavior | CALDERA |
| Exercise injects | Gallery, Steamfitter (Crucible), SCORCH stages |
| Uncertainty quantification | Dakota |
| Optimization | Pyomo |
| Provenance | Flowcept |
| Analysis pipelines | TalkPipe |
| Governed interaction | Atlas UI 3 |

These platforms can support infrastructure-failure experiments, adversary actions, realistic background activity, cyber-physical state changes, repeatable campaign execution, and provenance. Combining them into one campaign would require explicit adapters and validation.

## SCEPTRE integration boundary

SCEPTRE is especially useful for the **World** side of the causal chain because its public architecture separates experiment orchestration from process simulation:

```text
phēnix / SCORCH
        ↓
minimega environment
        ↓
Bennu virtual field devices
        ↓
provider / co-simulation boundary
        ↓
physical or domain model
```

This means Accessible Information Emulytics does not need to build a cyber range, SCADA emulator, hardware-in-the-loop layer, or universal physics engine from scratch.

A domain model can expose infrastructure state through Bennu while the human-centered layer observes the consequences. A lightweight pilot could use the GenericPython provider to model an information dependency such as:

```text
power availability
    ↓
cell-site / backhaul state
    ↓
alert delivery availability
    ↓
caption / ASL / device pathway state
    ↓
information burden
    ↓
decision and outcome
```

The important boundary is architectural: SCEPTRE generates or perturbs the lower-world state; Accessible Information Emulytics measures what that state means to people.

## The missing layer (explicit gap)

Existing platforms simulate systems, infrastructure, adversaries, and users.

**They do not yet implement a human-centered model of accessibility and information burden.**

The missing measurement layer includes:

- message receipt and delivery delay
- intelligibility (audio, caption quality, ASL access)
- language and literacy barriers
- device and connectivity access
- cognitive burden and trust
- decision delay and error modes
- differential outcome impact across populations

No current public repository listed in this catalog provides a validated, instrumented model of these factors that can be coupled to Emulytics-style campaigns.

## Research opportunity

The combination of:

1. high-fidelity cyber / cyber-physical environments (minimega + phēnix / FIREWHEEL + SCEPTRE),
2. modular process simulation (Bennu providers, HELICS, GenericPython, domain solvers),
3. synthetic populations (GHOSTS),
4. adversary and inject control (CALDERA + Crucible components + SCORCH),
5. scientific analysis and provenance (Dakota, Flowcept, TalkPipe),

could create a useful substrate for *Accessible Information Emulytics* research. The open gap is the human-factors instrumentation and outcome model itself.

This catalog records the substrate; it does not claim that the accessibility-burden measurement layer already exists.
