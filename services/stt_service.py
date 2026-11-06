import requests

API_KEY = "YOUR_API_KEY"
def transcribe_audio(audio_path):

    with open(audio_path, "rb") as f:

        response = requests.post(
            "https://api.vachana.ai/stt/v3",

            headers={
                "X-API-Key-ID": API_KEY
            },

            files={
                "audio_file": (audio_path, f)
            },

            data={
                "model": "prisma-v3.0",
                "language_code": "kn-IN",
                "format": "transcribe"
            },

            timeout=60
        )

    result = response.json()

    return result["transcript"]