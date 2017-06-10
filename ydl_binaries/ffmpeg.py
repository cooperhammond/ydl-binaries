from .utils import dl_progress, mark_executable
from os import path, makedirs
import sys
if sys.version_info[0] >= 3:
    from urllib.request import urlretrieve
else:
    from urllib import urlretrieve


def download_ffmpeg(location):
    if not location.endswith("/"):
        location += "/"

    location = path.expanduser(location)

    url = "https://github.com/kepoorhampond/ffmpeg-binaries/blob/master"

    platform_types = ["/linux/", "/win32/", "/darwin/"]

    for type in platform_types:
        if sys.platform.startswith(type.replace("/", "")):
            url += type
            files = [
                "ffmpeg",
                "ffprobe"
            ]
            if type == "win32":
                files = [x + ".exe" for x in files]
            for file in files:
                filename = location + file
                if not path.isfile(filename):

                    if not path.isdir(location):
                        makedirs(location)

                    print('Downloading "%s":' % file)

                    urlretrieve(url + file + "?raw=true", filename,
                                reporthook=dl_progress)
                    print("")
                    if type != "/win32/":
                        mark_executable(filename)
                else:
                    print('"%s" is already downloaded!' % file)


if __name__ == "__main__":
    download_ffmpeg()
