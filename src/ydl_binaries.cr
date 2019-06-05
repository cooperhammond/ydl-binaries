require "http/client"

# TODO: Write documentation for `YdlBinaries`
module YdlBinaries
  VERSION = "0.1.0"

  SYS = __get_system()

  extend self # module acts as namespace for methods

  def download_ffmpeg(location : String)
    download_url = "https://raw.githubusercontent.com/cooperhammond/ffmpeg-binaries/master/" + SYS

    files = ["ffmpeg", "ffprobe"]

    if SYS == "/win32/"
      files[0] += ".exe"
      files[1] += ".exe"
    end

    i = 0
    while i < files.size()
      url_to_download = download_url + files[i]
      filename = Path[location].join(files[i]).to_s
      puts "Downloading #{files[i]} ..."
      __retrieve_file(url_to_download, filename)
      __mark_as_executable(filename)

      i += 1
    end
  end

  def download_youtube_dl(location : String)
    download_url = "https://youtube-dl.org/downloads/latest/"
    filename = "youtube-dl" 

    filename += ".exe" if SYS == "/win32/"

    download_url += filename
    filename = Path[location].join(filename).to_s

    __retrieve_file(download_url, filename)
    __mark_as_executable(filename)
  end

  def __get_system
    puts "What system are you on?"
    puts "1. Linux"
    puts "2. Windows"
    puts "3. Mac OSX"
    while true
      print("> ")
      sys = gets()
      case sys
      when "1"
        return "/linux/"
      when "2"
        return "/win32/"
      when "3"
        return "/darwin/"
      else
        puts "Bad answer. Try again. 1, 2, or 3."
      end
    end
  end

  def __retrieve_file(url : String, filename : String)
    HTTP::Client.get(url) do |response|

      puts response.body_io.gets_to_end

      File.write(filename, response.body_io)

      # If there's a redirect, follow it.
      if response.status_code == 302 # Redirect code
        __retrieve_file(response.headers["Location"], filename)
      end
    
    end
  end

  def __mark_as_executable(filename : String)
    File.chmod(filename, 0o755) # 755 = executable
  end
end

YdlBinaries.download_youtube_dl("./")