# CMU SEI Crucible Ecosystem

Carnegie Mellon University Software Engineering Institute (SEI) maintains the Crucible family of tools for cyber training, exercise, and simulation. Public components include:

| Component | Repository | Role |
|-----------|------------|------|
| GHOSTS | cmu-sei/GHOSTS | Realistic NPC / synthetic-user behavior, traffic, social/cognitive models |
| TopoMojo | cmu-sei/TopoMojo | Virtual lab / topology builder and player |
| Steamfitter | (Crucible component; Helm charts under cmu-sei/helm-charts) | Scenario task orchestration and inject execution |
| Gallery / Player / Alloy / Blueprint / CITE / Polar | Various cmu-sei repos | Content, session, graph, and UI layers for multi-team exercises |

GHOSTS is the most mature and widely referenced public component; it produces authentic user activity for ranges and can be driven by higher-level exercise controllers.

**Usage pattern.** TopoMojo provisions environments; Steamfitter and related services schedule injects and tasks; GHOSTS populates the environment with realistic human activity; higher-level Crucible services coordinate multi-team scenarios.

Confirm current public availability of each Crucible microservice; some components are distributed primarily via Helm charts or internal SEI channels.
