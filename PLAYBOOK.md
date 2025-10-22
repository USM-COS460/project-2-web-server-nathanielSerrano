## COS 460/540 - Computer Networks
# Project 2: HTTP Server

# Nathaniel Serrano

This project is written in Python on MacOS.

## How to compile

No need to compile, since Python is an interpreted language. That being said, a Python interpreter is required to run `web_server.py`

## How to run

To run, simply enter the following command in a Python environment while within the file's directory:
```
python web_server.py [HOST] [PORT NUMBER] [DIRECTORY]
```

example usage:
```
python web_server.py locahost 8080 ./www
```

Once the server is running, clients can connect either via a web browser or through services like telnet.

example usage:
```
telnet locahost 8080

GET /index.html HTTP/1.0
```

## My experience with this project

This project marks my second experience with socket programming but this one actually gave some really cool insight into how the internet and web browsers actually work behind the scenes. Same as with the last project, I chose to complete this one in Python since it was what I felt best suited this task.

I really enjoyed interacting with the web server through both a web browser and the command line (via telnet), as well as experimenting with different directories to view different web pages and images. While the implementation may not necessarily be as thorough as production code in the industry, I was able to properly serve up web pages to clients when the server was met with an HTTP request. This is essentially the core functionality of a web browser, outside of parsing URLs to convert them to IP addresses and managing authentication/authorization via HTTP request headers.

Overall, this project made me learn more about what's usually hidden out of view and changed how I view web pages entirely. A fun project!
