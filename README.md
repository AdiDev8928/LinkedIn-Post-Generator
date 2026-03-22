# 📝 LinkedIn Post Generator

A lightweight web application built with **Streamlit** that leverages the power of **Generative AI** to craft engaging, professional LinkedIn posts in seconds.

Simply provide a topic, select your preferred tone and post length — and let the AI do the writing for you.

---

## ✨ Features

- 🤖 **Real AI Generation** — Connects to Google's **Gemini 2.5 Flash** model for high-quality content
- 🎯 **Topic-based Post Generation** — Enter any topic and get a publish-ready LinkedIn post
- 🎨 **Customizable Tone** — Professional, Casual, Inspirational, and more
- 📏 **Control Over Post Length** — Short, medium, or long-form content
- 🔐 **Sidebar API Key Input** — Securely enter your Gemini API key without hardcoding it
- ⚙️ **Prompt Engineering** — Sophisticated prompt building combining topic, tone, length, and options
- 🖥️ **Modern UI** — Custom CSS for a polished, LinkedIn-inspired blue aesthetic
- ⚡ **Quick Copy** — Dedicated code block for easy copying of the generated post

---

## 🛠️ Built With

- [Streamlit](https://streamlit.io/) — UI framework
- [Google Gemini API](https://aistudio.google.com/) — Language model backend (`gemini-2.5-flash`)
- `google-generativeai` — Official Python SDK for Gemini

---

## 📂 Project Structure

```
linkedin-post-generator/
├── app.py               # Main Streamlit application & LLM logic
└── requirements.txt     # Project dependencies
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/linkedin-post-generator.git
cd linkedin-post-generator
```

### 2. Set Up a Virtual Environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the App

```bash
streamlit run app.py
```

> Your browser will automatically open to `http://localhost:8501`

### 5. Add Your API Key

In the app's **sidebar**, enter your [Google Gemini API Key](https://aistudio.google.com/app/apikey) — no hardcoding required.

---

## 📦 Requirements

```
streamlit
google-generativeai
```

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to open a pull request or raise an issue.

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
