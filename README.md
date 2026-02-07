# DevOps Chaos Engineering Toolkit

[![Python 3.11](https://img.shields.io/badge/Python-3.11-3776AB.svg)](https://www.python.org/)
[![Resilience](https://img.shields.io/badge/Practice-Chaos-red.svg)](https://principlesofchaos.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A **production-grade chaos engineering toolkit** for resilience testing. This repository provides a Python agent capable of injecting controlled faults into a system, including CPU stress, memory consumption, and network latency simulation.

## 🚀 Features

- **CPU Stressor**: Simulates high CPU load to test autoscaling triggers.
- **Memory Gremlin**: Consumes RAM to test OOM (Out of Memory) handling.
- **Network Lag**: Simulates artificial latency (mock implementation for cross-platform safety).
- **Disk Filler**: Writes temporary files to test disk space alerts.
- **Scheduler**: Timed injection of faults.

## 📁 Project Structure

```
devops-chaos-engineering-toolkit/
├── src/
│   ├── chaos_agent.py    # Fault injection logic
│   └── main.py           # CLI Entrypoint
├── requirements.txt
└── Dockerfile
```

## 🛠️ Quick Start

```bash
# Clone
git clone https://github.com/Shivay00001/devops-chaos-engineering-toolkit.git

# Install
pip install -r requirements.txt

# Run Chaos (CPU Stress for 10s)
python src/main.py --fault cpu --duration 10
```

## 📄 License

MIT License
