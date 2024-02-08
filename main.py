import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
from config import password

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")
    speak("How can i help you sir ?")

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('bruce186201@gmail.com', password)
    server.sendmail('rohit186201@gmail.com', to, content)
    server.close()

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognising....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        return query.lower()

    except Exception as e:
        #peint(e)
        print("Say that again please.... ")
        return ""

if __name__ == "__main__":
    speak("Hi I am Arester")
    wishme()



    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia....')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("Acoording to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com.com")

        elif "play music" in query:
            try:
                # Provide the correct path to the Spotify executable on your system
                spotify_path = r"C:\Users\rohit\AppData\Local\Microsoft\WindowsApps\Spotify"
                os.startfile(spotify_path)
                speak("Opening Spotify, sir...")
            except Exception as e:
                print("Error:", e)
                speak("Sorry, I couldn't open Spotify.")

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir time is {strTime}")

        elif 'quit' in query:
            speak("Ok sir")
            exit()

        elif "open chrome" in query:
            try:
                # Provide the correct path to the Spotify executable on your system
                chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
                os.startfile(chrome_path)
                speak("Opening Chrome, sir...")
            except Exception as e:
                print("Error:", e)
                speak("Sorry, I couldn't open Chrome.")

        elif 'email to rohit' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "rohit186201@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir. I am not able to send this email")