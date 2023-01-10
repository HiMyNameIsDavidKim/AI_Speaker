# pip install SpeechRecognition
# brew install portaudio
# sudo nano $HOME/.pydistutils.cfg
# homebrew portaudio 경로 설정
# pip install pyaudio
# brew install flac
# pip install pydub
# brew install ffmpeg

import speech_recognition as sr
from pydub import AudioSegment

# 마이크로 음성 인식
r = sr.Recognizer()
with sr.Microphone() as source:
    print('듣고 있어요.')
    listen = r.listen(source)

# 파일로 음성 인식
w = AudioSegment.from_mp3('save/sample.mp3')
w.export('./save/sample.wav', format='wav')
r = sr.Recognizer()
with sr.AudioFile('save/sample.wav') as source:
    record = r.record(source)

try:
    text = r.recognize_google(listen, language='en-US')
    print(text)
    text = r.recognize_google(listen, language='ko')
    print(text)
except sr.UnknownValueError: print('인식 실패')
except sr.RequestError as e: print(f'요청 실패: {e}')

