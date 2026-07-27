import logging
import os
import shutil
from io import BytesIO

import speech_recognition as sr
from dotenv import load_dotenv
from groq import Groq
from pydub import AudioSegment

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

folder = os.path.dirname(__file__)
load_dotenv(os.path.join(folder, ".env"))

ffmpeg_path = os.environ.get("FFMPEG_PATH") or shutil.which("ffmpeg")
if not ffmpeg_path:
    raise RuntimeError(
        "ffmpeg not found. Either add ffmpeg's bin folder to your Windows PATH, "
        "or set FFMPEG_PATH in .env to the full path of ffmpeg.exe."
    )
AudioSegment.converter = ffmpeg_path


def record_audio(file_path, timeout=20, phrase_time_limit=None):
    """Record audio from the microphone and save it as an MP3 file."""
    recognizer = sr.Recognizer()

    mic_index = os.environ.get("MIC_INDEX")
    device_index = int(mic_index) if mic_index else None

    with sr.Microphone(device_index=device_index) as source:
        logging.info("Adjusting for ambient noise...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        logging.info("Start speaking now...")

        audio_data = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
        logging.info("Recording complete.")

        wav_data = audio_data.get_wav_data()
        audio_segment = AudioSegment.from_wav(BytesIO(wav_data))
        audio_segment.export(file_path, format="mp3", bitrate="128k")

        logging.info(f"Audio saved to {file_path}")


def transcribe_patient_voice(audio_filepath):
    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        raise ValueError("Missing GROQ_API_KEY in .env or environment")

    client = Groq(api_key=api_key)
    with open(audio_filepath, "rb") as audio_file:
        transcription = client.audio.transcriptions.create(
            file=audio_file,
            model=os.environ.get("WHISPER_MODEL", "whisper-large-v3"),
        )

    return transcription.text


if __name__ == "__main__":
    audio_filepath = os.path.join(folder, "patient_voice_test.mp3")

    print("Program started")
    record_audio(audio_filepath, timeout=20, phrase_time_limit=10)
    print("Recording finished")

    text = transcribe_patient_voice(audio_filepath)
    print("Transcription:")
    print(text)
