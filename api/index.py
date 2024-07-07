from http.server import BaseHTTPRequestHandler
import json

#API主体
class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        #api根
        if self.path == "/":
            self.send_response(200)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.end_headers()
            res = json.dumps({"code":200,"message":"Welcome to NoneBot GUI API！Deployed by Vercel"}, ensure_ascii=False, indent=4)
            self.wfile.write(res.encode('utf-8'))




