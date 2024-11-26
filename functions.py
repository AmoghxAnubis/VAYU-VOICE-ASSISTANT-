import pyttsx3
import speech_recognition as sr
import datetime
import os
import pyautogui
import requests
import random
import wikipedia
# import cv2
import pyjokes
import time
from requests.adapters import HTTPAdapter
from requests.adapters import Retry
from fake_useragent import UserAgent
import webbrowser
from bs4 import BeautifulSoup
import requests
import google.generativeai as genai

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', 150)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def startup():
    speak("Hello sir, My name is VAYU, Your virtual assistant. How can I help you today?")


def takecommand():
    # it takes microphone input from users and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognising...")
        query = r.recognize_google(audio, language="en-in")
        print("user said:", query)

    except Exception as e:
        return "None"
    query = query.lower()
    return query


# import cv2

# def webcam():
#     # Initialize the webcam
#     cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

#     # Check if the webcam is successfully opened
#     if not cap.isOpened():
#         print("Error: Could not open webcam.")
#         return

#     while True:
#         # Read the frame
#         ret, img = cap.read()

#         # Check if the frame was successfully captured
#         if not ret:
#             print("Error: Failed to capture frame. Exiting...")
#             break

#         # Convert to grayscale
#         gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#         # Display the original frame
#         cv2.imshow('Webcam - Original', img)

#         # Display the grayscale frame
#         cv2.imshow('Webcam - Grayscale', gray)

#         # Stop if escape key is pressed
#         k = cv2.waitKey(30) & 0xff
#         if k == 27:  # Escape key ASCII code
#             break

#     # Release the webcam and close all OpenCV windows
#     cap.release()
#     cv2.destroyAllWindows()

# # Run the webcam function
# webcam()


# def givenews():
#     apikey = 'b9b7359b5b88408486d29e3e117cde5b'
#     url = f"https://newsdata.io/api/1/latest?apikey={apikey}&q=donald%20trump&region=washington-united%20states%20of%20america"
#     r = requests.get(url)
#     data = r.json()
#     data = data["articles"]
#     flag = True
#     count = 0
#     for items in data:
#         count += 1
#         if count > 5:
#             break
#         print(items["title"])
#         to_speak = items["title"].split(" - ")[0]
#         if flag:
#             speak("Today's top ten Headline are : ")
#             flag = False
#         else:
#             speak("Next news :")
#         speak(to_speak)

# def givenews():
#     try:
#         apikey = 'b9b7359b5b88408486d29e3e117cde5b'  # Replace with your actual API key
#         url = f"https://newsdata.io/api/1/latest?apikey={apikey}&q=donald%20trump&region=washington-united%20states%20of%20america"
#         r = requests.get(url)

#         if r.status_code == 200:
#             data = r.json()
#             if "articles" in data and data["articles"]:
#                 articles = data["articles"]
#                 count = 0
#                 flag = True
#                 for item in articles:
#                     if count >= 5:  # Limit to 5 articles
#                         break
#                     count += 1
#                     title = item.get("title", "No Title Available")  # Handle missing title gracefully
#                     print(title)  # Debugging output to verify titles are fetched

#                     # Non-blocking call for speak
#                     to_speak = title.split(" - ")[0]
#                     if flag:
#                         speak("Today's top five headlines are: ")
#                         flag = False
#                     else:
#                         speak("Next news:")

#                     # Add a debug statement to verify if `speak` completes
#                     print(f"Speaking headline {count}: {to_speak}")
#                     speak(to_speak)
#             else:
#                 print("No articles found in the response.")
#         else:
#             print(f"Error fetching news, status code: {r.status_code}")

#     except Exception as e:
#         print(f"An error occurred in givenews: {e}")

def weather(city):

    # Generating the url
    url = "https://google.com/search?q=weather+in+" + city

    # Sending HTTP request
    request_result = requests.get(url)

    # Pulling HTTP data from internet
    soup = BeautifulSoup(request_result.text, "html.parser")

    # Finding temperature in Celsius.
    # The temperature is stored inside the class "BNeawe".
    temp = soup.find("div", class_='BNeawe').text.replace("C", "celsius")
    print(temp)
    speak(f"Sir it looks like the temprature is {temp}")

# # import google.generativeai as genai


# # # Text-to-speech engine initialization
# # engine = pyttsx3.init()


# # def initialize_gemini_api(api_key):
# #     """
# #     Configures the Gemini API with the provided API key.
# #     """
# #     api_key='AIzaSyAp6yTUHKLwosET1cv3ZkmTrXTtahUX2ik'
# #     genai.configure(api_key=api_key)

# # def ai_search(prompt):
# #     """
# #     Sends a query to the Gemini API and retrieves a response.
# #     """
# #     try:
# #         # Call the Gemini API chat model
# #         response = genai.chat(
# #             model="models/chat-bison-001",  # Use the specified model
# #             messages=[{"author": "user", "content": prompt}]
# #         )
# #         # Extract and return the AI's response
# #         return response.messages[-1]["content"]

# #     except Exception as e:
# #         print(f"Error during AI search: {e}")
# #         return "I'm sorry, I encountered an issue while processing your request."

# # def get_voice_input():
# #     """
# #     Captures voice input from the user and returns it as text.
# #     """
# #     recognizer = sr.Recognizer()
# #     with sr.Microphone() as source:
# #         print("Listening...")
# #         try:
# #             audio = recognizer.listen(source, timeout=5)
# #             query = recognizer.recognize_google(audio)
# #             print(f"You said: {query}")
# #             return query
# #         except sr.UnknownValueError:
# #             print("Sorry, I didn't catch that.")
# #             return None
# #         except sr.RequestError:
# #             print("Could not request results; check your internet connection.")
# #             return None
# #         except Exception as e:
# #             print(f"Error: {e}")
# #             return None

# # def speak_output(text):
# #     """
# #     Uses text-to-speech to vocalize the provided text.
# #     """
# #     print(f"Assistant: {text}")
# #     engine.say(text)
# #     engine.runAndWait()
# class GeminiSearch:
#     def __init__(self, api_key):
#         """Initialize Gemini with API key and configure the model"""
#         self.api_key = api_key
#         genai.configure(api_key=self.api_key)
#         self.model = genai.GenerativeModel('gemini-pro')
#         self.speech_engine = pyttsx3.init()
#         self.recognizer = sr.Recognizer()
    
#     def listen_for_query(self):
#         """Listen for user's search query using microphone"""
#         with sr.Microphone() as source:
#             print("What would you like to search for?")
#             self.speak("What would you like to search for?")
#             try:
#                 audio = self.recognizer.listen(source, timeout=5)
#                 query = self.recognizer.recognize_google(audio)
#                 print(f"Search query received: {query}")
#                 return query
#             except sr.UnknownValueError:
#                 return "Sorry, I couldn't understand that."
#             except sr.RequestError:
#                 return "Sorry, there was an error with the speech recognition service."

#     def speak(self, text):
#         """Convert text to speech"""
#         self.speech_engine.say(text)
#         self.speech_engine.runAndWait()

#     def search(self):
#         """Main search function that handles the complete search flow"""
#         print("Starting Gemini search...")
#         query = self.listen_for_query()
#         if query.startswith("Sorry"):
#             self.speak(query)
#             return
        
#         try:
#             print(f"Sending query to Gemini: {query}")
#             response = self.model.generate_content(query)
#             result = response.text
#             print(f"Gemini response: {result}")
#             self.speak(result)
#         except Exception as e:
#             error_message = f"An error occurred: {str(e)}"
#             print(error_message)
#             self.speak("Sorry, I encountered an error while searching.")
    
    
    
