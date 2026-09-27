import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src", "notion"))

from main_workflow import run_cafe_beans_rollover
from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        run_cafe_beans_rollover()
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"OK")