from ecapture import ecapture as ec
import subprocess
from email.mime import audio
from logging import exception
from tkinter.tix import MAIN
from unittest import result
from pip import main
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12 :
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    
    speak("Hello i am Iota. Please tell me how may i help you")

def takecommand():
    # It takes microphone from the user and returns string output.
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except exception as e:
        # print(e)
        print("Say that again please.....")
        return "None"
    
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to,content)
    server.close()

if __name__ == "__main__":
    wishMe()
    #while True:
    if 1:
        query = takecommand().lower()
        # Logic for executing task based on query 

        if 'wikipedia' in query:
            speak("Searching Wikipedia....")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')

        elif 'open google' in query:
            webbrowser.open('google.com')

        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com')

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codepath = "C:\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif 'email to amit' in query:
            try:
                speak("What should I say?")
                content = takecommand()
                to = "ag2255793@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent! ")
            except exception as e:
                print(e)
                speak("Sorry my friend. I am unable to send this email right now.")

        elif "camera" in query or "take a photo" in query:
            ec.capture(0, "Iota Camera ", "img.jpg")

        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])
             
        elif "hibernate" in query or "sleep" in query:
            speak("Hibernating")
            subprocess.call("shutdown / h")
 
        elif "log off" in query or "sign out" in query:
            speak("Make sure all the application are closed before sign-out")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])
            
        elif 'joke' in query:
            speak(pyjokes.get_joke())
            
        elif 'quit' in query:
            exit()
