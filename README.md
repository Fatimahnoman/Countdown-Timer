# ⏳ Countdown Timer

A beautiful and interactive Countdown Timer available in two versions — **Streamlit Web App** and **Terminal CLI**.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-red?logo=streamlit)
![License](https://img.shields.io/badge/License-MIT-green)

---

## ✨ Features

- ⏱️ Set countdown with **Minutes & Seconds**
- 🎨 Modern UI with custom CSS styling (Web version)
- 🔄 Real-time visual countdown with large display
- 🎈 Balloons animation when timer finishes (Web version)
- 🛑 Stop timer anytime
- ⏰ Hours support for long durations (CLI version)
- 📱 Fully responsive web interface

---

## 📂 Project Structure

```
Countdown-Timer/
├── app.py              # Streamlit Web App (main version)
├── timer_cli.py        # Terminal CLI version
├── requirements.txt    # Python dependencies
└── README.md           # Documentation
```

---

## 🚀 How to Run

### Option 1: Streamlit Web Version (Recommended)

```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

Opens in your browser at `http://localhost:8501`

### Option 2: Terminal / CLI Version

```bash
# No extra dependencies needed
python timer_cli.py
```

Works in any terminal — Windows, macOS, or Linux.

---

## 🎮 How to Use

### Web Version
1. Enter **minutes** and **seconds** using the input fields
2. Click the **🚀 Start Countdown** button
3. Watch the timer count down in real-time
4. When it reaches **00:00**, balloons will appear with a "Time's Up!" message
5. Click **🛑 Stop Timer** to cancel anytime

### CLI Version
1. Enter **minutes** and **seconds** when prompted
2. The timer displays a clean countdown in your terminal
3. Press **Ctrl+C** to stop the timer early

---

## 🛠️ Technologies Used

| Technology | Purpose |
|-----------|---------|
| Python 3 | Core language |
| Streamlit | Web framework for the UI |
| HTML/CSS | Custom styling for timer display |

---

## 📋 Requirements

- Python 3.7+
- Streamlit (`pip install streamlit`)

---

## 👩‍💻 Author

**Fatimah Noman**

Python Learner 🚀 | Exploring Agentic AI 🤖

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
