import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import time
import ecapture.ecapture as ec
import wolframalpha

engine = pyttsx3.init()
# engine = pyttsx3.init('sapi5')
# voices=engine.getProperty('voices')
# engine.setProperty('voice', 'voices[0].id')

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

def takeCommands():
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
print("Loading your personal AI- Boat")
wish()

if __name__=='__main__':
    while True:
        speak('Tell me how can i help u now?')
        statement = takeCommands().lower()
        if statement==0:
            continue

        if "adios" in statement or "ok bye" in statement or "stop" in statement:
            speak("Your personal assistant-Boat is now shutting down")
            print("Your personal assistant-Boat is now shutting down")
            break

        if 'search wikipedia on ' in statement:
            speak('Searching through Wikipedia...')
            statement = statement.replace('search the wikipedia on','')
            results=wikipedia.summary(statement, sentences=3)
            speak('According to Wikipedia')
            print(results)
            speak(results)

        elif 'open youtube' in  statement:
            webbrowser.open_new_tab('www.youtube.com')
            speak('opening Youtube')
            time.sleep(5)
        elif 'open google' in  statement or 'open new tab' in statement:
            webbrowser.open_new_tab('www.google.com')
            speak('opening google')
            time.sleep(5)
        elif 'open mail' in statement or 'check the mail' in statement:
            webbrowser.open_new_tab('www.gmail.com')
            speak('gmail is now open')
            time.sleep(5)
        
        elif 'who are you' in statement or 'what can you do' in statement:
            speak('I am Boat version 1 your personal assistant. I am currrently able to do minor tasks like opening websites, tell the time, take a photo, play songs search through wikipedia')
        elif 'camera' in statement or 'take a photo' in statement:
            ec.capture(0,'frame', 'cheese.jpg')
        elif 'search' in statement:
            statement=statement.replace('search','')
            print(statement)
            webbrowser.open_new_tab(statement)
            time.sleep(5)
        elif 'ask' in statement:
            speak('Yes?')
            question=takeCommands()
            appid="P4HU6J-YTXTXUPV2T"
            client=wolframalpha.Client('P4HU6J-YTXTXUPV2T')
            result = client.query(question).results
            answer=next(result).text
            speak(answer)
            print(answer)