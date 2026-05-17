import subprocess
import sys

vlcPath = r"C:\Program Files\VideoLAN\VLC"

def open_link(link):
    link = link.strip()
    if link:
        subprocess.run([vlcPath + r"\vlc.exe", link])