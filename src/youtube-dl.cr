require "./utils"

def download_youtube_dl(location : String)

  sys = __get_system()

  download_url = "https://youtube-dl.org/downloads/latest/"
  filename = "youtube-dl" 

  filename += ".exe" if sys == "/win32/"

  download_url += filename
  filename = Path[location].join(filename).to_s

  puts "Downloading youtube-dl to #{filename} ..."
  __retrieve_file(download_url, filename)
  __mark_as_executable(filename)
end