from selenium import webdriver
import time
import os
import pickle
import sys
from colorama import Fore
from selenium.webdriver.chrome.options import Options
import itertools
from selenium.webdriver.common.by import By
import threading
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from pyvirtualdisplay import Display


class Search():

    def __init__(self, options, song):
        self.chrome = options
        self.song = song
        self.done = False
        self.hasAd = False

    def search(self):

        try:
            time.sleep(5)
            done = self.done
            t = threading.Thread(target=self.animate)
            t.start()
            options = self.chrome
            # options.add_argument('--headless')
            display = Display(visible=0, size=(1080, 1920))
            display.start()
            driver = webdriver.Chrome(options=options)
            time.sleep(10)
            driver.implicitly_wait(10)
            driver.get("https://www.youtube.com")

            if os.path.isfile("cookies.pkl"):

                cookies = pickle.load(open("cookies.pkl", "rb"))

                for cookie in cookies:

                    if 'expiry' in cookie:

                        del cookie['expiry']

                    driver.add_cookie(cookie)

            driver.find_element_by_name(
                "search_query").send_keys(f"{self.song}")
            driver.maximize_window()
            driver.find_element_by_id("search-icon-legacy").click()
            self.done = True
            print("\n")
            driver.find_element_by_class_name(
                "style-scope ytd-video-renderer").click()
            time.sleep(4)
            try:
                driver.find_element_by_class_name(
                    "style-scope ytd-compact-radio-renderer").click()
            except:
                print("Might not be a song!! No associated playlist!!")

            # info = driver.find_element_by_class_name("style-scope ytd-video-primary-info-renderer").text
            info = driver.find_element_by_xpath(
                r'//*[@id="container"]/h1/yt-formatted-string').text
            print(Fore.LIGHTRED_EX +
                  f"Now Playing: {Fore.LIGHTCYAN_EX + str(info)}")

            try:

                while True:

                    info2 = driver.find_element_by_xpath(
                        r'//*[@id="container"]/h1/yt-formatted-string').text
                    if(info2 != info):
                        print(Fore.LIGHTRED_EX +
                              f"\nNow Playing: {Fore.LIGHTCYAN_EX + str(info2)}")
                        info = info2
                        continue
                    else:
                        continue

            except KeyboardInterrupt:
                # driver.find_element_by_id("movie_player").click()
                driver.quit()
                display.stop()
                print("\n")
                val = input(Fore.LIGHTRED_EX +
                            "New song or quit? (enter n or q): ")
                return self.quit(val)

        except KeyboardInterrupt:

            self.done = True
            print("\n")

            print(
                Fore.BLUE + "Interrupted before call completion. Exiting..." + Fore.RESET)
            # sys.exit(1)
            os._exit(1)

    def animate(self):

        for c in itertools.cycle(['|', '/', '-', '\\']):
            if self.done:
                break
            sys.stdout.write(Fore.LIGHTMAGENTA_EX +
                             '\rSearching for your song ' + c + Fore.RESET)
            sys.stdout.flush()
            time.sleep(0.1)

        # sys.stdout.write('\rDone!\n')

    def quit(self, val):

        if val.lower() == "n":

            # display.stop()
            print("\n")
            new_song = input("Which Song: ")
            new_obj = Search(options=self.chrome, song=new_song)
            new_obj.search()

        elif val.lower() == "q":
            print(Fore.WHITE + "\nQuitting...")
            # display.stop()
            os._exit(1)

        else:

            print("\n")
            new_val = input(Fore.LIGHTBLUE_EX + "Enter valid inpur (n or q): ")
            self.quit(new_val)
