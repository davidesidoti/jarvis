import datetime
import os
import shutil

import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Buongiorno !")

    elif 12 <= hour < 18:
        speak("Buon pomeriggio !")

    else:
        speak("Buonasera !")

    speak("Sono il tuo assistente")
    speak('Jarvis')


def username():
    speak("Come dovrei chiamarti?")
    uname = takeCommand()
    speak("Benvenuto")
    speak(uname)
    columns = shutil.get_terminal_size().columns

    print("#####################".center(columns))
    print("Benvenuto ", uname.center(columns))
    print("#####################".center(columns))

    speak("Come posso aiutarti?")


def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='it-IT')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Unable to Recognize your voice.")
        return "None"

    return query


clear = lambda: os.system('cls')

clear()
wishMe()
username()

while True:
    query = takeCommand().lower()

    if 'ore sono' in query or 'ora è' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f'Sono le {strTime}')
