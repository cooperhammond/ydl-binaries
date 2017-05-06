from sys import platform
from sys import stdout
import os
import urllib
import stat


def dlProgress(count, blocks, totalSize):
    stdout.write("\r %3d%%  (%4d / %d pieces)" %
                 (count * blocks * 100 / totalSize, count, totalSize / blocks))
    stdout.flush()


url = "https://github.com/kepoorhampond/ffmpeg-binaries/blob/master"

platform_types = ["/linux/", "/win32/", "/darwin/"]

for type in platform_types:
    if platform.startswith(type.replace("/", "")):
        url += type
        files = [
            "ffmpeg",
            "ffprobe"
        ]
        if type == "win32":
            files = [x + ".exe" for x in files]
        for file in files:
            filename = "bin/" + file
            if not os.path.isdir("bin/"):
                os.makedirs("bin/")
            print('Downloading "%s":' % file)
            urllib.urlretrieve(url + file + "?raw=true", filename,
                               reporthook=dlProgress)
            print("")
            if type != "/win32/":
                st = os.stat(filename)
                os.chmod(filename, os.stat(filename).st_mode | stat.S_IEXEC)
