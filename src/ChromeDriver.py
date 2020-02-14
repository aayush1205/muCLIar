import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def create_driver():
    """
    Create a webdriver instance of Chrome
    :return: Chrome driver instance
    """

    options = Options()
    # options.add_argument('headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_extension(os.path.dirname(os.path.abspath(__file__))+"/skipper_crx3.crx")

    return webdriver.Chrome(options=options)
