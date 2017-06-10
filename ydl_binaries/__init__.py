import argparse
from .utils import drop_root_privilege
from .ffmpeg import download_ffmpeg
from .ydl import update_ydl

drop_root_privilege()


def main():
    parser = argparse.ArgumentParser(
        description="Cross-platform binaries for youtube-dl and ffmpeg"
    )

    parser.add_argument(
        "-f",    "--ffmpeg",
        dest   = "ffmpeg",
        action = "store_true",
        help   = "download ffmpeg binaries"
    )

    parser.add_argument(
        "-y",    "--youtube-dl",
        dest   = "ydl",
        action = "store_true",
        help   = "download/update youtube-dl binary"
    )

    parser.add_argument(
        "-l", "--location",
        dest    = "location",
        default = "bin/",
        help    = 'where to put downloaded files. defaults to \"bin/" ' +
        'in the working directory.',
        type    = str
    )

    args = parser.parse_args()

    if not args.location.endswith("/"):
        args.location += "/"

    if args.ffmpeg:
        download_ffmpeg(args.location)

    if args.ydl:
        update_ydl(args.location)
