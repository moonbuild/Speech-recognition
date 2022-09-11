from neuralintents import GenericAssistant
import speech_recognition
import pyttsx3 as ts
import sys

recognizer = speech_recognition.Recognizer()

engine = ts.init()
engine.setProperty('rate', 150)

def hello_Norway():
    print("Hello Norway")

mappings = {'greetings': hello_Norway}
boat = GenericAssistant('intents.json', intent_methods=mappings)
boat.train_model()

baot.request()