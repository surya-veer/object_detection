# Build by Suryaveer
#Username: ayrusreev email:1998sveer@gmail.com
from ftplib import FTP #for ftp
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
import time
import pyttsx #for voice
import os

# connecting with the server
ftp = FTP('fluxus.in')
ftp.login(user="fluxusadmin", passwd = 'Kumarfluxus171')
ftp.cwd('public_html/assets/images/website/navigation/temp/')

# taking picture using streamer
img= str(time.time())+'.jpeg'
os.system('streamer -f jpeg -o '+img)

# uploading file on server
def placeFile():
    filename = img
    ftp.storbinary('STOR '+filename, open(filename, 'rb'))
    ftp.quit()
placeFile()

# Create a new instance of the chrome driver
driver = webdriver.Chrome("/media/ayrus/C06E98606E9850D0/Study/Linux/selenium/chromedriver")
# driver.implicitly_wait(30)
driver.set_window_position(1920,1080)
# driver.maximize_window()

#calling google image search
driver.get("****")
#taking Id of uplaod button
driver.find_element_by_id("qbi").click()

#putting image url on the image search
url=driver.find_element_by_name("image_url")
url.send_keys("http://fluxus.in//assets/images/website/navigation/temp/"+img)
url.submit()

#getting response from image search
get_obj = driver.find_element_by_class_name("_gUb").text

driver.quit()
#voice output
engine = pyttsx.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-100)
engine.say("This seems like a "+get_obj+ ". Am i right?")
engine.runAndWait()
