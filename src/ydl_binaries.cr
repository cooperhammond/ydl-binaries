require "./youtube-dl"
require "./ffmpeg"

module YdlBinaries
  VERSION = "0.1.0"

  extend self # module acts as namespace for methods
  
  def download_youtube_dl(location : String)
    ::download_youtube_dl(location)
  end

  def download_ffmpeg(location : String)
    ::download_ffmpeg(location)
  end

end
