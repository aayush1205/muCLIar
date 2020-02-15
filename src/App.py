from Player import Player
from getkey import getkey, keys
import sys
from itertools import cycle
from time import sleep
import threading

CURSOR_UP_ONE = '\x1b[1A'
ERASE_LINE = '\x1b[2K'
QUIT_SEARCH = False
LINE_BUFFER = 0


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
		print('\rSearching ' + _, end='\r')
		sleep(0.1)


def display_info():
	global LINE_BUFFER
	delete_lines(LINE_BUFFER)
	LINE_BUFFER = 13

	title = yt_music.get_song_title()

	has_playlist = yt_music.get_playlist()

	if not has_playlist:
		playlist = 'No playlist associated with this song.'
		LINE_BUFFER -= 4
	else:
		playlist = '\n'.join([track for track in has_playlist.values()])

	controls = "New song: s\tPause: o\tNext song: p\tPrev song: i\tQuit: q\nSeek 5 seconds: ←/→\t" \
			   "Volume: ↑/↓\tMute: m\n "

	print('Now Playing: {}\n\nPlaylist:\n{}\n\nControls:\n{}\r'.format(title, playlist, controls))


# Launches chrome with YouTube landing page
yt_music = Player()

key = ''

while key != 'q':
	key = getkey()

	if key == 's':
		song = input('Search new song: ')
		delete_lines(1)

		QUIT_SEARCH = False
		anim = threading.Thread(target=search_animation)
		anim.start()
		QUIT_SEARCH = yt_music.search(song=song)
		anim.join()

		display_info()

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
		delete_lines(LINE_BUFFER)
		yt_music.quit()
