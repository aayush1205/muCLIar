from selenium import webdriver
import time
import os
import pickle
import sys
from selenium.webdriver.chrome.options import Options

class Search():

    def __init__(self, options, song):
        self.chrome = options
        self.song = song

    def search(self):
        options = self.chrome
        options.add_argument('--headless')
        driver = webdriver.Chrome(options=options)
        driver.implicitly_wait(10)
        driver.get("https://www.youtube.com")

        if os.path.isfile("cookies.pkl"):
            cookies = pickle.load(open("cookies.pkl", "rb"))
            for cookie in cookies:

                if 'expiry' in cookie:

                    del cookie['expiry']
                
                driver.add_cookie(cookie)

        
        driver.find_element_by_name("search_query").send_keys(f"{self.song}")
        driver.maximize_window()
        driver.find_element_by_id("search-icon-legacy").click()
        driver.find_element_by_class_name("style-scope ytd-video-renderer").click()
        driver.find_element_by_class_name("style-scope ytd-compact-radio-renderer").click()


        
        try:
            while True:
                continue
        except KeyboardInterrupt:
            driver.quit()
            print("\n")
            val = input("New song or quit? (enter n or q)")
            return self.quit(val)

    
    def quit(self, val):

        if val.lower() == "n":

            print("\n")
            new_song = input("Which Song: ")
            new_obj = Search(options = self.chrome, song = new_song)
            new_obj.search()

        elif val.lower() == "q":
            sys.exit()
        
        else:

            print("\n")
            new_val = input("Enter valid inpur (n or q): ")
            self.quit(new_val)
            








