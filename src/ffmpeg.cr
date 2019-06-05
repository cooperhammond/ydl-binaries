require "./utils"

def download_ffmpeg(location : String)

  sys = __get_system()

  download_url = "https://raw.githubusercontent.com/cooperhammond/ffmpeg-binaries/master/" + sys

  files = ["ffmpeg", "ffprobe"]

  if SYS == "/win32/"
    files[0] += ".exe"
    files[1] += ".exe"
  end

  i = 0
  while i < files.size()
    url_to_download = download_url + files[i]
    filename = Path[location].join(files[i]).to_s

    puts "Downloading #{files[i]} to #{filename} ..."
    __retrieve_file(url_to_download, filename)
    __mark_as_executable(filename)

    i += 1
  end
end