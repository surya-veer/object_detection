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
driver.implicitly_wait(30)
driver.set_window_position(1920,1080)
# driver.maximize_window()

#calling google image search
driver.get("https://www.google.co.in/search?tbs=sbi:AMhZZivr19K8Kxm_1jGPKihmA9oG6U55ciEjnQaCtRXTPJfeP07M-iCDwPzJaTfA_1vt1HKiYwyntTizyzB_1xDZkubJneur_1RSgWaXzas0xEc_1OL4KPHPxKJHC4JWwXC93x9-ctg0iiUdHMMjAOTnw1oTzKaDHULtD_1zQOVCULYQ3VK4H5F802gZcVXZab_1fVXbWUkm6bCCeYpKSBRkjadXWKqr_1HgppsyNnIftdNTm70ByX8WLtCYXpA9leG-iuO8Q3CMGmC-ZOcee8QptEu2wM-gF8k6J-L1qbfd4d2y-hLtGnkdI3iA-uguA-cYFfI26d64cI5MsButksAUUUym2cVvvWDrl_1HlWRLcljTSMtCczR0LKk26SP7jFXcfEhiA_1SmQVlGgzXedYpORuoU-sLp40MhHWQ8-VaX1Okj0lnsEi0Xfg_1j9XyCcF9oRhIlHLtlfhLVQ0u06xBnQzn1qPynytQg86qSgVv6mUkFVRcRwGXmD3991VdW5RVqihJZhR8JSYgQPoySQrKzBx5l5bvvXML0OxAEAdSWuTScJ9F2j6KuwGl4nHDGofkoSiHyHzJIzRI7Qf5BTxexOxnR56C8Wj6_15O3tMLDGSSneQzDYidrNBuxXdIEBuaYD2yMLYaY5JLy88ZLlZinmW_1JXwtH-ppHrM6V-UnRHn3Uz0uRl6AKbOL9SSFgYvQT5ZbG9natdy7bwACc9L5GpNFoC76Zx0hS5lo_13kgchwpWwBPeLa_1uXDyEycc_1uXtwYLM-3YetoNmpQntS69aRANNZpTkCQ3CwA4JLWSkN1lgefnmBSNmD2RvX_1bBxDVYp6muX5DIfNU23HdpbBeUOKQ8Tj_11vW8jPKZpfRKzEVU_1GF9DHPSyXdBfbiHQoGeumFidfy_1v8QGipSlYN0jyy1YSHad39VLz8bPuvlNIP31udGtzMl8LBWAsJiJMvco_1e0b7b8FrGYh3WPcdFrFKPUHh2AmqA2JF8kCPE1KKekFoOqpmw_18Ndbf_1oL2hDQPr_1vba4YZ1_1uMb-CZi7MKZUCnVDWmcPKNAtXtcgJQzkuYbJ9RKg8q19_1ryCD2dTGzNQzXWV6lHJ6wn_1iXnVw9lNBhu587QUH4wJ6xCq04ttOYVT3S2DW-P-SRVsYk0cWRmE9mcjsK72IaFOgYEIXC-GbmRNtRpErN8iHKLuaAD3HBSD5A7tJFssfzcatH4kgTsMbf9l_1l0c8bpKS7Hol_1iDJCi7HavIR7okP2SCHjtSYtdpXKDKK4AVRYTCNrG1V7Gi34JGrXOtaDVk0wGp9f5pLZ7dzkXEEMZgentoqmQwQOblQJZaIABj89ua6bzgh0L7nUosRLsinh4UtZv06kTWA2u0Kp74NwcnC-s03thCvXfPWC5LMmpi8-RD-rSIe-nUjcRw6Zn8CCH3fwqokwceppx9feNB3VGJnxDU3PjdAZb2HI5idwjCWwoVCbj8NJlDtrsR6qXn7ldXVt2tX9exndz5q1mvSVhAVfA34vHiDskjg6T_1YhYNR8WuMaX_1hhEdnXdCBQlNkSvsw6qG8QsKOCUli5jp2r5ygy_1AXhX5w3ABumriMtUSSD6u8kdeqeVxDPfYPxgTi5Qo-vMAwpgzsAU_1co1UA-Xq81QzLSmg&btnG=Search%20by%20image&hl=en-IN")

#taking Id of uplaod button
driver.find_element_by_id("qbi").click()

#putting image url on the image search
url=driver.find_element_by_name("image_url")
url.send_keys("http://fluxus.in//assets/images/website/navigation/temp/"+img)
url.submit()

#getting response from image search
get_obj = driver.find_element_by_class_name("_gUb").text

#voice output
engine = pyttsx.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-100)
engine.say("This seems like a "+get_obj+ ". Am i right?")
engine.runAndWait()

driver.quit()