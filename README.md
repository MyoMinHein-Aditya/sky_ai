# SKY SYSTEM v1.1.0 (Local AI Terminal)

SKY is a highly responsive, terminal-style AI interface built with **Django** and powered by **Ollama**. Designed with a high-contrast aesthetic (Red modes), it provides a local, private alternative to cloud-based AI assistants.

## ⚡ Features

- **Local Execution:** Powered by Ollama (TinyDolphin) for 100% privacy and no API costs.
- **Terminal UI:** A sleek, futuristic command-line interface with custom CSS animations.
- **Real-time Feedback:** Includes "Processing" pulse animations and system status updates.
- **System Commands:** Integrated "RESET" feature to reindex memory and clear chat logs.
- **Full-Stack:** Built using Django REST Framework (DRF) for a robust backend-to-frontend link.

---

## 🛠️ Tech Stack

- **Backend:** Python, Django, Django REST Framework
- **Frontend:** HTML5, CSS3 (Custom Variables), JavaScript (Fetch API)
- **AI Engine:** Ollama (Model: `tinydolphin`)
- **Environment:** Dotenv for modular configuration

---

## 👨‍💻 About the Developer
Currently pursuing a technical curriculum with a focus on Python Full-Stack Development and local AI integration. SKY is a project born out of a desire to create a private, high-performance executive assistant that runs entirely on local hardware.

## 📋 Commands & Usage
- **Type a message:** Enter any prompt into the terminal and hit `EXECUTE`.
- **RESET:** Clears the current session and re-initializes the system interface.
- **Theme Shift:** (Developer Mode) Edit `:root` variables in `style.css` to toggle between Gold, Red, and Deep Sea modes.

---
*Created with focus and caffeine. System Status: Optimized.*

## 🚀 Installation & Setup

### 1. Prerequisites
Ensure you have **Ollama** installed on your machine.
```bash
# Pull the lightweight model for maximum speed
ollama pull tinydolphin
