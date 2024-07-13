from http.server import BaseHTTPRequestHandler
import json
class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.end_headers()
        res_raw = {"status":200,"message":"Welcome to NoneBot GUI API! Deployed by Vercel"}
        res = json.dumps(res_raw,ensure_ascii=False)
        self.wfile.write(res.encode('utf-8'))

