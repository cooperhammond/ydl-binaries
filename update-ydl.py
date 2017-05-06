from sys import platform
from sys import stdout
import os
import urllib
import stat
import subprocess


def check_ydl_version():
    if os.path.isdir("bin/"):
        try:
            local_version = subprocess.check_output("bin/youtube-dl --version"
                                                    .split(" ")).strip("\n")
        except OSError:
            return True

        remote_version = urllib.urlopen("https://youtube-dl.org/").read()
        remote_version = remote_version.rsplit('<a href="latest">Latest</a> (v'
                                               , 1)[1][:10]
        if local_version == remote_version:
            return False
    return True


def dlProgress(count, blocks, totalSize):
    stdout.write("\r %3d%%  (%3d / %d blocks)" %
                 (count * blocks * 100 / totalSize, count, totalSize / blocks))
    stdout.flush()


if check_ydl_version():
    windows = (platform == "win32")

    if not windows:
        url = ["https://yt-dl.org/downloads/latest", "youtube-dl"]
    else:
        url = ["https://yt-dl.org/latest", "youtube-dl.exe"]
    filename = "bin/" + url[1]

    if not os.path.isdir("bin/"):
        os.makedirs("bin/")

    print('Downloading "youtube-dl":')
    urllib.urlretrieve("/".join(url), filename, reporthook=dlProgress)

    if not windows:
        st = os.stat(filename)
        os.chmod(filename, os.stat(filename).st_mode | stat.S_IEXEC)
