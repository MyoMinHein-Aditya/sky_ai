## Security Policy for SKY

Since **SKY** is built on the principle of **100% local execution**, our security philosophy is simple: **Your data never leaves your machine.** However, maintaining a secure environment for local AI requires specific practices.

---

### Our Security Philosophy

> **Local-First, Privacy-Always:** SKY does not use external APIs, tracking cookies, or remote telemetry. The "Security Perimeter" is defined by your own hardware and local network.

---

### Supported Versions

We actively provide security updates for the following versions:

| Version | Supported |
| --- | --- |
| **v1.2.x** | ✅ Active Support |
| **v1.1.x** | ⚠️ Security Fixes Only |
| **< v1.0.0** | ❌ End of Life |

---

### Reporting a Vulnerability

If you discover a security hole—such as a flaw in how the **Django REST API** handles local requests or a potential code injection point—please do not open a public issue.

1. **Email us:** Send a detailed report to `aditya.bajoria0208@gmail.com`.
2. **Details to include:** * A description of the vulnerability.
* Steps to reproduce the issue.
* The version of **Ollama** and **Python** you are running.


3. **Response Time:** We aim to acknowledge all reports within **48 hours** and provide a fix or mitigation strategy within **7 days**.

---

### Security Best Practices for Users

While SKY is designed to be private, we recommend the following to keep your local instance secure:

* **Keep Ollama Updated:** Ensure you are running the latest version of the Ollama backend to benefit from their internal security patches.
* **Localhost Only:** By default, the Django server should only bind to `127.0.0.1`. Do not expose your local SKY port to the public internet unless using a secure VPN or tunnel.
* **Environment Variables:** Never hardcode sensitive paths or configurations in the source code. Use a `.env` file (which is excluded via `.gitignore`).
* **Python Version:** Run SKY using **Python 3.14+** to ensure you have the latest core security improvements.

---

### What We Do Not Collect

To be absolutely clear, the following data is **never** collected or transmitted by SKY:

* Your chat history or prompts.
* Model weights or configurations.
* System metadata or IP addresses.
* Personal identifiers.
