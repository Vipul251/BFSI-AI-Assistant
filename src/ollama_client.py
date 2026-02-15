import requests

class OllamaLLM:
    def __init__(self, model="tinyllama"):
        self.model = model
        self.url = "http://localhost:11434/api/generate"

    def generate(self, query, context=None):
        prompt = f"""
You are a compliant BFSI assistant.
Rules:
- Be professional
- Do not guess financial numbers
- If unsure, ask user to contact support

Context: {context}

User: {query}
Assistant:
"""

        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False
        }

        response = requests.post(self.url, json=payload)
        return response.json()["response"]
