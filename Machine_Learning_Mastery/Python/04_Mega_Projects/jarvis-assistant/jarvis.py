from dotenv import load_dotenv
load_dotenv()

from engine.speak import speak
from engine.listen import listen
from engine.command import process_command

# Google STT often mishears "Jarvis" — cover common variants
WAKE_WORDS = ["jarvis", "travis", "service", "jarvi", "java this"]
EXIT_WORDS = ["exit", "stop", "quit", "goodbye"]


def main():
    speak("Initializing Jarvis....")

    while True:
        text = listen()
        print(f"[DEBUG] Heard: '{text}'")

        if not text:
            continue

        if any(w in text for w in WAKE_WORDS):
            speak("Ya")
            command_text = listen()
            print(f"[DEBUG] Command heard: '{command_text}'")

            if not command_text:
                speak("Sorry, I didn't catch that.")
                continue

            if any(w in command_text for w in EXIT_WORDS):
                speak("Goodbye!")
                break

            response = process_command(command_text)

            if response:
                speak(response)


if __name__ == "__main__":
    main()