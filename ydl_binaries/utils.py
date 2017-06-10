from sys import stdout
import os
import stat


# Hook to display progress of downloads.
def dl_progress(count, blocks, totalSize):
    stdout.write("\r %3d%%  (%4d / %d pieces)"
                 % (count * blocks * 100 / totalSize, count,
                    (totalSize / blocks) + 1))
    stdout.flush()


def drop_root_privilege():
    try:
        os.seteuid(int(os.environ['SUDO_UID']))
    except Exception:
        pass


def return_root_privilege():
    try:
        os.seteuid(0)
    except Exception:
        pass


# Mark a file as an executable
def mark_executable(filename):
    st = os.stat(filename)
    os.chmod(filename, os.stat(filename).st_mode | stat.S_IEXEC)
