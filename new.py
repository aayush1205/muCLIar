from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
import pickle

chrome_options = Options()
#chrome_options.add_argument("user-data-dir=/home/aayush/.config/google-chrome/Default")
driver = webdriver.Chrome(executable_path = "/home/aayush/Webdriver/bin/chromedriver", options = chrome_options)

driver.get("https://youtube.com")

time.sleep(10)


cookies = pickle.load(open("cookies.pkl", "rb"))
for cookie in cookies:

    if 'expiry' in cookie:
        del cookie['expiry']
    

    driver.add_cookie(cookie)
    


    

