# Devops Chaos Engineering Toolkit

Chaos engineering toolkit: Python agents, C++ core, Docker, CI/CD.

![Language](https://img.shields.io/badge/Language-HTML-blue)
![Status](https://img.shields.io/badge/Status-Active-success)
![License](https://img.shields.io/badge/License-MIT-green)

## 🚀 Overview

Welcome to the **Devops Chaos Engineering Toolkit** repository. This project is built to deliver a robust and scalable solution tailored to modern development standards.

## ✨ Features

- **High Performance:** Optimized for speed and efficiency.
- **Scalable Architecture:** Designed to grow with your needs.
- **Clean Codebase:** Follows best practices and industry standards.
- **Secure by Default:** Engineered with security in mind.

## 🛠️ Prerequisites

Ensure you have the following installed in your environment before proceeding:
- Appropriate runtime/compiler for `HTML`
- Standard development tools

## 📦 Installation

Follow standard installation steps for `HTML` to set up the project locally:

1. Clone the repository:
   ```bash
   git clone https://github.com/Shivay00001/devops-chaos-engineering-toolkit.git
   ```
2. Navigate to the project directory:
   ```bash
   cd devops-chaos-engineering-toolkit
   ```
3. Install dependencies according to the standard `HTML` ecosystem.

## 💻 Usage

```bash
# Install dependencies
pip install -r requirements.txt

# Inject faults
python src/main.py --fault cpu --duration 10 --param 2        # stress 2 CPU cores
python src/main.py --fault memory --duration 10 --param 500   # consume 500 MB RAM
python src/main.py --fault latency --duration 10 --param 200  # simulate 200 ms lag
python src/main.py --fault disk --duration 10 --param 100     # write 100 MB mock files

# Docker
docker build -t chaos-toolkit .
docker run --rm chaos-toolkit --fault cpu --duration 5
```

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

## 📝 License

This project is licensed under standard terms.
