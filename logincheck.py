
#! /usr/bin/python3
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pickle

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
#chrome_options.add_argument('--disable-dev-shm-usage')
#chrome_options.add_argument("--remote-debugging-port=9222")
#chrome_options.add_argument('--headless')
#chrome_options.add_argument("--user-data-dir = chrome-data")
#chrome_options.binary_location = "/etc/chromium-browser"


driver = webdriver.Chrome(executable_path="/home/aayush/Webdriver/bin/chromedriver", options=chrome_options)

#chrome_options.add_argument("user-data-dir=/home/aayush/.config/google-chrome")
#driver.get("https://accounts.google.com/signin/v2/identifier?service=youtube&uilel=3&passive=true&continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Den-GB%26next%3D%252F&hl=en-GB&ec=65620&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
driver.get("https://youtube.com")
driver.find_element_by_xpath('//*[@id="buttons"]/ytd-button-renderer/a').click()
driver.implicitly_wait(10)
#driver.find_element_by_class_name("style-scope paper-button").click()
driver.find_element_by_id("identifierId").send_keys("upadhyayaayush12@gmail.com")


driver.find_element_by_id("identifierNext").click()
driver.find_element_by_xpath(r'//*[@id="password"]/div[1]/div/div[1]/input').send_keys("Aayush@8218716525")
driver.find_element_by_id("passwordNext").click()


time.sleep(10)


pickle.dump(driver.get_cookies(), open("cookies.pkl","wb"))

driver.quit()


"""
skipAd = driver.find_element_by_id("ad-text:s")

def skipAdFunction():
    threading.Timer(3,skipAdFunction).start()
    if(skipAd.is_enabled() or skipAd.is_displayed()):
        skipAd.click()


skipAdFunction()

"""
