# Accessible Information Emulytics

## Definition

**Accessible Information Emulytics** is a rigorous experimentation framework for measuring how infrastructure failures, communications systems, accessibility barriers, and information quality affect human decisions and emergency outcomes.

It extends classic Emulytics (high-fidelity cyber and cyber-physical experimentation) with an explicit human-centered information-burden layer.

## Causal chain

```
World → People → Information → Burden → Decision → Outcome
```

- **World**: physical and cyber infrastructure state (outages, attacks, degraded sensors).
- **People**: operators, first responders, public, D/HH communities, limited-English speakers.
- **Information**: alerts, captions, ASL interpretation, sensor feeds, status messages.
- **Burden**: delay, intelligibility, device access, cognitive load, trust, language, literacy.
- **Decision**: whether and how a person acts.
- **Outcome**: safety, recovery time, equity of impact.

## How existing platforms support the lower layers

Existing federal and laboratory tools already provide strong support for the *World* and early *People/Information* layers:

| Layer support | Tools |
|---------------|-------|
| Experiment orchestration | FIREWHEEL, phenix |
| Environments / ranges | minimega, TopoMojo |
| Cyber-physical fidelity | SCEPTRE / ARCADE-style components |
| Synthetic users | GHOSTS (behavior, traffic, artifacts) |
| Adversary behavior | CALDERA |
| Exercise injects | Gallery, Steamfitter (Crucible) |
| Uncertainty quantification | Dakota |
| Optimization | Pyomo |
| Provenance | Flowcept |
| Analysis pipelines | TalkPipe |
| Governed interaction | Atlas UI 3 |

These platforms can instantiate infrastructure failures, inject adversary actions, generate realistic background activity, and record outcomes with provenance.

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

1. high-fidelity cyber / cyber-physical environments (minimega + phenix / FIREWHEEL + SCEPTRE),
2. synthetic populations (GHOSTS),
3. adversary and inject control (CALDERA + Crucible components),
4. scientific analysis (Dakota, Flowcept, TalkPipe),

creates a natural substrate for *Accessible Information Emulytics* research. The open gap is the human-factors instrumentation and outcome model itself.

This catalog records the substrate; it does not claim that the accessibility-burden measurement layer already exists.
