import http.server
import socketserver
import sys
from freesms import FreeClient

free_mobile_user=""
free_mobile_api_key = ""
port = 8000
redirect_to = "https://framagit.org"

class Server(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(302)
        self.send_header('Location',redirect_to)
        self.end_headers()
        f = FreeClient(user=free_mobile_user, passwd=free_mobile_api_key)
        resp = f.send_sms(str(self.client_address) + " " + str(self.requestline))

    def serve_forever(port):
        socketserver.TCPServer(('', port), Server).serve_forever()
if __name__ == "__main__":
    Server.serve_forever(port)

