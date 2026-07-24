# Jarvis – Voice-Controlled Virtual Assistant

A Python-based voice assistant inspired by Alexa/Google Assistant. Activates on the wake word **"Jarvis"**, then listens for a command to open websites, play music, fetch live news headlines, or answer general questions using **Google Gemini**.

Built as a practice project to strengthen skills in speech processing, API integration, and modular Python design.

---

## Features

- **Voice Recognition** — Listens for and transcribes spoken commands using `speech_recognition` (Google Web Speech API).
- **Wake Word Activation** — Stays idle until it hears "Jarvis," then actively listens for a command.
- **Text-to-Speech** — Responds out loud using `pyttsx3` (offline, local TTS engine).
- **Web Browsing** — Opens Google, YouTube, Facebook, and LinkedIn on command.
- **Music Playback** — Plays songs from a local `musicLibrary` dictionary via web links.
- **Live News** — Fetches and reads out the latest headlines using [NewsAPI](https://newsapi.org).
- **AI Query Handling** — Routes any general/complex question to **Google Gemini** (`gemini-1.5-flash`) for a natural-language response.

---

## How It Works

```
Initialize Jarvis
        │
        ▼
  Listen for wake word ("Jarvis")
        │
        ▼
  Acknowledge ("Ya")
        │
        ▼
  Listen for command
        │
        ▼
  Route command ──► Open website / Play music / Fetch news / Ask Gemini
        │
        ▼
  Speak response
        │
        └──► loop back to wake word listening
```

---

## Tech Stack

| Purpose | Library / Service |
|---|---|
| Speech-to-Text | `speech_recognition` (Google Web Speech API) |
| Text-to-Speech | `pyttsx3` |
| AI Responses | Google Gemini (`google-generativeai`) |
| News Data | [NewsAPI](https://newsapi.org) |
| Web Automation | `webbrowser` (Python standard library) |
| Env Config | `python-dotenv` |

---

## Project Structure

```
jarvis-assistant/
├── jarvis.py              # Main loop — wake word detection & orchestration
├── musicLibrary.py        # Song name → link mapping
├── engine/
│   ├── __init__.py
│   ├── speak.py            # Text-to-speech (pyttsx3)
│   ├── listen.py           # Speech recognition (speech_recognition)
│   ├── command.py          # Command router (websites, music, news, fallback)
│   └── gemini_client.py    # Gemini API integration
├── requirements.txt
├── .env                     # API keys (not committed)
└── .gitignore
```

---

## Setup & Installation

### 1. Clone the repo

```bash
git clone https://github.com/muhammad-hassnain-973/jarvis-assistant.git
cd jarvis-assistant
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/Scripts/activate      # Windows (Git Bash)
# source venv/bin/activate        # macOS/Linux
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

> **Windows users:** if `pyaudio` fails to install via pip, download the matching wheel from [Gohlke's unofficial binaries](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio) and install it directly with `pip install <wheel_file>`.

### 4. Add your API keys

Create a `.env` file in the project root:

```
GEMINI_API_KEY=your_gemini_api_key
NEWSAPI_KEY=your_newsapi_key
```

- Get a Gemini key: [aistudio.google.com/apikey](https://aistudio.google.com/apikey)
- Get a NewsAPI key: [newsapi.org/register](https://newsapi.org/register)

### 5. Run it

```bash
python jarvis.py
```

Say **"Jarvis"**, wait for the acknowledgment ("Ya"), then say a command:

- *"Open Google"* / *"Open YouTube"* / *"Open Facebook"* / *"Open LinkedIn"*
- *"Play believer"*
- *"What's the news"*
- *"What's the capital of France"* → routed to Gemini
- *"Exit"* / *"Stop"* / *"Quit"* → ends the program

---

## Notes & Limitations

- Requires an active internet connection (Google STT, NewsAPI, and Gemini are all cloud-based).
- Speech recognition accuracy depends on microphone quality and background noise; short/unusual wake words like "Jarvis" are occasionally mistranscribed — the wake-word check includes common near-misses as a workaround.
- `musicLibrary.py` currently uses YouTube links as a placeholder — swap in real URLs for songs you want to test.
- NewsAPI's free tier is limited to headline data for a handful of requests per day.

---

## Possible Improvements

- Wake word detection via a dedicated offline model (e.g. Porcupine) instead of relying on general STT to catch "Jarvis."
- GUI or system tray interface instead of terminal-only.
- Persistent conversation memory for follow-up questions to Gemini.
- Expand command routing with intent classification instead of keyword matching.


---

## Author

**Muhammad Hasnain** — Final-year BS Information Technology (AI/ML) student
GitHub: [@muhammad-hassnain-973](https://github.com/muhammad-hassnain-973)