-- Head --
description = [[
    "Web Server Detection NSE Script"
    " custom NSE script that checks if a web server is running on a target host and retrieves the server's response headers"
]]

author = "David Prutch"

creation_date = "08/25/2023"

-- Rule --
portrule = function(host, port)
    return port.number == 80 or port.number == 443
 end
 
 action = function(host, port)
    local socket = nmap.create_socket()
    socket:set_timeout(5000)
 
    local status, err = socket:connect(host, port)
    if not status then
       return
    end
 
    local request = "HEAD / HTTP/1.1\r\nHost: " .. host.ip .. "\r\n\r\n"
    socket:send(request)
 
    local response = socket:receive_lines()
 
    if response then
       print("Web server detected on " .. host.ip .. ":" .. port.number)
       print("Server response:")
       for _, line in ipairs(response) do
          print(line)
       end
    else
       print("No web server detected on " .. host.ip .. ":" .. port.number)
    end
 
    socket:close()
 end