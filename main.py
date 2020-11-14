import pytube
import os
import colorama
from pathlib import Path
import webbrowser
import hashlib
import httpx
from colorama import Fore, init

os.system("title YouTube Downloader - ShahriarXD")



url = input("Enter the video url")
print("\nDownloading, please hold and do not close this window!")

video = pytube.YouTube(url)
youtube = video.streams.first()
youtube.download()

print("\n\nDowload Completed!")
