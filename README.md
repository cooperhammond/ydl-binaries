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

YdlBinaries.get_ffmpeg("/usr/local/bin")
YdlBinaries.get_youtube_dl("/usr/local/bin")
```