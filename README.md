# Raw Industrial Protocols Lab

This repository contains the blueprints, low-level execution steps, and serialization matrices for deploying an isolated, bare-metal Industrial Control Systems (ICS) and Operational Technology (OT) protocol analysis environment.

By stripping away heavy vendor software and abstraction layers, this lab utilizes lightweight Python socket twins running on a local loopback interface to replicate, capture, and dissect the exact binary handshakes used by major industrial controllers.

## 🚀 Getting Started

If you want the complete, deep-dive architectural analysis, byte-by-byte hex mappings, and structural telemetry, go straight to the master manual:

👉 **[Read the Complete Reference Manual (NOTES.md)](https://github.com/404saint/raw-industrial-protocols/blob/main/NOTES.md)**

To view, modify, or execute the raw socket manipulation and injection templates used across the lab blocks, browse the source code directory:

👉 **[Browse the Script Templates (/scripts)](https://github.com/404saint/raw-industrial-protocols/tree/main/scripts)**
Here is the complete `README.md` for **`raw-industrial-protocols`**. It has been structured to perfectly mirror the formatting, tone, and high-signal layout of your GNS3 lab documentation.

---

---

## Lab Architecture

The testing environment relies on host-isolated loopback interfaces to establish low-overhead socket connections. This layout allows for safe, hardware-less transport analysis without flooding physical subnets.

* **Analysis Host:** Ubuntu / EndeavourOS Linux workstation running `tshark`
* **Transport Drivers:** Custom Python socket twins handling raw binary streams
* **Network Boundary:** Localhost interface loopback (`lo`)
* **Isolators:** Strict Berkeley Packet Filters (BPF) to strip host-process noise

### Handshake Execution Flow

```text
  [ Client Application ]                          [ Target / PLC Emulator ]
            │                                                 │
            │ ─── Step 1: Standard TCP 3-Way Handshake ─────> │
            │ <── [SYN], [SYN-ACK], [ACK] ─────────────────── │
            │                                                 │
            │ ─── Step 2: Protocol Transport Negotiation ───> │
            │     (e.g., S7Comm TPKT/COTP or OPC UA HEL)      │
            │                                                 │
            │ <── Step 3: Transport Acknowledge / Verify ───> │
            │                                                 │
            ▼                                                 ▼
     [ Socket Opened ]                                 [ Session Active ]

```

## Repository Structure

```text
├── README.md       - Core project overview, matrix, and navigation map.
├── NOTES.md        - Deep-dive technical manual and structural hex breakdowns.
├── scripts/        - Isolated client/server handshake injection engines.
└── assets/         - Diagnostic assets, terminal screenshots, and raw PCAP captures.

```

## Protocol Target Matrix

| Protocol | Evaluation Mode | Default Port |
| :--- | :--- | :--- |
| **Modbus/TCP** | Register Polling / MBAP Framing | `502` |
| **DNP3** | EPA Stack / Link Status Queries | `20000` |
| **EtherNet/IP** | Session Registration Tracking | `44818` |
| **S7Comm** | Nested ISO-TSAP Negotiations | `102` |
| **OPC UA** | Native Binary Plaintext Backdoors | `4840` |
---

## 👨‍💻 Author

Developed and maintained by **RUGERO Tesla (404saint)**. Feel free to open issues or contribute updates if you uncover alignment anomalies in new protocol environments!
