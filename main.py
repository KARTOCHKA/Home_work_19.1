from http.server import BaseHTTPRequestHandler, HTTPServer

hostName = 'localhost'
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):

    def do_GET(self):
        text = "Hello, World wide web!"

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(bytes(text, 'utf-8'))

    def do_POST(self):
        c_len = int(self.headers['Content-Length'])
        body = self.rfile.read(c_len)
        data = body.decode('utf-8')
        print(data)
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(bytes('', 'utf-8'))


if __name__ == '__main__':
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print('Server started http://%s:%s' % (hostName, serverPort))
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass
    webServer.server_close()
    print('Server stopped')
