# AI Skin Specialist

An AI-powered skin consultation assistant. Describe a skin concern by voice, upload a photo or a short video, and get a spoken response from an AI "doctor" persona with preliminary guidance.

> **Disclaimer:** This is not a real medical diagnosis. Always consult a licensed doctor for persistent or severe symptoms.

## How it works

1. **Voice input** - you record (or upload) a short description of your concern.
2. **Transcription** - the recording is transcribed to text with Groq's Whisper model.
3. **Analysis** - a vision-capable LLM looks at your photo or video alongside the transcript and responds in character as a doctor:
   - Photo → analyzed with Groq (`qwen/qwen3.6-27b`), falling back to Gemini automatically if Groq errors.
   - Video → analyzed with Gemini (`gemini-3.6-flash`), since Groq doesn't support video input.
4. **Voice reply** - the doctor's text response is converted to speech with Deepgram and played back.

All of this runs through a Gradio web UI (`main.py`).

## Tech stack

| Purpose | Provider | Notes |
|---|---|---|
| Speech-to-text | [Groq](https://console.groq.com) (Whisper) | Free tier |
| Image + text analysis | [Groq](https://console.groq.com) (Qwen 3.6) | Free tier |
| Video + text analysis | [Google Gemini](https://aistudio.google.com) | Free tier (Flash model) |
| Text-to-speech | [Deepgram](https://deepgram.com) | |
| UI | [Gradio](https://gradio.app) | |

## Setup

**Requirements:** Python 3.13+, [uv](https://docs.astral.sh/uv/), [ffmpeg](https://ffmpeg.org/) on your PATH (or set `FFMPEG_PATH` below).

1. Install dependencies:
   ```bash
   uv sync
   ```
2. Create a `.env` file in the project root with your API keys:
   ```bash
   GROQ_API_KEY=your_groq_key
   GOOGLE_API_KEY=your_gemini_key
   DEEPGRAM_API_KEY=your_deepgram_key

   # Optional overrides
   FFMPEG_PATH=C:\path\to\ffmpeg.exe   # only if ffmpeg isn't on your PATH
   MIC_INDEX=1                         # only if the wrong microphone is picked up by default
   ```
3. Run the app:
   ```bash
   uv run python main.py
   ```
   Open the URL printed in the terminal.

## Project structure

| File | Purpose |
|---|---|
| `main.py` | Gradio web app tying the full pipeline together |
| `brain_of_the_doc.py` | Image/video analysis + doctor persona (Groq + Gemini) |
| `voice_of_the_patient.py` | Microphone recording + speech-to-text |
| `voice_of_the_doc.py` | Text-to-speech for the doctor's reply |
| `list_microphones.py` | Lists available input devices (for setting `MIC_INDEX`) |
