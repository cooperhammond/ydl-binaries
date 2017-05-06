from sys import platform
from .utils import dl_progress, mark_executable
from os import path, makedirs
import urllib
import subprocess


def check_ydl_version(location):
    if path.isdir(location):
        try:
            local_version = subprocess.check_output(location + "youtube-dl \
--version".split(" ")).strip("\n")
        except OSError:
            return True

        remote_version = urllib.urlopen("https://youtube-dl.org/").read()
        remote_version = remote_version.rsplit('<a href="latest">\
Latest</a> (v', 1)[1][:10]
        if local_version == remote_version:
            return False
    return True


def update_ydl(location):
    location = path.expanduser(location)
    if check_ydl_version(location):
        windows = (platform == "win32")

        if not windows:
            url = ["https://yt-dl.org/downloads/latest", "youtube-dl"]
        else:
            url = ["https://yt-dl.org/latest", "youtube-dl.exe"]
        filename = location + url[1]

        if not path.isdir(location):
            makedirs(location)

        print('Downloading "youtube-dl":')
        urllib.urlretrieve("/".join(url), filename, reporthook=dl_progress)

        if not windows:
            mark_executable(filename)


if __name__ == "__main__":
    update_ydl()
