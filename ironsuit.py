import pyttsx3
import speech_recognition as sr
import serial

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
arduino = serial.Serial(port="COM3", baudrate=9600, timeout=.1)

arduino.write(bytes("0", "utf-8"))

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


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


while True:
    query = takeCommand().lower()

    if "jarvis" in query:
        command = query.split("jarvis ")[1]

        if command == "apri la maschera" or command == "apri maschera":
            print("apri")
            arduino.write(bytes("1", "utf-8"))
        elif command == "chiudi la maschera" or command == "chiudi maschera":
            print("chiudi")
            arduino.write(bytes("0", "utf-8"))
