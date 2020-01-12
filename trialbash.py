from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import argparse
import socket

flag = 0


chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
socket.setdefaulttimeout(100)
#options.binary_location = "/usr/bin/google-chrome"

driver = webdriver.Chrome(
    executable_path="/home/aayush/Webdriver/bin/chromedriver", options=chrome_options)
driver.implicitly_wait(10)
driver.maximize_window()


class Musify(object):

    def __init__(self, args):
        self.args = args

    def __enter__(self):

        self.song = ' '.join(args.QUERY)

        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if exc_type:
            print(exc_type, exc_value, exc_traceback)

    def search_song(self):
        songl = self.song

        driver.get("https://youtube.com")
        driver.find_element_by_name("search_query").send_keys(f"{songl}")
        driver.find_element_by_id("search-icon-legacy").click()
        driver.find_element_by_class_name(
            "style-scope ytd-video-renderer").click()

        try:

            while True:
                continue

        except KeyboardInterrupt:

            print("\n")
            driver.quit()

            val = input("New song or quit? (enter n or q): ")

            self.quit(val)

    def quit1(self, t1):

        print("\n")

        val = input("New song or quit? (enter n or q): ")

        return self.quit(val, flag=0)

    def quit(self, ff, flag=0):

        if(ff == "n"):

            print("\n")

            new = input("Which song? ")

            drivern = webdriver.Chrome(
                executable_path="/home/aayush/Webdriver/bin/chromedriver", options=chrome_options)

            drivern.get("https://youtube.com")
            drivern.find_element_by_name("search_query").send_keys(f"{new}")
            drivern.find_element_by_id("search-icon-legacy").click()
            drivern.find_element_by_class_name(
                "style-scope ytd-video-renderer").click()

            try:
                while True:
                    continue

            except KeyboardInterrupt:
                print("\n")
                drivern.quit()
                val = input("New song or quit? (enter n or q): ")

                self.quit(val, flag=1)

        elif(ff == "q"):

            if(flag == 0):
                driver.quit()
            else:
                drivern.quit()

        else:
            print("\n")
            print("Enter valid input: ")
            return self.quit1(10)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("QUERY", type=str, nargs='+')

    return parser.parse_args()


if __name__ == "__main__":

    args = parse_args()

    with Musify(args) as Mus:
        Mus.search_song()
