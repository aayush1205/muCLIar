from ChromeDriver import CreateDriver


# TODO:
# Issues from author's repo:
# Get playlist
# Pause/Play, Previous, Next controls


class Player():

    def __init__(self):
        self.driver = CreateDriver()
        self.driver.get("https://youtube.com")

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
        driver.get("https://www.youtube.com/results?search_query="+song)
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
        """

        try:
            self.driver.find_element_by_class_name(
                "style-scope ytd-compact-radio-renderer").click()
        except:
            print("Might not be a song!! No associated playlist!!")

    def Next(self):
        pass

    def Prev(self):
        pass

    def Play(self):
        pass

    def Pause(self):
        pass
