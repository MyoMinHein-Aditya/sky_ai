# 🌤️ SKY — Your Local AI Assistant

> *"Fully local. Surprisingly smart. Runs on your machine, not someone else's cloud."*

---

## What is SKY?

SKY is a personal AI chatbot powered by **Ollama's TinyDolphin** model — running 100% on your own device. No API keys. No monthly bills. No sending your data to a server in another country. Just you, your laptop, and an AI that actually remembers what you said.

Shipped with more features than I planned. Zero regrets.

---

## ✨ Features

| Feature | Description |
|---|---|
| 💬 **Chat with memory** | SKY remembers your entire conversation — stored in a real database |
| 🌤️ **Gemini-style UI** | Clean, smooth interface with sidebar, avatars, and typing animations |
| 📎 **File upload** | Attach `.py`, `.txt`, `.csv`, `.json` and more — SKY reads and reasons about them |
| 🖼️ **Image upload** | Send a photo and ask SKY to explain, summarize, or solve it |
| 🌙 **Dark / Light mode** | Because your eyes deserve a choice |
| 📱 **Works on iPhone/iPad** | Open it on any device on the same WiFi |
| 🔒 **100% Local** | Your data never leaves your machine |
| 🕓 **Cross-device history** | Chat on your phone, continue on your laptop |

---

## 🚀 Getting Started

### Prerequisites
Make sure you have these installed:
- Python 3.10+
- [Ollama](https://ollama.ai) — for running the AI models locally

### 1. Clone the repo
```bash
git clone https://github.com/MyoMinHein-Aditya/sky_ai.git
cd sky_ai
```

### 2. Set up virtual environment
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install django djangorestframework ollama
```

### 4. Pull the AI models
```bash
# Main chat model (fast & lightweight)
ollama pull tinydolphin

# Vision model (for image understanding)
ollama pull llava
```

### 5. Run migrations
```bash
cd sky_project
python manage.py makemigrations sky_app
python manage.py migrate
```

### 6. Start the server
```bash
# Local only
python manage.py runserver

# Access from phone/tablet on same WiFi
python manage.py runserver 0.0.0.0:8000
```

### 7. Open SKY
```
http://localhost:8000
```

---

## 📱 Using SKY on iPhone / iPad

1. Connect your iPhone/iPad to the **same WiFi** as your laptop
2. Find your laptop's IP — run `ipconfig` on Windows, look for **IPv4 Address**
3. Run Django with `python manage.py runserver 0.0.0.0:8000`
4. Open Safari on your iPhone and go to `http://YOUR_IP:8000`

> **Windows users:** If it times out, open Command Prompt as Administrator and run:
> ```bash
> netsh advfirewall firewall add rule name="Django SKY" dir=in action=allow protocol=TCP localport=8000
> ```

---

## 🧠 How It Works

```
You type a message
      ↓
Django receives it → saves to SQLite DB
      ↓
Loads full conversation history from DB
      ↓
Sends everything to Ollama (TinyDolphin / LLaVA)
      ↓
AI responds → saved to DB → shown in UI
```

Every message is stored. Every session is remembered. SKY never forgets — unless you hit **Clear Chat**.

---

## 🗂️ Project Structure

```
sky_project/
├── sky_app/
│   ├── templates/sky_app/
│   │   └── index.html        # The entire frontend
│   ├── models.py             # ChatSession + ChatMessage
│   ├── views.py              # API logic + Ollama integration
│   └── urls.py               # URL routing
├── sky_project/
│   ├── settings.py
│   └── urls.py
└── manage.py
```

---

## 🛠️ Tech Stack

- **Backend** — Django + Django REST Framework
- **AI** — Ollama (TinyDolphin for text, LLaVA for vision)
- **Database** — SQLite
- **Frontend** — Vanilla HTML/CSS/JS (no frameworks, no build tools)
- **Fonts** — Plus Jakarta Sans

---

## 🎯 Built For

This project was built for a **vibe-coding hackathon** — where the goal was to build something real, useful, and impressively fast.

SKY went from zero to fully featured in one session:
- ✅ Local LLM inference
- ✅ Persistent memory
- ✅ Cross-device sync
- ✅ File + image understanding
- ✅ A UI that doesn't look like it was made in 5 minutes (it was made in more than 5 minutes)

---

## 🤝 Contributing

Got ideas? Found a bug? Feel free to open an issue or submit a pull request. SKY is always learning.

---

## 📄 License

MIT — do whatever you want with it. Just don't sell it and call it yours. ✌️

---

<div align="center">
  <strong>Made with 🌤️ and too much caffeine</strong>
</div>
