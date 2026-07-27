import os

import gradio as gr

from brain_of_the_doc import brain_of_the_doctor, brain_of_the_doctor_video
from voice_of_the_doc import text_to_speech
from voice_of_the_patient import transcribe_patient_voice

folder = os.path.dirname(__file__)
doctor_reply_path = os.path.join(folder, "doctor_reply.mp3")


def run_pipeline(image_path, video_path, audio_path):
    if not video_path and not image_path:
        raise gr.Error("Please upload a photo or a video of the skin concern.")
    if not audio_path:
        raise gr.Error("Please record a voice message describing the concern.")

    patient_text = transcribe_patient_voice(audio_path)

    if video_path:
        doctor_text = brain_of_the_doctor_video(patient_text, video_path)
    else:
        doctor_text = brain_of_the_doctor(patient_text, image_path)

    audio_reply = text_to_speech(doctor_text, doctor_reply_path)

    return patient_text, doctor_text, audio_reply


def reveal_results():
    return gr.update(visible=False), gr.update(visible=True)


HEAD_HTML = """
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=swap" rel="stylesheet">
"""

CUSTOM_CSS = """
.gradio-container {
    background: #f9f9ff !important;
    font-family: 'Inter', sans-serif !important;
}

.material-symbols-outlined {
    font-family: 'Material Symbols Outlined';
    font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24;
    vertical-align: middle;
}

#app-header {
    display: flex;
    flex-direction: column;
    padding: 8px 0 20px 0;
    border-bottom: 1px solid #c3c6d7;
    margin-bottom: 16px;
}
#app-header h1 {
    color: #004ac6 !important;
    font-weight: 700 !important;
    margin: 0 !important;
}
#app-header p {
    color: #434655 !important;
    font-size: 12px !important;
    margin: 0 !important;
}

.card {
    background: #ffffff !important;
    border: 1px solid #c3c6d7 !important;
    border-radius: 24px !important;
    padding: 24px !important;
    box-shadow: 0px 4px 20px rgba(26, 43, 75, 0.05), 0px 10px 40px rgba(26, 43, 75, 0.03) !important;
}
.doctor-card {
    position: sticky !important;
    top: 24px !important;
}

.section-header {
    display: flex;
    align-items: center;
    gap: 12px;
    margin-bottom: 16px;
}
.section-header .icon-badge {
    width: 40px;
    height: 40px;
    border-radius: 999px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 22px;
    flex-shrink: 0;
}
.section-header.patient .icon-badge {
    background: rgba(13, 148, 136, 0.1);
    color: #0D9488;
}
.section-header.doctor .icon-badge {
    background: rgba(0, 106, 97, 0.1);
    color: #006a61;
}
.section-header h2 {
    color: #081b3a !important;
    font-size: 20px !important;
    font-weight: 600 !important;
    margin: 0 !important;
}

#analyze-btn {
    background: #004ac6 !important;
    color: #fff !important;
    border-radius: 12px !important;
    font-weight: 600 !important;
    padding: 14px !important;
    border: none !important;
    box-shadow: 0 4px 12px rgba(0, 74, 198, 0.25) !important;
}
#analyze-btn:hover {
    filter: brightness(1.1);
}

/* Upload dropzones (image + video) */
.upload-container {
    border: 2px dashed #c3c6d7 !important;
    border-radius: 12px !important;
    background: #f1f3ff !important;
    transition: border-color 0.15s ease, background 0.15s ease;
}
.upload-container:hover {
    border-color: #004ac6 !important;
    background: #e9edff !important;
}

/* Idle mic record button */
button.record-button {
    background: #004ac6 !important;
    color: #fff !important;
    border: none !important;
    border-radius: 999px !important;
    font-weight: 600 !important;
}
button.record-button:hover {
    filter: brightness(1.1);
}

#transcript-box textarea {
    font-style: italic;
    color: #434655 !important;
    background: #f9f9ff !important;
    border-radius: 12px !important;
}

#guidance-box textarea {
    background: #f1f3ff !important;
    color: #081b3a !important;
    border-radius: 12px !important;
}

.helper-note {
    display: flex;
    align-items: flex-start;
    gap: 8px;
    background: #f1f3ff;
    border-radius: 12px;
    padding: 16px;
    color: #434655;
    font-size: 12px;
    margin-top: 8px;
}

.empty-state {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    padding: 48px 24px;
}
.empty-state .icon-circle {
    width: 80px;
    height: 80px;
    border-radius: 999px;
    background: #e0e8ff;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #737686;
    font-size: 40px;
    margin-bottom: 24px;
}
.empty-state h3 {
    color: #081b3a;
    font-size: 20px;
    font-weight: 600;
    margin: 0 0 8px 0;
}
.empty-state p {
    color: #434655;
    font-size: 14px;
    margin: 0;
    max-width: 320px;
}
"""

EMPTY_STATE_HTML = """
<div class="empty-state">
    <div class="icon-circle"><span class="material-symbols-outlined" style="font-size: 48px;">clinical_notes</span></div>
    <h3>Ready for Analysis</h3>
    <p>Your consultation summary will appear here after analysis. Record your concern and upload an image or video to begin.</p>
</div>
"""


with gr.Blocks(title="AI Skin Specialist") as demo:
    gr.HTML(
        """
        <div id="app-header">
            <h1>AI Skin Specialist</h1>
            <p>Voice, image, and video based skin consultation assistant</p>
        </div>
        """
    )

    with gr.Row():
        with gr.Column(elem_classes=["card"]):
            gr.HTML(
                """
                <div class="section-header patient">
                    <div class="icon-badge"><span class="material-symbols-outlined">person</span></div>
                    <h2>Patient Input</h2>
                </div>
                """
            )
            audio_input = gr.Audio(
                sources=["microphone", "upload"],
                type="filepath",
                label="Describe your skin concern",
            )
            image_input = gr.Image(
                type="filepath", label="Skin photo (used if no video is provided)"
            )
            video_input = gr.Video(
                label="Skin video (optional, takes priority over the photo)"
            )
            gr.HTML(
                """
                <div class="helper-note">
                    <span class="material-symbols-outlined" style="color:#004ac6;font-size:20px;">videocam</span>
                    <span>For better assessment, include a short video showing the affected area.
                    This helps the AI understand the texture and relief of the skin concern.</span>
                </div>
                """
            )
            analyze_btn = gr.Button("Start AI Analysis", elem_id="analyze-btn")

        with gr.Column(elem_classes=["card", "doctor-card"]):
            gr.HTML(
                """
                <div class="section-header doctor">
                    <div class="icon-badge"><span class="material-symbols-outlined">psychology</span></div>
                    <h2>Doctor Response</h2>
                </div>
                """
            )
            empty_state = gr.HTML(EMPTY_STATE_HTML)
            with gr.Group(visible=False) as results_group:
                transcript_output = gr.Textbox(
                    label="Your speech", elem_id="transcript-box", interactive=False, lines=3
                )
                guidance_output = gr.Textbox(
                    label="Doctor's guidance", elem_id="guidance-box", interactive=False, lines=6
                )
                audio_output = gr.Audio(label="Doctor's voice reply", autoplay=True)

    analyze_btn.click(
        fn=run_pipeline,
        inputs=[image_input, video_input, audio_input],
        outputs=[transcript_output, guidance_output, audio_output],
    ).then(
        fn=reveal_results,
        outputs=[empty_state, results_group],
    )


if __name__ == "__main__":
    port = os.environ.get("PORT")
    demo.launch(server_port=int(port) if port else None, css=CUSTOM_CSS, head=HEAD_HTML)
