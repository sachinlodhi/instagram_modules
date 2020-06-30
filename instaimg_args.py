from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import urllib.request
import os
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import argparse

# Adding and parsing the requirements
ap = argparse.ArgumentParser()
ap.add_argument("-u", "--username", required = True,
                help ="username of instagram account")
ap.add_argument("-n", "--number", default=0,
                help = "number of pictures to be downloaded")
ap.add_argument("-s", "--stealth", default='y',
                help = "Run browser in hidden mode")
args = vars(ap.parse_args())
number_of_pics = args["number"]
print("[INFO] Starting...")

# Adding two options for launching browser instance
options = FirefoxOptions()
options.add_argument("--headless")
if args["stealth"] == 'y':
    driver = webdriver.Firefox(options=options)
elif args["stealth"] == 'n':
    driver = webdriver.Firefox()


target_usr=args["username"]

# getting to the user
driver.get('https:///www.instagram.com/'+target_usr)
driver.implicitly_wait(5)

if "Page Not Found" in driver.title:
    print("[ERROR] User is does NOT exist!!")
    exit(1)

if "This Account is Private" in driver.page_source:
    print("[ERROR] This is private account!!!")
    exit(1)

print("[INFO] User Found!!!")
SCROLL_PAUSE_TIME = 3
img_Link=[]
# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

#Looping till the end
while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    try:
        #print(len(img_Link))
        element = driver.find_elements(By.CLASS_NAME, 'FFVAD')
        for i in element:
            if str(i.get_attribute('src')) not in img_Link:
                #    print(i.get_attribute('src'))
                img_Link.append(str(i.get_attribute('src')))
    except:
        continue



    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
       break
    last_height = new_height
    print('[INFO] Working......')


# Saving the photos by fetching the from URL list
print(f'[INFO] Total Available Photos : {len(img_Link)}')
os.mkdir(target_usr)
if args["number"] == "0":
    number_of_pics = len(img_Link)

img_Num=1
for i in img_Link:
 urllib.request.urlretrieve(i,target_usr+"/pic_"+str(img_Num)+".jpeg")
 print(f'[INFO] Total Pics Saved : {img_Num} of {number_of_pics}.')
 if str(img_Num) == args["number"]:
     break
 img_Num+=1

print(f"[SUCEESS] Job Done. Total {img_Num} photos have been saved.")
