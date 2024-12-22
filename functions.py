import pyttsx3
import speech_recognition as sr
import datetime
import os
import pyautogui
import requests
import random
import wikipedia
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

