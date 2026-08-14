# Sandia Emulytics Ecosystem

Sandia National Laboratories' Emulytics work provides modular, high-fidelity cyber and cyber-physical experimentation infrastructure. The public repositories are best understood as a family of cooperating layers rather than one monolithic simulator.

| Component | Repository | Role |
|-----------|------------|------|
| minimega | sandia-minimega/minimega | VM, container, network, and SDN emulation from laptop-scale experiments to clusters |
| FIREWHEEL | sandialabs/firewheel | Model-component framework and orchestration for repeatable cyber experiments |
| phēnix | sandialabs/sceptre-phenix | Experiment definition, deployment, UI, and orchestration on minimega |
| SCORCH | in sandialabs/sceptre-phenix | Scenario orchestration pipelines, breakpoints, repeatable runs, and artifact-producing experiment stages |
| Bennu / Pybennu | sandialabs/sceptre-bennu | ICS/SCADA device modeling, virtual field devices, provider interfaces, and hardware-in-the-loop integration |
| SCEPTRE topologies | sandialabs/sceptre-phenix-topologies | Executable example environments for power, wind, waterway, SCADA, and HIL experiments |
| wiretap | sandialabs/wiretap | Privilege-light WireGuard tunneling for segmented experiment networks |
| Atlas UI 3 | sandialabs/atlas-ui-3 | Governed AI agents with MCP, access control, and audit |
| TalkPipe | sandialabs/talkpipe | Streaming AI and RAG pipeline composition |
| Dakota | snl-dakota/dakota | Optimization, uncertainty quantification, and sensitivity analysis |

## SCEPTRE as an ecosystem

Current public SCEPTRE material is distributed primarily across phēnix, Bennu, SCEPTRE documentation, images, applications, and reusable topologies. A useful decomposition is:

```text
phēnix / SCORCH
experiment + campaign orchestration
        |
        v
minimega
VMs + networks + emulated environment
        |
        v
Bennu / Pybennu
virtual field devices + ICS/SCADA interfaces
        |
        v
provider boundary
        |
        v
physical or domain solver
```

This separation is important. SCEPTRE does not require one universal physical-world engine. Bennu can expose simulated process state through virtual field devices while providers connect those devices to different solvers or external systems.

Public Bennu code includes power-provider integrations and HELICS support, along with a GenericPython provider intended for lightweight discrete-time simulations. That creates a practical extension seam: a project can implement a small state model in Python without adopting a heavyweight engineering solver, while retaining SCEPTRE's experiment, network, field-device, and instrumentation layers.

## Representative experiments

The public topologies show the architecture operating as a system-of-systems test environment rather than a simple cyber range:

- **SOAP** models a SCADA-controlled power system, can integrate a physical Siemens S7 PLC as hardware-in-the-loop, includes virtual-only operation, attack paths, HMI behavior, packet capture, Zeek metadata, and SCORCH-driven experiment stages.
- **Waterway** models a notional lock system with MATLAB Simulink physics plus OPC, SCADA, historian, HMI, and engineering-workstation components.
- **Wind** models owner/operator, grid-operator, OEM, and wind-plant networks around a PowerWorld-derived grid model, with variants for Zeek, Wazuh, and SOAR experimentation.

The examples demonstrate a recurring pattern: cyber actions can alter control-system state, which alters a process model, while the surrounding network, HMI, telemetry, and evidence collection remain observable inside the experiment.

## Reuse boundary

For broader resilience research, the most reusable SCEPTRE ideas are the **physics boundary, experiment grammar, HIL abstraction, and repeatable campaign model**.

A project does not need to treat SCEPTRE as a complete human or societal world model. Instead, phēnix/minimega/Bennu can supply a lower-world execution substrate while separate models handle information availability, human behavior, accessibility burden, decisions, and outcomes.

That makes SCEPTRE particularly relevant to Accessible Information Emulytics: infrastructure and communications state can be generated or perturbed below the human layer, while a separate measurement layer evaluates what information people actually receive and can use.

## Operational caveats

Treat the published topologies as research and demonstration assets, not hardened production baselines. Some examples depend on older operating systems, licensed engineering software, or privileged networking. The phēnix container documentation also notes that the published main image defaults to UI authentication disabled unless rebuilt with authentication enabled.

Evaluate image provenance, licensing, privilege requirements, isolation, credentials, and network exposure before operational range use.
