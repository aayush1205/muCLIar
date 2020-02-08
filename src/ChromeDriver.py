from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

import os


def CreateDriver():
    """
    Create a webdriver instance of Chrome
    Args: None

    Returns:
        Chrome driver instance
    """

    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_extension(os.path.dirname(
        os.path.abspath(__file__))+"/skipper_crx3.crx")

    return webdriver.Chrome(options=options)
