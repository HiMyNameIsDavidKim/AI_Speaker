import time, os, sys
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound


class DAVIS(object):
    def __init__(self):
        global fname_init, fname_ans, path_stock
        fname_init = './save/init.mp3'
        fname_ans = './save/ans.mp3'
        path_stock = '/Users/davidkim/PycharmProjects/pythonProject/auto_stock_report/report/stock_report_23-01-10 .xlsx'
        self.shutdown = None

    def process(self):
        r = sr.Recognizer()
        m = sr.Microphone()
        self.speak('Welcome home Master.', fname_init)
        # auto insight report, stock report, weather report
        self.shutdown = r.listen_in_background(m, self.listen)

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
        text = text.lower()
        if 'hi' in text:
            answer_text = 'Hi Master.'
        elif 'davis' == text:
            answer_text = 'Yes Master.'
        elif 'thank' in text:
            answer_text = 'My pleasure.'
        elif 'shut down' in text:
            answer_text = 'See you Master.'
            self.speak(answer_text, fname_ans)
            self.shutdown = True
            sys.exit()
        elif 'stock' in text:
            answer_text = self.stock_report()
        elif 'weather' in text:
            answer_text = 'weather'
        else:
            answer_text = 'Please speak again.'
        self.speak(answer_text, fname_ans)

    def speak(self, text, fname):
        print('[DAVIS]: ' + text)
        tts = gTTS(text=text, lang='en')
        tts.save(fname)
        playsound(fname)

    def stock_report(self):
        answer = f''
        if os.path.isfile(path_stock):
          answer = f''
        else:
            # report analyze file run
            answer = f'' + f'' + f''
        return answer


if __name__ == '__main__':
    davis = DAVIS()
    davis.process()
    while davis.shutdown is not True:
        time.sleep(0.1)
