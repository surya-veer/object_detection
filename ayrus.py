#By: Suryaveer from IIT INDORE
#Username: ayrusreev 
#Email:1998sveer@gmail.com
#GitHub : http://github.com/surya-veer


from ftplib import FTP #for ftp
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
import time
import pyttsx #for voice
import os
import speech_recognition as sr #for voice to text
import difflib

r = sr.Recognizer()
com = ''
while difflib.SequenceMatcher(None,"capture this",com).ratio()<.7:
	with sr.Microphone() as source:
	    print("Say something!")
	    audio = r.listen(source)
	    com = r.recognize_google(audio)

	 
	# Speech recognition using Google Speech Recognition
	try:
	    print("You said: " + r.recognize_google(audio))
	except sr.UnknownValueError:
	    print("Google Speech Recognition could not understand audio")
	except sr.RequestError as e:
	    print("Could not request results from Google Speech Recognition service; {0}".format(e))

# connecting with the server
ftp = FTP('******')
ftp.login(user="******", passwd = '******')
ftp.cwd('public_html/assets/images/******')

engine = pyttsx.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-100)
# engine.say("Ok capturing.")
# engine.runAndWait()

# taking picture using streamer
img= str(time.time())+'.jpeg'
os.system('streamer -f jpeg -o '+img)

# uploading file on server
def placeFile():
    filename = img
    ftp.storbinary('STOR '+filename, open(filename, 'rb'))
    ftp.quit()
placeFile()

# # Create a new instance of the chrome driver
driver = webdriver.Chrome("/media/ayrus/C06E98606E9850D0/Study/Linux/selenium/chromedriver")

# driver.implicitly_wait(30)
#driver.set_window_position(1920,1080)
# driver.maximize_window()

# #calling google image search
driver.get("https://www.google.com/search?site=&tbm=isch&source=hp&biw=1311&bih=676&q=linkin+park&oq=link&gs_l=img.3.2.0l10.5333.11936.0.13878.9.8.1.0.0.0.187.1002.0j6.6.0....0...1ac.1.64.img..2.7.1004.0..35i39k1.kbzghZ4pSPw")

#taking Id of uplaod button
driver.find_element_by_id("qbi").click()

# #putting image url on the image search
url=driver.find_element_by_name("image_url")
url.send_keys("http://fluxus.in//assets/images/website/navigation/temp/"+img)
url.submit()

# #getting response from image search
get_obj = driver.find_element_by_class_name("_gUb").text

print(get_obj)

#driver.quit()
#voice output

engine1 = pyttsx.init()
rate = engine1.getProperty('rate')
engine1.setProperty('rate', rate-100)
engine1.say("This seems like a "+get_obj+ ". Am i right?")
engine1.runAndWait()

while difflib.SequenceMatcher(None,"No you are not right",com).ratio()<.6:
	with sr.Microphone() as source:
	    print("Say something!")
	    audio = r.listen(source)
	    com = r.recognize_google(audio)

	 
	# Speech recognition using Google Speech Recognition
	try
	    print("You said: " + r.recognize_google(audio))
	except sr.UnknownValueError:
	    print("Google Speech Recognition could not understand audio")
	except sr.RequestError as e:
	    print("Could not request results from Google Speech Recognition service; {0}".format(e))

engine1.say("Let me check for another one!")
# engine1.runAndWait()
