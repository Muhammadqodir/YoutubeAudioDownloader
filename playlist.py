from __future__ import unicode_literals
from pytube import Playlist
import youtube_dl


ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

playlist = Playlist('https://www.youtube.com/playlist?list=PLD6SPjEPomatGZyaYOV1SOzS0MpIjc2oV')

print(len(playlist))

for x in range(250, 300):
	print(playlist[x])
	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
		ydl.download(['https://www.youtube.com/watch?v=9PZ0NP6Jl5I'])
	pass