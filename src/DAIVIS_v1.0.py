import time, os
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound


class DAIVIS(object):
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
        if 'daivis' == text:
            answer_text = 'yes Master.'
        elif 'thank' in text:
            answer_text = 'My pleasure.'
        elif 'shutdown' in text:
            answer_text = 'See you Master.'
            self.shutdown(wait_for_stop=False)
        elif 'stock' in text:
            answer_text = self.stock_report()
        elif 'weather' in text:
            answer_text = 'weather'
        else:
            answer_text = 'Please speak again.'
        self.speak(answer_text, fname_ans)

    def speak(self, text, fname):
        print('[DAIVIS]: ' + text)
        tts = gTTS(text=text, lang='en')
        tts.save(fname)
        playsound(fname)

    def stock_report(self):
        asnwer = f''
        if os.path.isfile(path_stock):
          asnwer = f''
        else:
            # report analyze file run
            asnwer = f'' + f'' + f''
        return asnwer


if __name__ == '__main__':
    daivis = DAIVIS()
    daivis.process()
    while True:
        time.sleep(0.1)