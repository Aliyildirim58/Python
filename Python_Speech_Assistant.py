import speech_recognition as sr
from datetime import datetime
import webbrowser
import time
from gtts import gTTS, lang
from playsound import playsound
import random
import os
r=sr.Recognizer()

def record(ask=False):
    with sr.Microphone() as source:
     if ask:
         speak(ask)
     audio=r.listen(source)
     voice=''
     try:
        voice=r.recognize_google(audio,language='tr-TR')
     except sr.UnknownValueError:
         speak("Ne Söylediğini Anlayamadım")
     except sr.RequestError:
         speak("Sistem Çalışmadı")
     return voice
def response(voice):
    if 'Selam' in voice:
        speak("Aleykümselam")
    if 'ismin ne' in voice:
        speak("Merhaba ben sivaslı siri halk arasında kangal siri de derler.")
    if 'Ne yapıyorsun dayı' in voice:
        speak("Kendim için yapmıyorum ezel")
    if 'mesele neymiş dayı' in voice:
        speak("Mesele dost bildiğin adamın eliyle ölmekmiş mesele.Şimdi anladın mı o avludaki çocuk kimmiş kardeş")
    if 'Ne yaptın Ramiz işi berbat ettin'in voice:
        speak("Tamam kardeş tamam bir zamanalar buralar mert insanların diyarıydı şimdi bakıyorumda çapulcuları doldurmuşsun.")
    if 'saat kaç' in voice:
        speak(datetime.now().strftime('%H:%M:%S'))
    if 'arama yap' in voice:
        search=record('Ne aramak istiyorsun')
        url='https://google.com/search?q='+search
        webbrowser.get().open(url)
        speak(search+' için bulduğum sonuçlar')
    if 'konum bul' in voice:
        location=record('Hangi konumu bulmak istiyorsunuz?')
        url='https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        speak(location+' için bulduğum konum bilgileri')
    if 'kapat' in voice:
        speak('Görüşürüz iyi günler')
        exit()

def speak(string):
    tts=gTTS(string,lang='tr')
    rand=random.randint(1,10000)
    file='audio-'+str(rand)+'.mp3'
    tts.save(file)
    playsound(file)
    os.remove(file)


speak("Buyur nasıl yardımcı olabilirim?")
time.sleep(1)
while 1:
    voice=record()
    print(voice)
    response(voice)

