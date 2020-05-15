from Player import Player
from getkey import getkey, keys
import sys
from itertools import cycle
from time import sleep
import threading
import argparse
from colorama import Fore

CURSOR_UP_ONE = '\x1b[1A'
ERASE_LINE = '\x1b[2K'
QUIT_SEARCH = False
QUIT_DISPLAY = False
LINE_BUFFER = 0

# Launches chrome with YouTube landing page
yt_music = Player()


def delete_lines(n=1):
	for _ in range(n):
		sys.stdout.write(CURSOR_UP_ONE)
		sys.stdout.write(ERASE_LINE)


def search_animation():
	for _ in cycle(['|', '/', '-', '\\']):
		if QUIT_SEARCH:
			sys.stdout.write('\r\033[K')
			sys.stdout.flush()
			return
		print(Fore.LIGHTCYAN_EX +  '\rSearching ' + _, end='\r'+ Fore.RESET)
		sleep(0.1)


def display_info():
	new_title = 'Idle'

	while True:
		if QUIT_DISPLAY:
			return

		try:
			title = yt_music.get_song_title()
		except:
			title = 'Idle'

		if new_title == title:
			continue
		else:
			global LINE_BUFFER
			delete_lines(LINE_BUFFER)
			LINE_BUFFER = 13

			try:
				sleep(5)
				has_playlist = yt_music.get_playlist()
				if not has_playlist:
					playlist = 'No playlist associated with this song.'
					LINE_BUFFER -= 4
				else:
					playlist = '\n'.join([track for track in has_playlist.values()])
			except:
				playlist = 'Idle'
				LINE_BUFFER -= 4

			controls = "New song: s\tPause: o\tNext song: p\tPrev song: i\tQuit: q\nSeek 5 seconds: ←/→\t" \
					   "Volume: ↑/↓\tMute: m\n " 

			print((Fore.LIGHTCYAN_EX + f'Now Playing: {Fore.WHITE + title + Fore.RESET}\n\n'+ Fore.RESET) + (Fore.LIGHTCYAN_EX + f'Playlist:\n{Fore.WHITE + playlist + Fore.RESET}\n\n'+ Fore.RESET) + (Fore.LIGHTCYAN_EX + f'Controls:\n{Fore.WHITE + controls + Fore.RESET}\r' + Fore.RESET))

			new_title = title
			sleep(0.1)


def parse_args():
	"""
	Parse muCLIar args
	:return:
	"""
	parser = argparse.ArgumentParser(description='muCLIar - Music from CLI')
	parser.add_argument('-s', '--song', type=str, help='Song name', required=True)
	parser.add_argument('-c', '--config', action='store_true')

	return parser.parse_args()


def application(args):
	"""
	Event loop for Player
	:param args: Arguments from command line: song name (required), config (optional)
	:return:
	"""
	if args.config:
		res = yt_music.auth()
		if res == 0:
			print('Using stored credentials.')
		else:
			print('Logged in.')

	inf = threading.Thread(target=display_info)
	inf.start()
	global QUIT_SEARCH
	QUIT_SEARCH = False
	anim = threading.Thread(target=search_animation)
	anim.start()
	QUIT_SEARCH = yt_music.search(song=args.song)
	anim.join()

	key = ''

	while key != 'q':
		key = getkey()

		if key == 's':
			song = input(Fore.WHITE + 'Search new song: ' + Fore.RESET)
			delete_lines(1)			
			QUIT_SEARCH = False
			anim = threading.Thread(target=search_animation)
			anim.start()
			QUIT_SEARCH = yt_music.search(song=song)
			anim.join()

		if key == 'i':
			yt_music.prev()

		elif key == 'o':
			yt_music.play_pause()

		elif key == 'p':
			yt_music.next()

		elif key == 'm':
			yt_music.mute()

		elif key == keys.LEFT:
			yt_music.backward()

		elif key == keys.RIGHT:
			yt_music.forward()

		elif key == keys.UP:
			yt_music.volume_up()

		elif key == keys.DOWN:
			yt_music.volume_down()

		elif key == 'q':
			global QUIT_DISPLAY
			QUIT_DISPLAY = True
			delete_lines(LINE_BUFFER)
			yt_music.quit()


if __name__ == "__main__":

	arguments = parse_args()

	application(arguments)
