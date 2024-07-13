from http.server import BaseHTTPRequestHandler
import json
import httpx


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.end_headers()
        response = httpx.get('https://registry.nonebot.dev/plugins.json')
        res_raw = response.text
        res = json.dumps(res_raw, ensure_ascii=False, indent=4)
        self.wfile.write(res.encode('utf-8'))


