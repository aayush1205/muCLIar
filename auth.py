import getpass
from selenium import webdriver
import pickle
import time
import sys

class Auth():

    def __init__(self, query, driver):
        self.query = query
        self.driver = driver

    def auth_and_search(self,query):

        driver = self.driver


        self.auth_func()
        time.sleep(5)
        url = driver.current_url
        print(url)
        if url == "https://www.youtube.com/":
            print("Logged in sucessfully!")
            time.sleep(5)
            pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))
            
        else:
            print("Login Unsucessful! Enter correct credentials!")
            self.auth_func()


        if query is None:
            time.sleep(5)
            driver.quit()
            time.sleep(10)
            sys.exit()

        else:

            driver.find_element_by_name("search_query").send_keys(f"{query}")
            driver.find_element_by_id("search-icon-legacy").click()
            driver.find_element_byy_class_name("style-scope ytd-video-renderer").click()
            driver.find_element_by_class_name("yt-simple-endpoint style-scope ytd-compact-radio-renderer").click()

    def auth_func(self):

        driver = self.driver

        driver.get("https://youtube.com")
        usname = input("Enter email: ")
        passw = getpass.getpass(prompt="Enter Password: ")
        driver.find_element_by_xpath('//*[@id="buttons"]/ytd-button-renderer/a').click()
        driver.implicitly_wait(10)
        driver.find_element_by_id("identifierId").send_keys(f"{usname}")
        driver.find_element_by_id("identifierNext").click()
        driver.find_element_by_xpath(r'//*[@id="password"]/div[1]/div/div[1]/input').send_keys(f"{passw}")
        driver.find_element_by_id("passwordNext").click()

    
