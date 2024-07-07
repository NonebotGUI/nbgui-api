from http.server import BaseHTTPRequestHandler, HTTPServer
import os
import json
from datetime import datetime
import re



def get_list():
    json_list = []
    for id, file_name in enumerate(sorted(os.listdir('broadcast'))):
        if file_name.endswith('.md'):
            path = os.path.join('broadcast', file_name)
            time = datetime.fromtimestamp(os.path.getmtime(path)).strftime('%Y-%m-%d %H:%M:%S')
            json_list.append({"name": file_name, "time": time, "id": id})
    return json_list

def get_md(name):
    with open(f'broadcast/{name}', 'r', encoding='utf-8') as file:
        markdown_content = file.read()

    content = json.dumps(markdown_content, ensure_ascii=False)

    return content


class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain; charset=utf-8')
            self.end_headers()
            self.wfile.write(response_bytes)


        
        elif re.match(r'^/nbgui/broadcast(/(\d+))?$', self.path):
            match = re.match(r'^/nbgui/broadcast(/(\d+))?$', self.path)
            if match:
                broadcast_id = match.group(2) if match.group(2) else None
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                response = f"{get_md(broadcast_id)}"
                self.wfile.write(response.encode())
            else:
                self.send_error(404, '')

httpd = HTTPServer(('0.0.0.0', 8080), handler)

print("Serving at port 8000...")
httpd.serve_forever()