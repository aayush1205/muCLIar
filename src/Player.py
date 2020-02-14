from ChromeDriver import CreateDriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

# TODO:

class Player():

    def __init__(self):
        self.actions = None
        self.driver = CreateDriver()
        self.driver.get("https://youtube.com")
        self.url = "https://youtube.com"


    def Search(self, song):
        """
        Search and play given song on YouTube.
        :param (str) song: Song name to be searched
        :return:
        """

        song = "+".join(song.split(' '))
        driver = self.driver
        driver.implicitly_wait(10)
        self.url = "https://www.youtube.com/results?search_query="+song
        driver.get(self.url)
        driver.maximize_window()
        driver.find_element_by_id("search-icon-legacy").click()
        driver.find_element_by_class_name(
            "style-scope ytd-video-renderer").click()
        self.GetPlaylist()

    def GetSongTitle(self):
        """
        Get currently playing song's title.
        :return (str): Current song title
        """

        info = self.driver.find_element_by_xpath(
            r'//*[@id="container"]/h1/yt-formatted-string').text
        return info

    def GetPlaylist(self):
        """
        Checks if there is any associated playlist for the current song.
        :return (dict): Next 5 songs from associated playlist else None
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
            next5[link] = title
        return next5


    def action(self, key_signal):
        """
        Control YouTube webplayer
        :param (str) key_signal: Key combination string
        :return:
        """

        self.actions = ActionChains(self.driver)
        self.actions.send_keys(key_signal)
        self.actions.perform()
        self.actions = None

    def Next(self):
        """
        Play next song
        :return:
        """
        key_signal = Keys.LEFT_SHIFT + 'N'
        self.action(key_signal)

    def Prev(self):
        """
        Play previous song
        :return:
        """
        key_signal = Keys.LEFT_SHIFT + 'P'
        self.action(key_signal)

    def PlayPause(self):
        """
        Toggle play state
        :return:
        """
        key_signal = 'k'
        self.action(key_signal)
