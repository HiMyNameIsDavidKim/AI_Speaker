import time, os
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound


def listen(recognizer, audio):
    try:
        text = recognizer.recognize_google(audio, language='en')
        print('[You]: ' + text)
    except sr.UnknownValueError:
        print(f'UnknownValueError')
    except sr.RequestError as e:
        print(f'RequestError: {e}')

def answer(input_text):
    pass

def speak(text):
    print('[AI]: ' + text)
    file_name = './save/voice.mp3'
    tts = gTTS(text=text, lang='en')
    tts.save(file_name)
    playsound(file_name)


if __name__ == '__main__':
    r = sr.Recognizer()
    m = sr.Microphone()

    speak('Welcome home Master.')
    stop_listening = r.listen_in_background(m, listen())
    # stop_listening(wait_for_stop=False)

    while True:
        time.sleep(0.1)