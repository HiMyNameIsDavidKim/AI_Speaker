# venv
# pip3 install gTTS
# pip3 install playsound
# pip3 install PyObjC

from gtts import gTTS
from playsound import playsound
file_name = './save/sample.mp3'

# 영어
text = 'Can I help you?'
tts_en = gTTS(text=text, lang='en')
tts_en.save(file_name)
playsound(file_name)

# 한글
text = '파이썬을 배우면 이런 것도 할 수 있어요.'
tts_ko = gTTS(text=text, lang='ko')
tts_ko.save(file_name)
playsound(file_name)

# 파일 읽기
with open('./data/sample.txt', 'r', encoding='utf8') as f:
    text = f.read()
tts_ko = gTTS(text=text, lang='ko')
tts_ko.save(file_name)
playsound(file_name)

