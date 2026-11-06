from flask import Flask, render_template, request
from services.stt_service import transcribe_audio
from services.llm_service import get_ai_answer
from services.tts_service import text_to_speech
from services.sms_service import explain_sms
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/process", methods=["POST"])
def process():

    if "audio" not in request.files:
        return render_template(
            "index.html",
            answer="Please upload an audio file."
        )

    audio = request.files["audio"]

    if audio.filename == "":
        return render_template(
            "index.html",
            answer="Please select an audio file."
        )

    os.makedirs("uploads", exist_ok=True)

    audio_path = os.path.join(
        "uploads",
        audio.filename
    )

    audio.save(audio_path)

    transcript = transcribe_audio(audio_path)

    answer = get_ai_answer(transcript)

    text_to_speech(answer)

    return render_template(
        "index.html",
        transcript=transcript,
        answer=answer
    )


@app.route("/sms", methods=["POST"])
def sms():

    sms_text = request.form.get("sms", "")

    if not sms_text.strip():
        return render_template(
            "index.html",
            sms_answer="Please enter a message."
        )

    answer = explain_sms(sms_text)

    return render_template(
        "index.html",
        sms_answer=answer
    )


if __name__ == "__main__":
    app.run(debug=True)