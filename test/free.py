from neuralintents import GenericAssistant as ga
import speech_recognition
boat=ga.load_model('boat_ai.h5')
print(boat.request('hello'))
recognizer = speech_recognition.Recognizer()

while True:
    try:
        with speech_recognition.Microphone() as mic:
            print("Listening")
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio=recognizer.listen(mic)

            message=recognizer.recognize_google(audio)
            message = message.lower()
        boat.request(message)
    except speech_recognition.UnknownValueError:
        recognizer=speech_recognition.Recognizer()