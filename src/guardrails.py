import re

class Guardrails:
    def __init__(self):
        self.pii_patterns = [
            r"\b\d{12}\b",  # Aadhaar-like
            r"\b\d{10}\b",  # phone-like
            r"[A-Z]{5}[0-9]{4}[A-Z]"  # PAN-like
        ]

    def contains_pii(self, text):
        for pattern in self.pii_patterns:
            if re.search(pattern, text):
                return True
        return False

    def is_out_of_scope(self, text):
        blocked = ["weather", "joke", "movie", "politics"]
        return any(word in text.lower() for word in blocked)
