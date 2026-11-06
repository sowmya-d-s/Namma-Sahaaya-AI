def get_ai_answer(question):

    question = question.lower()

    if "upi" in question:
        return """
        UPI PIN ನಿಮ್ಮ ಡಿಜಿಟಲ್ ಪಾವತಿಗಳನ್ನು
        ಸುರಕ್ಷಿತಗೊಳಿಸುವ ರಹಸ್ಯ ಸಂಖ್ಯೆ.
        """

    elif "kyc" in question:
        return """
        KYC ನಿಮ್ಮ ಬ್ಯಾಂಕ್ ಖಾತೆಯ ಗುರುತಿನ
        ವಿವರಗಳನ್ನು ದೃಢೀಕರಿಸುವ ಪ್ರಕ್ರಿಯೆ.
        """

    elif "wifi" in question:
        return """
        ಸೆಟ್ಟಿಂಗ್ಸ್ ತೆರೆಯಿರಿ ಮತ್ತು ವೈಫೈ
        ಆಯ್ಕೆಯನ್ನು ಆನ್ ಮಾಡಿ.
        """

    elif "bluetooth" in question:
        return """
        ಸೆಟ್ಟಿಂಗ್ಸ್ ತೆರೆಯಿರಿ ಮತ್ತು
        ಬ್ಲೂಟೂತ್ ಆಯ್ಕೆಯನ್ನು ಆನ್ ಮಾಡಿ.
        """

    elif "otp" in question:
        return """
        OTP ಒಂದು ಸುರಕ್ಷತಾ ಕೋಡ್ ಆಗಿದ್ದು
        ನಿಮ್ಮ ಗುರುತನ್ನು ದೃಢೀಕರಿಸಲು ಬಳಸಲಾಗುತ್ತದೆ.
        """

    elif "bank" in question or "ಬ್ಯಾಂಕ್" in question:
        return """
        ಇದು ಬ್ಯಾಂಕಿಂಗ್ ಸಂಬಂಧಿತ ಮಾಹಿತಿ.
        """

    elif "ಹೆಸರು" in question:
        return """
        ನಿಮ್ಮ ಹೆಸರು ಸೌಮ್ಯ ಎಂದು ಕೇಳಿಸುತ್ತಿದೆ.
        """

    else:
        return """
        ನಿಮ್ಮ ಪ್ರಶ್ನೆಯನ್ನು ಅರ್ಥ ಮಾಡಿಕೊಂಡಿದ್ದೇನೆ.
        """