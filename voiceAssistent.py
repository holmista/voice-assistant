from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime
import time

youtube = False
# start_time = datetime.now()
PATH = r"C:\Program Files (x86)\chromedriver.exe"
# youtube = False
driver = webdriver.Chrome(PATH)
driver.get('https://facebook.com')
import speech_recognition as sr
listener = sr.Recognizer()
try:
    with sr.Microphone() as source:
        print('listening...')
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        if command == 'YouTube':
            driver.get('https://youtube.com')
            
        print(command)
        time.sleep(10)
except:
    pass

if youtube:
    pass

    