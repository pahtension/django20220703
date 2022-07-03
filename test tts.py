from gtts import gTTS


text= "안녕하세요"
tts = gTTS(text=text, lang="ko")
filename = "voice.mp3"
tts.save(filename)



















