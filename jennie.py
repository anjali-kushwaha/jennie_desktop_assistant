from email.mime import audio
from http import server
from importlib.resources import contents
from winreg import QueryValueEx
from pip import main
import pyttsx3
import datetime
from setuptools import Command
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import pywhatkit
from flask import Flask
import pyjokes
from googletrans import Translator

engine = pyttsx3.init("sapi5")
"""SAPI 5 applications issue calls through the API (for example to load a recognition 
grammar; start recognition; or provide text to be synthesized)."""
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoom!")

    else:
        speak("Good Evening!")
    speak("hi i'm jennie, how can i help ypu ")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        #print(e)
        speak("i don't understand....can you say it again")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("youremail@gmal.com", "your-password-here")
    server.sendemail("youremail@gmail.com", to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while (10):
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('seaching wikipedia......')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youTube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("goggel.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com ")
        #also for play song

        elif 'open control panel' in query:
            codePath = "C:\\Users\\anjali\\AppData\\Roaming\\Microsoft\Windows\\Start Menu\\Programs\\System Tools"
            os.startfile(codePath)

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S ")
            speak(f"it's {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\anjali\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open Microsoft Office' in query:
            codePath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office"
            os.startfile(codePath)

        #email
        elif 'email to anjali' in query:
            try:
                speak("what should i say..?")
                content = takeCommand()
                to = "anjalikushwaha3012@gmail.com"
                sendEmail(to, content)
                speak("email has been send")
            except Exception as e:
                print(e)
                print("email not send")

        elif 'play' in query:
            song = Command.replace("play", "")
            speak("playing" + song)
            pywhatkit.playonyt(song)

        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif 'in hindi' in query:
            translator = Translator()
            from_lang = 'en'
            to_lang = 'hi'
            out = translator.translate(query, to_lang)
