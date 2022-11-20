from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import datetime, time
import os
import subprocess

import Xlib.display
os.environ['DISPLAY'] = ":0"
# os.environ['XAUTHORITY']='/run/user/1000/gdm/Xauthority'
print(os.environ['DISPLAY'])

display = Display(visible=0, size=(1920, 1080))
display.start()

import pyautogui

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-dev-shm-usage')
browser = webdriver.Chrome('chromedriver', options=chrome_options)
browser.set_window_size(1920, 1080)
# browser.get('chrome://settings/')
# browser.execute_script('chrome.settingsPrivate.setDefaultZoom(1.5);')
browser.get('https://github.com/asweigart/pyautogui/blob/master/pyautogui/_pyautogui_x11.py')
browser.execute_script("document.body.style.zoom='150%'")

print(browser.title)

screenshot = pyautogui.screenshot()
screenshot.save(f"ss_before_1.png")

#time.sleep(45)

screenshot = pyautogui.screenshot()
screenshot.save(f"ss_after_1.png")

# To save Screenshot to S3
subprocess.run(f"aws s3 cp ss_after_1.png s3://cp-patient-datastore/rough_work/headless_chrome/ss_before_1.png", shell=True)
subprocess.run(f"aws s3 cp ss_before_1.png s3://cp-patient-datastore/rough_work/headless_chrome/ss_after_1.png", shell=True)

browser.quit()

display.stop()
