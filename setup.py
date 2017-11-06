from setuptools import setup

setup(
    name =         'ydl-binaries',
    version =      '1.1.4',
    description =  'A collection of scripts that will download and update \
binaries for youtube-dl and ffmpeg.',
    url =          'https://github.com/kepoorhampond/XXX',
    author =       'Kepoor Hampond',
    author_email = 'kepoorh@gmail.com',
    license =      'UNLICENSE',
    packages =     ['ydl_binaries'],
    install_requires = [
        # Nothing. :)-|-<
    ],
    entry_points = {
        'console_scripts': ['ydl-binaries = ydl_binaries.__init__:main'],
    },
)
