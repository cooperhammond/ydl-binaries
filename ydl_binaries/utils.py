from sys import stdout
import os
import stat


# Hook to display progress of downloads.
def dl_progress(count, blocks, totalSize):
    stdout.write("\r %3d%%  (%4d / %d pieces)"
                 % (count * blocks * 100 / totalSize, count,
                    (totalSize / blocks) + 1))
    stdout.flush()


# Mark a file as an executable
def mark_executable(filename):
    st = os.stat(filename)
    os.chmod(filename, os.stat(filename).st_mode | stat.S_IEXEC)
