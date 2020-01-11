from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import argparse

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
#options.binary_location = "/usr/bin/google-chrome"

driver = webdriver.Chrome(
    executable_path="/home/aayush/Webdriver/bin/chromedriver", chrome_options=chrome_options)
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


            quit1()
    

    def quit1():


            print("\n")

            val = input("New song or quit? (enter n or q): ")

            self.quit(self, ff = val)




    def quit(self, ff= None):

        if( ff == "n"):

            print("\n")
            
            new = input("Which song? ")

            search_song(self, new)




        elif(ff == "q"):
            pass
        else:
            print("\n")
            print("Enter valid input: ")
            quit1()



"""
driver.get("https://youtube.com")
driver.find_element_by_name("search_query").send_keys(f"{songl}")
driver.find_element_by_id("search-icon-legacy").click()

driver.find_element_by_class_name("style-scope ytd-video-renderer").click()



try:

    while True:
        continue

except KeyboardInterrupt:

    driver.quit()


    """


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("QUERY", type=str, nargs='+')

    return parser.parse_args()


if __name__ == "__main__":

    args = parse_args()

    with Musify(args) as Mus:
        Mus.search_song()
