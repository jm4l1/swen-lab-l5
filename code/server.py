from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import sys
import time
from datetime import datetime


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # set response code
        self.send_response(200)
        self.end_headers()
        if self.path == "/favicon.ico":
            return
        resource = "index.html" if self.path == "/" else self.path
        with open(f"public/{resource}", "r") as html_file_reader:
            file_lines = html_file_reader.read()
            self.wfile.write(bytes(file_lines, "utf8"))

    def do_POST(self):
        # read content length header
        content_len = int(self.headers.get("Content-Length"))
        # get content-body
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)
        # set response code
        self.send_response(200)
        # set headers
        self.send_header("content-type", "application/json")
        self.end_headers()

        # set data
        message = {}
        message["response"] = "hello " + post_body["name"]
        message["date"] = datetime.now().strftime("%A %d. %B %Y")

        self.wfile.write(bytes(json.dumps(message), "utf8"))

    def do_PUT(self):
        # set response code
        self.send_response(200)
        # set headers
        self.send_header("content-type", "text/html")
        self.end_headers()

        message = "<body><div>Method Not allowed </div><body>"
        self.wfile.write(bytes(message, "utf8"))

    def do_DELETE(self):
        # set response code
        self.send_response(200)
        # set headers
        self.send_header("content-type", "application/json")
        self.end_headers()

        message = {}

        message["response"] = "You cannot do that"

        self.wfile.write(bytes(json.dumps(message), "utf8"))
        pass


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please specify port number")
        exit(1)

    port = int(sys.argv[1])
    with HTTPServer(("", port), handler) as server:
        print("Server is running on port " + str(port))
        server.serve_forever()
