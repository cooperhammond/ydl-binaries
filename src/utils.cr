require "http/client"


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