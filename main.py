from __future__ import unicode_literals
import youtube_dl


ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=9PZ0NP6Jl5I&ab_channel=%D0%90%D0%9D%D0%93%D0%9B%D0%98%D0%99%D0%A1%D0%9A%D0%98%D0%99%D0%AF%D0%97%D0%AB%D0%9A%D0%9F%D0%9E%D0%9F%D0%9B%D0%95%D0%99%D0%9B%D0%98%D0%A1%D0%A2%D0%90%D0%9C'])
