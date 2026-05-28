# 🎯 AI Interview Coach

> Practice interviews with AI-powered feedback. Get detailed scores, improvement tips, and a full performance report — all powered by Groq LLaMA 3.3 70B.

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=flat-square&logo=fastapi)
![Python](https://img.shields.io/badge/Python-3.11-blue?style=flat-square)
![LangChain](https://img.shields.io/badge/LangChain-latest-green?style=flat-square)
![Groq](https://img.shields.io/badge/Groq-LLaMA3.3-orange?style=flat-square)
![Render](https://img.shields.io/badge/Deployed-Render-purple?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-pink?style=flat-square)

---

## 🔗 Live Demo
👉 **[Try AI Interview Coach](https://ai-interview-coach-pzp4.onrender.com/)**

> ⚠️ First load may take ~50 seconds (free tier cold start). After that it's fast!

---

## 📌 What is AI Interview Coach?

A full-stack AI application that simulates real job interviews and gives you honest, detailed feedback on every answer — just like a real interviewer would.

**Perfect for:**
- Students preparing for campus placements
- Anyone practicing for ML / SDE / Data Science interviews
- People who want honest feedback before the real thing

---

## ✨ Features

- 🎤 **Role-specific questions** — Technical, Behavioral, HR, System Design
- 🎯 **Difficulty levels** — Entry Level, Mid Level, Senior Level
- 🧠 **AI feedback on every answer** — Score out of 10, what you did well, what to improve, ideal answer
- 📊 **Full performance report** — Overall score, top strengths, areas to improve, recommendation
- 📈 **Session tracking** — Daily goal progress
- 🌙 **Beautiful dark UI** — Professional dashboard design

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | FastAPI (Python) |
| AI / LLM | Groq API — LLaMA 3.3 70B |
| Orchestration | LangChain |
| Frontend | Pure HTML / CSS / JavaScript |
| Deployment | Render.com |

---

## ⚙️ How It Works

```
User enters role + difficulty + focus areas
    → LangChain + Groq generates role-specific questions
        → User answers each question
            → AI analyzes answer and gives Score + Feedback
                → Full performance report generated at end
```

---

## 🚀 Run Locally

### 1. Clone the repo
```bash
git clone https://github.com/PhaniHarika/ai-interview-coach.git
cd ai-interview-coach
```

### 2. Create virtual environment
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up environment variables
Create a `.env` file:
```
GROQ_API_KEY=your_groq_api_key_here
```

Get your free Groq API key at: https://console.groq.com

### 5. Run the app
```bash
python main.py
```

Open **http://localhost:8000** 🎉

---

## 📁 Project Structure

```
ai-interview-coach/
├── main.py              ← FastAPI backend + API routes
├── interview_engine.py  ← AI logic (questions, feedback, summary)
├── templates/
│   └── index.html       ← Full frontend (HTML/CSS/JS)
├── static/              ← Static assets
├── requirements.txt
├── .env                 ← API keys (not committed)
└── .gitignore
```

---

## 🔑 Key Design Decisions

- **Groq over OpenAI** — Free tier, 3x faster inference, LLaMA 3.3 70B is highly capable
- **FastAPI over Flask** — Async support, automatic API docs, cleaner code
- **Pure HTML/CSS/JS** — No framework needed, full control over UI, fast load time
- **Role + difficulty aware prompts** — Questions adapt to the specific role and level

---

## 📸 Screenshots

### Home Dashboard
![Home](https://github.com/PhaniHarika/ai-interview-coach/raw/main/screenshots/home.png)

### Interview Question
![Question](https://github.com/PhaniHarika/ai-interview-coach/raw/main/screenshots/question.png)

### AI Feedback
![Feedback](https://github.com/PhaniHarika/ai-interview-coach/raw/main/screenshots/feedback.png)

### Performance Report
![Report](https://github.com/PhaniHarika/ai-interview-coach/raw/main/screenshots/report.png)

---

## 🌱 Future Enhancements

- [ ] Voice input support (speak your answers)
- [ ] Track progress across sessions with charts
- [ ] Download performance report as PDF
- [ ] Company-specific interview modes (Google, Amazon, startup)
- [ ] Leaderboard for competitive practice

---

## 👩‍💻 Author

**Phani Harika Soma**
- 🔗 GitHub: [@PhaniHarika](https://github.com/PhaniHarika)
- 💼 LinkedIn: [phaniharikasoma](https://www.linkedin.com/in/phaniharikasoma)
- 📧 phaniharikasoma@gmail.com

---

## 📄 License

MIT License — feel free to use, modify and build on this!

---

⭐ **If this helped you, give it a star!** It motivates me to keep building 🚀
