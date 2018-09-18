from .utils import dl_progress, mark_executable
from os import path, makedirs
import subprocess
import sys
if sys.version_info[0] >= 3:
    from urllib.request import urlretrieve, urlopen
else:
    from urllib import urlretrieve, urlopen


def update_ydl(location):
    if not location.endswith("/"):
        location += "/"

    location = path.expanduser(location)

    windows = (sys.platform == "win32")

    if not windows:
        url = ["https://yt-dl.org/downloads/latest", "youtube-dl"]
    else:
        url = ["https://yt-dl.org/latest", "youtube-dl.exe"]
    filename = location + url[1]

    if not path.isdir(location):
        makedirs(location)

    print('Downloading "youtube-dl":')
    urlretrieve("/".join(url), filename, reporthook=dl_progress)

    if not windows:
        mark_executable(filename)


if __name__ == "__main__":
    update_ydl()
