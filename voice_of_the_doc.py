import os
import platform
import subprocess
from pathlib import Path

from deepgram import DeepgramClient
from dotenv import load_dotenv

folder = os.path.dirname(__file__)
load_dotenv(os.path.join(folder, ".env"))


def text_to_speech(text, output_filepath):
    api_key = os.environ.get("DEEPGRAM_API_KEY")
    if not api_key:
        raise ValueError("Missing DEEPGRAM_API_KEY in .env or environment")

    deepgram = DeepgramClient(api_key=api_key)
    audio = deepgram.speak.v1.audio.generate(
        text=text,
        model=os.environ.get("DEEPGRAM_MODEL", "aura-2-thalia-en"),
        encoding="mp3",
    )

    audio_path = Path(output_filepath)
    with audio_path.open("wb") as file:
        for chunk in audio:
            file.write(chunk)

    return str(audio_path)


def play_audio(audio_path):
    if platform.system() == "Darwin":
        subprocess.run(["afplay", audio_path])
    elif platform.system() == "Windows":
        os.startfile(audio_path)
    else:
        subprocess.run(["xdg-open", audio_path])


if __name__ == "__main__":
    output_path = os.path.join(folder, "test-output.mp3")
    text_to_speech("Hello, my name is Shayana, who are you? I am GOOD HUMAN.", output_path)
    play_audio(output_path)
