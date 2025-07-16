import google.generativeai as genai
import os


# 1. Replace "PASTE_YOUR_API_KEY_HERE" with your actual Gemini API key.
api_key = "your api key" 

# 2. The line below that reads from the environment variable is no longer needed.
# api_key = os.environ.get("GEMINI_API_KEY")

if not api_key or api_key == "PASTE_YOUR_API_KEY_HERE":
    print("🚨 Error: API key not set in the script.")
    print("Please open the script and replace 'PASTE_YOUR_API_KEY_HERE' with your actual key.")
    exit()
else:
    print("✅ API key loaded directly from script.")
    genai.configure(api_key=api_key)

# --- AI Model Initialization ---
# This is the prompt that tells the AI how to behave.
system_instruction = (
    "You are 'EcoAgent', an expert AI focused on climate change. "
    "Your purpose is to provide clear, factual, and unbiased information. "
    "When a user asks a question or presents a claim, fact-check it using scientific evidence. "
    "When a user asks for advice, provide practical, actionable steps they can take. "
    "Always maintain a helpful and informative tone. Cite reputable sources when possible, but do not make up URLs."
)

model = genai.GenerativeModel(
    # Switched to the 'flash' model to work around the quota error.
    model_name='gemini-1.5-flash-latest', 
    system_instruction=system_instruction
)

# --- Main Application Logic ---
def main():
    """
    The main function to run the interactive chat session.
    """
    print("\n🌍 Welcome to the Climate Change Fact-Checker & Advisor!")
    print("   Ask me to fact-check a claim or give you sustainability tips.")
    print("   Type 'quit' or 'exit' to end the session.\n")

    # Start a chat session
    chat = model.start_chat(history=[])

    while True:
        # Get user input
        user_query = input("You: ")

        # Check if the user wants to exit
        if user_query.lower() in ['quit', 'exit']:
            print("\n👋 Thank you for using the Climate Advisor. Stay green!")
            break
        
        # Send the user's message to the model and handle potential errors
        try:
            response = chat.send_message(user_query)
            # Print the model's response
            print(f"\nEcoAgent: {response.text}\n")
        except Exception as e:
            print(f"\n🚨 An error occurred while communicating with the API: {e}\n")


if __name__ == "__main__":
    main()
