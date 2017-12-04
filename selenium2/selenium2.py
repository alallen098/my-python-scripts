import os
import time
from selenium import webdriver

drv = webdriver.Chrome()

time.sleep(1)
drv.get("http://google.com")
inp = drv.find_element_by_id("lst-ib")
inp.send_keys("abc")
inp.submit()
time.sleep(3)
drv.quit()

os.system("taskkill -f -im chromedriver.exe")


