import webbrowser
import os
import requests
from musicLibrary import music

NEWSAPI_KEY = os.getenv("NEWSAPI_KEY")


def process_command(command):
    command = command.lower().strip()

    if "open google" in command:
        webbrowser.open("https://google.com")
        return "Opening Google"

    elif "open facebook" in command:
        webbrowser.open("https://facebook.com")
        return "Opening Facebook"

    elif "open youtube" in command:
        webbrowser.open("https://youtube.com")
        return "Opening YouTube"

    elif "open linkedin" in command:
        webbrowser.open("https://linkedin.com")
        return "Opening LinkedIn"
    
    elif "open my linkedin" in command:
        webbrowser.open("https://www.linkedin.com/in/muhammadhassnain973/")
        return "Opening Your LinkedIn"

    elif command.startswith("play"):
        parts = command.split(" ", 1)
        song = parts[1].strip() if len(parts) > 1 else ""
        if song in music:
            webbrowser.open(music[song])
            return f"Playing {song}"
        else:
            return f"Sorry, I don't have {song} in the music library"

    elif "news" in command:
        return fetch_news()

    else:
        from engine.gemini_client import ask_gemini
        return ask_gemini(command)


def fetch_news():
    if not NEWSAPI_KEY:
        return "News API key is missing."

    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWSAPI_KEY}"
    try:
        response = requests.get(url, timeout=10)
        data = response.json()
        articles = data.get("articles", [])[:5]

        if not articles:
            return "No news found right now."

        headlines = [article["title"] for article in articles if article.get("title")]
        return "Here are the top headlines: " + ". ".join(headlines)
    except requests.RequestException:
        return "Sorry, I couldn't fetch the news right now."