from .utils import dl_progress, mark_executable
from sys import platform
from os import path, makedirs
import urllib


def download_ffmpeg():
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
                if not path.isdir("bin/"):
                    makedirs("bin/")
                print('Downloading "%s":' % file)
                urllib.urlretrieve(url + file + "?raw=true", filename,
                                   reporthook=dl_progress)
                print("")
                if type != "/win32/":
                    mark_executable(filename)


if __name__ == "__main__":
    download_ffmpeg()
