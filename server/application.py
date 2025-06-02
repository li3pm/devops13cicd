import http.server
import socketserver

PORT = 8000

class TestMe:
    def take_five(self):
        return 5

    def port(self):
        return PORT

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        try:
            with open('index.html', 'r', encoding='utf-8') as file:
                content = file.read()
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(content.encode())
        except FileNotFoundError:
            self.send_response(404)
            self.end_headers()

if __name__ == '__main__':
    with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
        print("serving at port", PORT)
        httpd.serve_forever()
