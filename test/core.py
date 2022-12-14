from neuralintents import GenericAssistant
import speech_recognition
import pyttsx3 as ts

recognizer = speech_recognition.Recognizer()

engine = ts.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice', 'voices[1].id')
# engine.setProperty('rate', 150)

def hello_Norway():
    print("Hello Norway")

mappings = {'greetings': hello_Norway}
boat = GenericAssistant('intents.json', intent_methods=mappings, model_name="boat_ai")
boat.train_model()
boat.save_model()

if __name__ == "__main__":
    try:
        with speech_recognition.Microphone() as mic:

            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio=recognizer.listen(mic)

            message=recognizer.recognize_google(audio)
            message = message.lower()
        boat.request(message)
    except speech_recognition.UnknownValueError:
        recognizer=speech_recognition.Recognizer()