import getpass
from selenium import webdriver
import pickle
import time
import sys
import trialsplit


class Auth():

    def __init__(self, query):
        self.query = query
        #self.driver = driver

    def auth_and_search(self, query , driver):

        query = query
        url = self.auth_func(driver)
        time.sleep(5)

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
            driver.find_element_by_class_name(
                "style-scope ytd-video-renderer").click()
            driver.find_element_by_class_name(
                "style-scope ytd-compact-radio-renderer").click()

            try:

                while True:
                    continue
            except KeyboardInterrupt:
                print("\n")
                val = input("New song or quit? (enter n or q): ")
                trialsplit.Musify.quit1(t1=val)

    def auth_func(self,driver):

        

        driver.get("https://youtube.com")
        usname = input("Enter email: ")
        passw = getpass.getpass(prompt="Enter Password: ")
        driver.find_element_by_xpath(
            '//*[@id="buttons"]/ytd-button-renderer/a').click()
        driver.implicitly_wait(10)
        driver.find_element_by_xpath(
            r'//*[@id="Email"]').send_keys(f"{usname}")
        driver.find_element_by_xpath(r'//*[@id="next"]').click()
        driver.find_element_by_xpath(
            r'//*[@id="Passwd"]').send_keys(f"{passw}")
        driver.find_element_by_id(r'//*[@id="signIn"]').click()

        return driver.current_url
