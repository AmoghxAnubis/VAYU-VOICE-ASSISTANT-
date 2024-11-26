from brain import *
from functions import *
__AUTH__ = "HAZEL"
__VERSION__ = "2.0.0"


# def main():
#     # Step 1: Set the Gemini API key
#     api_key = 'AIzaSyAp6yTUHKLwosET1cv3ZkmTrXTtahUX2ik'
#     initialize_gemini_api(api_key)  # Initialize the Gemini API

#     # Step 2: Create an instance of GeminiBrain
#     gemini_brain = GeminiBrain(api_key)

#     # Step 3: Call the AI search protocol
#     print("Starting the voice assistant...")
#     gemini_brain.process_user_query()  # This listens and processes the user query
# def initialize_gemini():
#     """Initialize Gemini instance"""
#     GEMINI_API_KEY = "AIzaSyAp6yTUHKLwosET1cv3ZkmTrXTtahUX2ik"  # Replace with your actual API key
#     print("Initializing Gemini...")
#     return GeminiSearch(GEMINI_API_KEY)

# def main_loop():
#     """Main program loop with Gemini integration"""
#     print("Starting main loop... Say 'AI search' to begin searching")
#     gemini = initialize_gemini()
#     recognizer = sr.Recognizer()
    
#     while True:
#         try:
#             with sr.Microphone() as source:
#                 print("\nListening...")
#                 recognizer.adjust_for_ambient_noise(source, duration=0.5)
#                 audio = recognizer.listen(source)
#                 command = recognizer.recognize_google(audio).lower()
#                 print(f"You said: {command}")
                
#                 # Process the command
#                 process_commands(command, gemini)
                    
#         except sr.UnknownValueError:
#             print("Could not understand audio")
#         except sr.RequestError as e:
#             print(f"Could not request results; {e}")
#         except Exception as e:
#             print(f"An error occurred: {str(e)}")
# global gemini_model
# gemini_model = None

# def initialize_gemini():
#     """Initialize Gemini instance"""
#     global gemini_model
#     try:
#         GEMINI_API_KEY = "AIzaSyAp6yTUHKLwosET1cv3ZkmTrXTtahUX2ik"  # Replace with your actual API key
#         print("Initializing Gemini...")
#         genai.configure(api_key=GEMINI_API_KEY)
#         gemini_model = genai.GenerativeModel('gemini-pro')
#         print("Gemini AI initialized successfully")
#     except Exception as e:
#         print(f"Warning: Gemini initialization failed: {str(e)}")
#         gemini_model = None

if __name__ == "__main__":

    startup()
    protocols()
  
