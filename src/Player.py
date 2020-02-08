from ChromeDriver import CreateDriver
from bs4 import BeautifulSoup as bs
import requests

# TODO:
# Issues from author's repo:
# Get playlist
# Pause/Play, Previous, Next controls


class Player():

    def __init__(self):
        self.driver = CreateDriver()
        self.driver.get("https://youtube.com")
        self.url = "https://youtube.com"

    
    def ParsePage(self):
        r = requests.get(self.url)
        return bs(r, 'html5lib')

    def Search(self, song):
        """
        Search and play given song on YouTube.

        Args:
            song (str): Song name to be searched

        Returns: None
        """

        song = "+".join(song.split(' '))
        driver = self.driver
        driver.implicitly_wait(10)
        self.url = "https://www.youtube.com/results?search_query="+song
        driver.get(self.url)
        driver.maximize_window()
        driver.find_element_by_id("search-icon-legacy").click()
        print("\n")
        driver.find_element_by_class_name(
            "style-scope ytd-video-renderer").click()
        self.GetPlaylist()

    def GetSongTitle(self):
        """
        Get currently playing song's title.

        Returns:
            str: Current song title
        """

        info = self.driver.find_element_by_xpath(
            r'//*[@id="container"]/h1/yt-formatted-string').text
        return info

    def GetPlaylist(self):
        """
        Checks if there is any associated playlist for the current song.

        Returns:
            dict: Next 5 songs from associated playlist else None
        """

        try:
            self.driver.find_element_by_class_name(
                "style-scope ytd-compact-radio-renderer").click()
        except:
            print("Might not be a song!! No associated playlist!!")
            return None
        next5 = {}
        for i in range(2,7):
            link = self.driver.find_element_by_xpath(
                r'/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[2]/div/ytd-playlist-panel-renderer/div/div[2]/ytd-playlist-panel-video-renderer['
                +str(i)+r']/a').get_attribute('href')
            title = self.driver.find_element_by_xpath(
                r'/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[2]/div/ytd-playlist-panel-renderer/div/div[2]/ytd-playlist-panel-video-renderer['
                +str(i)+r']/a/div/div[2]/h4/span').text
            next5[link]=title
        return next5

    def Next(self):
        pass

    def Prev(self):
        pass

    def Play(self):
        pass

    def Pause(self):
        pass
