from .csv_handler import read_input
from .gemini_client import GeminiClient

def main():
    print("loading GeminiClient.")
    gemini = GeminiClient()
    
    prompt = input("Give a prompt: ")
    
    print("Getting response from Gemini...")
    
    response = gemini.generate_response(prompt)
    
    print(f"Response is: {response}")
    
    

############################    
    
if __name__ == "__main__":
    main()