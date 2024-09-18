import os
import playsound
import speech_recognition_python as sr
import time
import sys
import ctypes
import wikipedia
import datetime
import json
import re
import webbrowser
import smtplib
import requests
import urllib
import urllib.request as urllib2
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from time import strftime
from gtts import gTTS

wikipedia.set_lang("vi")
language = "vi"
path = ChromeDriverManager().install()

#Chức năng chuyển văn bản thành âm thanh
def speak(text):
    print("Bot: {}".format(text))
    tts = gTTS(text = text, lang=language, slow=False)
    tts.save("Sound.mp3")
    playsound.playsound("sound.mp3", False)
    os.remove("sound.mp3")

#Chức năng chuyển âm thanh thành văn bản
def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Tôi: ", end="")
        audio = r.listen(source, phrase_time_limit=5)
        try:
            text = r.recognize_google_cloud(audio, language="vi - VN")
            print(text)
            return text
        except:
            print("...")
            return 0

def stop():
    speak("Hẹn gặp lại sau !")

def get_text():
    for i in range(3):
        text = get_audio()
        if text:
            return text.lower()
        elif i <2:
            speak("Bot không nghe rõ, nói lại ii")
    time.sleep(2)
    stop()
    return 0

#Chức năng giao tiếp, chào hỏi
def hello(name):
    day_time =int(strftime("%H"))
    if day_time < 12:
        speak("Chào buổi sáng bạn {}. Chúc bạn một ngày tốt lành.".format(name))
    elif 12 <= day_time < 18:
        speak("Chào buổi chiều bạn {}. Bạn đã dự định gì cho chiều nay chưa.".format(name))
    else:
        speak("Chào buổi tối bạn {}. Bạn đã ăn tối chưa nhỉ.".format(name))

# Chức năng hiển thị thời gian
def get_time(text):
    now = datetime.datetime.now()
    if "giờ" in text:
        speak("Bây gờ là %d giờ, % phút" % (now.hour, now.minute))
    elif "ngày" in text:
        speak("Hôm nay là ngày %d tháng %d năm %d" %
              (now.day, now.month, now.year))
    else:
        speak("bot chưa hiểu ý bạn lắm. bạn nói lại ii")

#Chức năng mở ứng dụng hệ thống,
# website và chức năng tìm kiếm từ khóa trên Google

def open_application(text):
    if "Microsoft Edge" in text:
        speak("Mở Microsoft Edge")
        os.startfile("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")
    elif "word" in text:
        speak("Mở Microsoft Word")
        os.startfile("C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE")
    elif "excel" in text:
        speak("Mowr Excel")
        os.startfile("C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE")
    else:
        speak("Ứng dụng chưa được cài đặt. Hãy thử lại")

def open_website(text):
    reg_ex = re.search("mở (.+)", text)
    if reg_ex:
        domain = reg_ex.group(1)
        url = "https://www." + domain
        webbrowser.open(url)
        speak("Trang web bạn yêu cầu đã được mở")

        return  True
    else:
        return False

def open_google_and_search(text):
    search_for = text.split("kiếm", 1)[1]
    speak("okey!")
    driver = webdriver.ChromeOptions(path)
    driver.get("https://www.google.com")
    que = driver.find_element_by_path("//input[@name='q']")
    que.send_keys(str(search_for))
    que.send_keys(Keys.RETURN)
    