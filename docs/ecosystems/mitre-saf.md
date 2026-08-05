# MITRE Security Automation Framework (SAF) and related tooling

MITRE maintains a family of tools that turn security assessment results into structured, pipeline-friendly evidence and support adversary emulation.

| Component | Repository | Role |
|-----------|------------|------|
| SAF CLI | mitre/saf | Convert, filter, validate, and report assessment data (HDF, InSpec, etc.) |
| Heimdall2 | mitre/heimdall2 | Store and visualize assessment results |
| Apache CALDERA | apache/caldera (MITRE origin) | Automated adversary emulation (ATT&CK) |
| eMASSer | mitre/emasser | CLI automation against the eMASS REST API for RMF evidence |
| Vulcan | mitre/vulcan | STIG authoring and InSpec profile development from SRGs |

**Potential usage pattern.** CALDERA can generate adversary activity inside a range; SAF and Heimdall can normalize and visualize compatible assessment outputs; eMASSer and OSCAL tooling can support evidence transfer into authorization workflows; Vulcan supports content creation for automated validation. These are complementary projects, not a pre-integrated stack.

These tools are complementary to Emulytics and Crucible platforms rather than replacements.
