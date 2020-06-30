import threading
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
import list_read as lr
import os.path
from os import path



driver = 0 # making global variable to access browser instance in all funcitons

# launching the instance in the very beginning using the thread
def launch():
    global driver
    options = FirefoxOptions()
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)
    #print("[INFO] Browser instance opened")

#funciton if only one user is targeted
def single_usr(usrname):
    usrname = str(usrname).strip()
    main_process(usrname)


# main process to scrap data
def main_process(target_usr):
    global driver

    driver.get('https:///www.instagram.com/' + target_usr)
    driver.implicitly_wait(5)

    if "Page Not Found" in driver.title:
        print(f"[ERROR] User does NOT exist : {target_usr}")
        return None
        #exit(1)

    if "This Account is Private" in driver.page_source:
        print(f"[ERROR] This is private account : {target_usr}")
        #exit(1)
        return None
    print(f"[INFO] User Found : {target_usr}")
    SCROLL_PAUSE_TIME = 3
    img_Link = []
    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    # Looping till the end
    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        try:
            # print(len(img_Link))
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
    #if 0 == "0":
    number_of_pics = len(img_Link)

    img_Num = 1
    for i in img_Link:
        urllib.request.urlretrieve(i, target_usr + "/pic_" + str(img_Num) + ".jpeg")
        print(f'[INFO] Total Pics Saved : {img_Num} of {number_of_pics}.')
        #if str(img_Num) == args["number"]:
        #break
        img_Num += 1

    print(f"[SUCEESS] Job Done.\nTotal {img_Num-1} photos have been saved.")
    print("##################################################################\n")




if __name__ == '__main__':
    t1= threading.Thread(target=launch, name ="t1") # launched the browser instance in starting using threading
    t1.start()
    print("1. Single user\n2. In BULK")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        usrname = input("Enter the username : ")
        single_usr(usrname)
    elif choice == 2:
        filepath = input("Please enter the path of the csv file containing usernames : ")
        if path.exists(str(filepath)):
            print("[INFO] File Exist")
            userlist = lr.pre_Process(str(filepath))
            for i in userlist:
                main_process(i)
        else:
            print("[ERROR] Either file does not exist or wrong filepath.")
    driver.close()
    print(f"[STOP] Completed")







