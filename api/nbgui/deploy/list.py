from http.server import BaseHTTPRequestHandler
import os
import json


def get_list():
    json_list = []
    for id, file_name in enumerate(sorted(os.listdir('api/nbgui/deploy/template'), reverse=True)):
        if file_name.endswith('.json'):
            path = os.path.join('api/nbgui/deploy/template', file_name)
            with open(path, 'r', encoding='utf-8') as file:
                jsonData = json.loads(file)
                id = jsonData['id']
                desc = jsonData['desc']
                json_list.append({"name": file_name, "id": id, "desc": desc})
    return json_list


class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        json_list = get_list()
        res = json.dumps(json_list, ensure_ascii=False, indent=4)
        self.send_response(200)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.end_headers()
        self.wfile.write(res.encode('utf-8'))