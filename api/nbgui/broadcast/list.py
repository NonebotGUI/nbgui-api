from http.server import BaseHTTPRequestHandler
import os
import json
from frontmatter import Frontmatter

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        json_list = []
        for id,file_name in enumerate(sorted(os.listdir('data'),reverse=True)):
            if file_name.endswith('.md'):
                path = os.path.join('data', file_name)
                md = Frontmatter.read_file(path)
                time = md['attributes']['time']
                id = md['attributes']['id']
                json_list.append({"name": file_name, "time": time, "id": id})
        res = json.dumps(json_list, ensure_ascii=False, indent=4)
        self.send_response(200)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.end_headers()
        self.wfile.write(res.encode('utf-8'))