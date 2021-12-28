import datetime
import os
import pyttsx3
import random
import re
import shutil
import speech_recognition as sr
import webbrowser
import wolframalpha
from googletrans import Translator, constants

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
translator = Translator()


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

    speak("Sono il tuo assistente, Jarvis")


def username():
    if os.path.isdir('C:\\Users\\sidot\\AppData\\Roaming\\Jarvis'):
        _userdata = open('C:\\Users\\sidot\\AppData\\Roaming\\Jarvis\\user_data.md', 'r')
        _username = _userdata.read().split('----')[1]
        _username = _username.replace('\n', '')
        speak(f'Bentornato, {_username}')
        speak("Come posso aiutarti?")
    else:
        speak("Come dovrei chiamarti?")
        uname = takeCommand()
        os.mkdir('C:\\Users\\sidot\\AppData\\Roaming\\Jarvis')
        _appdatafile = open('C:\\Users\\sidot\\AppData\\Roaming\\Jarvis\\user_data.md', 'a')
        _appdatafile.write(f'----\n{uname}')
        _appdatafile.close()
        speak("Benvenuto")
        speak(uname)
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
    chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe %s"

    # TELLS THE TIME
    if 'ore sono' in query or 'ora è' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f'Sono le {strTime}')
    # OPEN WEB APPS
    elif 'apri youtube' in query or 'aprire youtube' in query:
        speak('Certo!')
        webbrowser.open('https://www.youtube.com/')
    elif 'apri google' in query or 'aprire google' in query:
        speak('Certo!')
        webbrowser.open('https://www.google.it/')
    elif 'apri reddit' in query or 'aprire reddit' in query:
        speak('Certo!')
        webbrowser.open('https://www.reddit.com/')
    elif 'apri disney plus' in query or 'aprire disney plus' in query:
        speak('Certo!')
        webbrowser.open('https://www.disneyplus.com/')
    elif 'apri netflix' in query or 'aprire netflix' in query:
        speak('Certo!')
        webbrowser.open('https://www.netflix.com/')
    # OPEN APPLICATIONS
    elif 'lavoro con python' in query or 'lavoro in python' in query:
        speak('Buon lavoro!')
        os.startfile("E:\\Program Files (x86)\\PyCharm 2021.3\\bin\\pycharm64.exe")
        os.startfile("C:\\Users\\sidot\\AppData\\Local\\GitHubDesktop\\GitHubDesktop.exe")
    elif 'lavoro con i siti' in query or 'lavoro in web' in query:
        speak('Buon lavoro!')
        os.startfile("E:\\Program Files (x86)\\WebStorm 2021.3\\bin\\webstorm64.exe")
        os.startfile("C:\\Users\\sidot\\AppData\\Local\\GitHubDesktop\\GitHubDesktop.exe")
    elif 'lavoro con unity' in query or 'lavoro in unity' in query:
        speak('Buon lavoro!')
        os.startfile("E:\\Program Files (x86)\\JetBrains Rider 2021.3.1\\bin\\rider64.exe")
        os.startfile("C:\\Program Files\\Unity Hub\\Unity Hub.exe")
    elif 'lavoro con php' in query or 'lavoro in php' in query:
        speak('Buon lavoro!')
        os.startfile("E:\\Program Files (x86)\\PhpStorm 2021.3\\bin\\phpstorm64.exe")
        os.startfile("C:\\xampp\\xampp-control.exe")
        os.startfile("C:\\Users\\sidot\\AppData\\Local\\GitHubDesktop\\GitHubDesktop.exe")
    # GENERAL HELP
    elif 'quanto fa' in query:
        client = wolframalpha.Client('VQL97W-L9G38URH4A')
        query = query.replace('quanto fa ', '')
        query = translator.translate(query, src='it', dest='en')
        res = client.query(query.text)
        if '...' in next(res.results).text:
            answer = next(res.results).text.replace('...', '')
        else:
            answer = next(res.results).text
        regex = r'^[+-]{0,1}((\d*\.)|\d*)\d+$'
        if re.match(regex, answer) is not None:
            answer = round(float(answer), 3)
            answer = str(answer).replace('.', ',')
        else:
            print('NOT NUMBER')
            answer = translator.translate(answer, src='en', dest='it').text
        print("Il risultato è:  " + answer)
        speak("Il risultato è:  " + answer)
    elif 'cerca' in query:
        query = query.replace('cerca', '')
        query = query.split(' ')
        webbrowser.open('https://www.google.com/search?q=' + '+'.join(query))
    # USER DATA
    elif 'cambiami il nome' in query or 'cambia il mio nome' in query or 'cambiare il mio nome' in query:
        shutil.rmtree('C:\\Users\\sidot\\AppData\\Roaming\\Jarvis')
        username()
    # ASSISTANT PERSONALITY
    elif 'grazie' in query:
        _thanks = ['Prego!', 'Di niente!', 'Non c\'è di che!', 'Niente!']
        speak(random.choice(_thanks))
    elif 'come stai' in query:
        speak('Sto bene grazie! Tu come stai?')
    elif 'bene' in query or 'apposto' in query:
        speak('Ne sono felice!')
    elif 'come ti chiami' in query or 'qual è il tuo nome' in query:
        _reply = ['Mi chiamo Jarvis', 'Il mio nome è Jarvis', 'I miei amici mi chiamano Jarvis']
        speak(random.choice(_reply))
    elif 'chi ti ha creato' in query or 'chi è il tuo creatore' in query or 'chi ti ha fatto' in query or 'chi ti ha programmato' in query:
        speak('Il mio creatore è quel geniaccio di Davide Sidoti!')
