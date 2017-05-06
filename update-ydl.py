from sys import platform
from sys import stdout
import os
import urllib
import stat

windows = (platform == "win32")


def dlProgress(count, blocks, totalSize):
    stdout.write("\r %2d%%  (%3d / %d blocks)" %
                 (count * blocks * 100 / totalSize, count, totalSize / blocks))
    stdout.flush()


if not windows:
    url = ["https://yt-dl.org/downloads/latest", "youtube-dl"]
else:
    url = ["https://yt-dl.org/latest", "youtube-dl.exe"]

urllib.urlretrieve("/".join(url), url[1], reporthook=dlProgress)

if not windows:
    st = os.stat(url[1])
    os.chmod(url[1], os.stat(url[1]).st_mode | stat.S_IEXEC)
