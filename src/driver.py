from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import argparse
import socket
import time
import os
import main_auth
import main_search

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_extension(os.path.dirname(os.path.abspath(__file__))+"/skipper_crx3.crx")
socket.setdefaulttimeout(100)



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

            try:                
                obj = main_search.Search(options= chrome_options,song=self.song)
                obj.search()
            except KeyboardInterrupt:
                os._exit(1)




def parse_args():

    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()

    group.add_argument('-s', '--song', type=str,
                        help="Enter the song you wish to hear")
    group.add_argument('-c', '--config', action='store_true')
    return parser.parse_args()


if __name__ == "__main__":

    args = parse_args()

    with Musify(args) as Mus:
        Mus.search_song()
