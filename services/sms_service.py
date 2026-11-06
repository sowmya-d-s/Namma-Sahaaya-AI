# services/sms_service.py

def explain_sms(message):

    msg = message.lower()

    if "kyc" in msg:
        return """
        ನಿಮ್ಮ ಬ್ಯಾಂಕ್ ಖಾತೆಯ
        ದೃಢೀಕರಣ ಪ್ರಕ್ರಿಯೆ ಬಾಕಿಯಿದೆ.
        """

    elif "otp" in msg:
        return """
        ಇದು ನಿಮ್ಮ ದೃಢೀಕರಣ ಕೋಡ್.
        ಇದನ್ನು ಯಾರ ಜೊತೆಯೂ ಹಂಚಿಕೊಳ್ಳಬೇಡಿ.
        """

    elif "credited" in msg:
        return """
        ನಿಮ್ಮ ಖಾತೆಗೆ ಹಣ ಜಮಾ ಆಗಿದೆ.
        """

    elif "debited" in msg:
        return """
        ನಿಮ್ಮ ಖಾತೆಯಿಂದ ಹಣ ಕಡಿತಗೊಂಡಿದೆ.
        """

    else:
        return """
        ಈ ಸಂದೇಶದ ಸರಳ ವಿವರಣೆ ಲಭ್ಯವಿಲ್ಲ.
        """