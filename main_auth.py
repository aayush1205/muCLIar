from selenium import webdriver
import time
import pickle


class Authenticate():

    def __init__(self,options):

        self.chrome = options



    def auth(self):

        options = self.chrome
        driver = webdriver.Chrome(options = options)
        driver.get("https://youtube.com")
        driver.find_element_by_xpath(r'//*[@id="buttons"]/ytd-button-renderer/a').click()

        while(driver.current_url != "https://www.youtube.com/"):
            continue
        
        print("Logged In Successfully!")
        time.sleep(2)
        pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))

        driver.quit()






