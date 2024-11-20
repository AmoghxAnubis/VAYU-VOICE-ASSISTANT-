import pyttsx3
import speech_recognition as sr
import datetime
import os
import pyautogui
import requests
import random
import wikipedia
import cv2
import pyjokes
import time
from requests.adapters import HTTPAdapter
from requests.adapters import Retry
from fake_useragent import UserAgent
import webbrowser
from bs4 import BeautifulSoup
import requests

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
#     apikey = 'b9b7359b5b88408486d29e3e117cde5bapikey'
#     url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={apikey}"
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
#         apikey = 'cb6765fa7b4a34d1351fdeb819829336'  # Replace with your actual API key
#         url = f"http://api.mediastack.com/v1/news?access_key={apikey}"
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
