
#! /usr/bin/python3
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pickle

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')


driver = webdriver.Chrome(executable_path="/home/aayush/Webdriver/bin/chromedriver", options=chrome_options)
driver.get("https://youtube.com")
driver.find_element_by_xpath('//*[@id="buttons"]/ytd-button-renderer/a').click()
driver.implicitly_wait(10)
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
