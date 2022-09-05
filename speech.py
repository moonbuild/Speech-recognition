import pyttsx3
import speech_recognition as sr
import datetime


#find alternatives to sapi5 if any
#same for voices
engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice', 'voices[1].id')

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wish():
    hour=datetime.datetime.now().hour

    if hour>=0 and hour<12:
        speak("Hello, Good Morning sir")
        print("Hello, Good Morning sir")
    elif hour>=12 and hour<18:
        speak("Hello, Good Afternoon sir")
        print("Hello, Good Afternoon sir")    
    else:
        speak("Hello, Good Evening sir")
        print("Hello, Good Evening sir")

def speech_to_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening🎧")
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio, language='en-in')
            print("user said: ",statement,'\n')
        except Exception as e:
            speak("Sorry, please say that again")
            return "None"
        return statement
speak("Loading your personal AI- Boat")
wish()

if __name__=='__main__':
    while True:
        speak('Tell me how can i help u now?')
        statement = speech_to_text().lower()
        if statement==0:
            continue

        if "adios" in statement or "ok bye" in statement or "stop" in statement:
            speak("Your personal assistant-Boat is now shutting down")
            print("Your personal assistant-Boat is now shutting down")
            break

        if 'wikipedia' in statement:
            