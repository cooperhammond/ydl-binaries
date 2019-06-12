# ydl_binaries

Downloads system-correct `ffmpeg`, `ffprobe`, and `youtube-dl` binaries.

## Installation

1. Add the dependency to your `shard.yml`:

   ```yaml
   dependencies:
     ydl_binaries:
       github: cooperhammond/ydl-binaries
   ```

2. Run `shards install`

## Usage

```crystal
require "ydl_binaries"

YdlBinaries.download_ffmpeg("/usr/local/bin")
YdlBinaries.download_youtube_dl("/usr/local/bin")
```

**`.download_ffmpeg(location : String)`**

Queries the user for the system type and then downloads the correct `ffmpeg` and `ffprobe` binaries into the specified location/folder.

**`.download_youtube_dl(location : String)`**

Queries the user for the system type and then downloads the latest [`youtube-dl`](https://github.com/ytdl-org/youtube-dl) binary into the specified location/folder.
