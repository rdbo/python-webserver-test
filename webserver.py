from http.server import BaseHTTPRequestHandler, HTTPServer

class WebServer(BaseHTTPRequestHandler):
    def do_GET(self):
        if(self.path == "/"):
            self.path = "/index.html"
        
        self.path = f".{self.path}"

        try:
            page_file = open(self.path)
            self.send_response(200)
            output = page_file.read().encode("utf-8")
        except:
            print(f"[!] Unable to open file: {self.path}")
            self.send_response(404)
            output = "<h1>File Not Found</h1>".encode("utf-8")

        self.end_headers()

        self.wfile.write(bytes(output))

    def do_POST(self):
        pass


def main():

    host = "localhost"
    port = 4444

    try:
        try:
            server = HTTPServer((host, port), WebServer)
        except:
            print(f"[!] Unable to start server at: '{host}:{port}'")
            return False
        print(f"[*] Server started at: '{host}:{port}'")
        server.serve_forever()
    except BaseException as e:
        print(f"[!] Exception caught: {e}")
        print("[*] Exiting...")
    
    server.server_close()
    return True

if __name__ == "__main__":
    main()