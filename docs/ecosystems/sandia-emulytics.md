# Sandia Emulytics Ecosystem

Sandia National Laboratories' Emulytics program provides modular, high-fidelity cyber and cyber-physical experimentation infrastructure. Core public components:

| Component | Repository | Role |
|-----------|------------|------|
| minimega | sandia-minimega/minimega | Lightweight VM/container/SDN orchestration (laptop to cluster) |
| FIREWHEEL | sandialabs/firewheel | Experiment orchestration, model components, repeatable campaigns |
| phenix | sandialabs/sceptre-phenix | Topology/orchestration UI and workflow engine for minimega (incl. SCEPTRE) |
| wiretap | sandialabs/wiretap | Privilege-light WireGuard tunneling for segmented experiment networks |
| Atlas UI 3 | sandialabs/atlas-ui-3 | Governed AI agents (MCP, access control, audit) |
| TalkPipe | sandialabs/talkpipe | Streaming AI / RAG pipeline composition |
| Dakota | snl-dakota/dakota | Optimization, UQ, sensitivity analysis |

Supporting model-component repositories (firewheel_repo_*) and SCEPTRE documentation exist under sandialabs. Many internal ARCADE / gait / protonuke components remain research or limited-release.

**Usage pattern.** FIREWHEEL or phenix drives experiments on minimega; model components encapsulate services, networks, and ICS elements; Dakota closes the analysis loop; Atlas/TalkPipe support governed AI-assisted post-processing.

Evaluate privilege requirements, image provenance, and isolation carefully before operational range use.
