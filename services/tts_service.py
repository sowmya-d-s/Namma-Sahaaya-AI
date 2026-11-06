import requests
import os

API_KEY = os.getenv("GNANI_API_KEY")


def text_to_speech(text):

    response = requests.post(
        "https://api.vachana.ai/api/v1/tts/inference",

        headers={
            "Content-Type": "application/json",
            "X-API-Key-ID": API_KEY
        },

        json={
            "text": text,
            "voice": "Shivani",
            "model": "timbre-v3.0",
            "language": "kn-IN",
            "speed": 1.0,

            "audio_config": {
                "sample_rate": 48000,
                "num_channels": 1,
                "sample_width": 2,
                "encoding": "linear_pcm",
                "container": "wav"
            }
        }
    )

    # DEBUG CODE HERE
    print("Status:", response.status_code)
    print("Content-Type:", response.headers.get("content-type"))

    if response.status_code == 200:
        with open("static/response.wav", "wb") as f:
            f.write(response.content)

        print("Audio saved successfully")

    else:
        print(response.text)

    return "response.wav"