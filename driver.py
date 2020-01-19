from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import argparse
import socket
import getpass
import pickle
import time
import os
import main_auth
import main_search
flag = 0


chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
socket.setdefaulttimeout(100)
#executable_path= "/home/aayush/Webdriver/bin/chromedriver"
# driver.maximize_window()


class Musify(object):

    def __init__(self, args):
        self.args = args

    def __enter__(self):

        self.song = args.song
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if exc_type:
            print(exc_type, exc_value, exc_traceback)

    def search_song(self):
        songl = self.song

        if args.config:

            obj = main_auth.Authenticate(chrome_options)
            obj.auth()


        else:

            obj = main_search.Search(options= chrome_options,song=self.song)
            obj.search()

def parse_args():

    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--song', type=str,
                        help="Enter the song you wish to hear")
    parser.add_argument('-c', '--config', action='store_true')
    return parser.parse_args()


if __name__ == "__main__":

    args = parse_args()

    with Musify(args) as Mus:
        Mus.search_song()
