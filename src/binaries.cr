require "./youtube"
require "./ffmpeg"
require "./utils"

module YdlBinaries
  extend self # module acts as namespace for methods

  @binary_location = "./"

  def get_both(location = "", system = "")
    location = @binary_location if location == ""
    system = Utils.get_system() if system == ""

    self.download_youtube_dl(location, system)
    self.download_ffmpeg(location, system)
  end

  def get_youtube_dl(location = "", system = "")
    location = @binary_location if location == ""
    system = Utils.get_system() if system == ""

    ::download_youtube_dl(location, system)
  end

  def get_ffmpeg(location = "", system = "")
    location = @binary_location if location == ""
    system = Utils.get_system() if system == ""

    ::download_ffmpeg(location, system)
  end
  
  def download_youtube_dl(location : String, system : String)
    ::download_youtube_dl(location, system)
  end

  def download_ffmpeg(location : String, system : String)
    ::download_ffmpeg(location, system)
  end

end
