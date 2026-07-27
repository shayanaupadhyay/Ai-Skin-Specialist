# Step1: Install and import dependencies
import base64
import logging
import os
import sys
import time

from dotenv import load_dotenv
from google import genai
from groq import Groq

# Step2: Create API keys & Client

load_dotenv()

sys.stdout.reconfigure(encoding="utf-8")
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


def encode_file(filepath):
    with open(filepath, "rb") as file:
        return base64.b64encode(file.read()).decode("utf-8")


def _doctor_prompt(patient_text):
    return (
        "You are a confident, natural doctor specializing in skin care. Speak with the reassurance, clarity, and authority of a real doctor. "
        "Limit your entire response to two or three sentences maximum. "
        "Do not use any special characters, symbols, asterisks, or markdown formatting in your response because it will be converted directly to audio.\n\n"
        f"Patient text: {patient_text}"
    )


def _analyze_image_with_groq(prompt, image_filepath):
    image_data = encode_file(image_filepath)
    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
    response = client.chat.completions.create(
        model=os.environ.get("GROQ_MODEL", "qwen/qwen3.6-27b"),
        reasoning_effort="none",
        max_completion_tokens=1000,
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/png;base64,{image_data}"},
                    },
                ],
            }
        ],
    )
    return response.choices[0].message.content


def _analyze_image_with_gemini(prompt, image_filepath):
    from PIL import Image

    client = genai.Client(api_key=os.environ.get("GOOGLE_API_KEY"))
    image = Image.open(image_filepath)
    response = client.models.generate_content(
        model=os.environ.get("GEMINI_MODEL", "gemini-3.6-flash"),
        contents=[image, prompt],
    )
    return response.text


def brain_of_the_doctor(patient_text, image_filepath):
    prompt = _doctor_prompt(patient_text)
    try:
        return _analyze_image_with_groq(prompt, image_filepath)
    except Exception as exc:
        logging.warning(f"Groq analysis failed ({exc}); falling back to Gemini.")
        return _analyze_image_with_gemini(prompt, image_filepath)


def brain_of_the_doctor_video(patient_text, video_filepath):
    """Video isn't supported by Groq, so this always uses Gemini."""
    prompt = _doctor_prompt(patient_text)
    client = genai.Client(api_key=os.environ.get("GOOGLE_API_KEY"))

    video_file = client.files.upload(file=video_filepath)
    while video_file.state == "PROCESSING":
        time.sleep(2)
        video_file = client.files.get(name=video_file.name)

    if video_file.state == "FAILED":
        raise RuntimeError("Gemini failed to process the uploaded video.")

    response = client.models.generate_content(
        model=os.environ.get("GEMINI_MODEL", "gemini-3.6-flash"),
        contents=[video_file, prompt],
    )
    return response.text


if __name__ == "__main__":
    folder = os.path.dirname(__file__)
    image_path = os.path.join(folder, "sample-image.png")

    result = brain_of_the_doctor(
        patient_text="What do you see in this image?",
        image_filepath=image_path,
    )
    print(result)
