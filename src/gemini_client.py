from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

class GeminiClient:
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        
        if not api_key:
            raise ValueError("GEMINI_API_KEY enviroment variable is missing!")
        
        self.client = genai.Client(api_key=api_key)
        self.model = "gemini-3.8-flash"
        
    def generate_response(self, prompt: str) -> str:
        """
        Sends a prompt to Gemini API and returns the generated response.
        """
        
        response = self.client.interactions.create(
            model=self.model,
            input=prompt
        )
        
        return response.output_text