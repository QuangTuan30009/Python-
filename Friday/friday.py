import pyttsx3 
import datetime
friday = pyttsx3.init()
voice = friday.getProperty('voices')
friday.setProperty('voice', voice[1].id)

def speak(audio):
    friday.say(audio)
    friday.runAndwait()
speak("Hello Youtube")
def time():
    Time = datetime.datetime.now().strftime("%I : %M : %P")
    speak(Time)
time()

