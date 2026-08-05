# MITRE Security Automation Framework (SAF) and related tooling

MITRE maintains a family of tools that turn security assessment results into structured, pipeline-friendly evidence and support adversary emulation.

| Component | Repository | Role |
|-----------|------------|------|
| SAF CLI | mitre/saf | Convert, filter, validate, and report assessment data (HDF, InSpec, etc.) |
| Heimdall2 | mitre/heimdall2 | Store and visualize assessment results |
| CALDERA | apache/caldera (MITRE origin) | Automated adversary emulation (ATT&CK) |
| eMASSer | mitre/emasser | CLI automation against the eMASS REST API for RMF evidence |
| Vulcan | mitre/vulcan | STIG authoring and InSpec profile development from SRGs |

**Usage pattern.** CALDERA generates adversary activity inside a range; SAF/Heimdall normalize and visualize assessment outputs; eMASSer and OSCAL tooling move evidence into formal authorization packages; Vulcan supports content creation for automated validation.

These tools are complementary to Emulytics and Crucible platforms rather than replacements.
