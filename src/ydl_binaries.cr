require "file_utils"

require "./youtube"
require "./ffmpeg"
require "./utils"

module YdlBinaries
  extend self # module acts as namespace for methods

  @@binary_location = "./"

  def get_both(location = "", system = "")
    location = @@binary_location if location == ""
    expanded_loc = Path[location].expand(home: true).to_s

    system = Utils.get_system() if system == ""
    Utils.check_directory(expanded_loc)
    ::download_youtube_dl(expanded_loc, system)
    ::download_ffmpeg(expanded_loc, system)
  end

  def get_youtube_dl(location = "", system = "")
    location = @@binary_location if location == ""
    expanded_loc = Path[location].expand(home: true).to_s

    system = Utils.get_system() if system == ""
    Utils.check_directory(expanded_loc)
    ::download_youtube_dl(expanded_loc, system)
  end

  def get_ffmpeg(location = "", system = "")
    location = @@binary_location if location == ""
    expanded_loc = Path[location].expand(home: true).to_s

    system = Utils.get_system() if system == ""
    Utils.check_directory(expanded_loc)
    ::download_ffmpeg(expanded_loc, system)
  end
  
  def download_youtube_dl(location : String, system : String)
    ::download_youtube_dl(location, system)
  end

  def download_ffmpeg(location : String, system : String)
    ::download_ffmpeg(location, system)
  end

end
