import time, os
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound


class AI_Speaker(object):
    def __init__(self):
        global fname_init, fname_ans
        fname_init = './save/init.mp3'
        fname_ans = './save/ans.mp3'

    def process(self):
        r = sr.Recognizer()
        m = sr.Microphone()
        self.speak('Welcome home Master.', fname_init)
        self.stop_listening = r.listen_in_background(m, self.listen)

    def listen(self, recognizer, audio):
        try:
            text = recognizer.recognize_google(audio, language='en')
            print('[You]: ' + text)
            self.answer(text)
        except sr.UnknownValueError:
            print(f'UnknownValueError')
        except sr.RequestError as e:
            print(f'RequestError: {e}')

    def answer(self, text):
        if 'hello' in text:
            answer_text = 'Hello Master.'
        elif 'weather' in text:
            answer_text = "The temperature in Seoul is 20 degrees. It will be sunny day."
        elif 'thank' in text:
            answer_text = 'My pleasure.'
        elif 'exit' in text:
            answer_text = 'See you Master.'
            self.stop_listening(wait_for_stop=False)
        else:
            answer_text = 'Please speak again.'
        self.speak(answer_text, fname_ans)

    def speak(self, text, fname):
        print('[AI]: ' + text)
        tts = gTTS(text=text, lang='en')
        tts.save(fname)
        playsound(fname)


if __name__ == '__main__':
    ai_sp = AI_Speaker()
    ai_sp.process()
    while True:
        time.sleep(0.1)