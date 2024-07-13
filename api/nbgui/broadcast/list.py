from http.server import BaseHTTPRequestHandler
import os
import json
from frontmatter import Frontmatter


def get_list():
    json_list = []
    for id, file_name in enumerate(sorted(os.listdir('data'))):
        if file_name.endswith('.md'):
            path = os.path.join('data', file_name)
            md = Frontmatter.read_file(path)
            time = md['attributes']['time']
            json_list.append({"name": file_name, "time": time, "id": id})
    return json.dumps(json_list, ensure_ascii=False, indent=4)


class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        json_list = get_list()
        res = json.dumps(json_list, ensure_ascii=False, indent=4)
        self.send_response(200)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.end_headers()
        self.wfile.write(res.encode('utf-8'))