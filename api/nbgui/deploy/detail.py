from http.server import BaseHTTPRequestHandler
import os
import json
from urllib import parse


def get_list():
    json_list = []
    for id, file_name in enumerate(sorted(os.listdir('api/nbgui/deploy/template'), reverse=True)):
        if file_name.endswith('.json'):
            path = os.path.join('api/nbgui/deploy/template', file_name)
            with open(path, 'r', encoding='utf-8') as file:
                jsonData = json.loads(file.read())
                id = jsonData['id']
                desc = jsonData['desc']
                json_list.append({"name": file_name, "id": id, "desc": desc})
    return json_list




def get_detail(id):
    if id is not None:
        try:
            id = int(id)
            list = get_list()
            name = next((item['name'] for item in list if item['id'] == id), None)
            if name:
                with open(f'api/nbgui/deploy/template/{name}', 'r', encoding='utf-8') as file:
                    res_raw = json.loads(file.read())
                res = json.dumps(res_raw, indent=4, ensure_ascii=False)
            else:
                res_raw = {"status": 1002, "error": f"ID {id} not found"}
                res = json.dumps(res_raw, ensure_ascii=False)

        except TypeError as e:
            res_raw = {"status": 1001, "error": "Only allow int ID!"}
            res = json.dumps(res_raw, ensure_ascii=False)
            print(e)
    else:
        res_raw = {"status": 1000, "error": "ID is required!"}
        res = json.dumps(res_raw, ensure_ascii=False)
    return res


class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.end_headers()
        query = parse.urlparse(self.path).query
        query_components = parse.parse_qs(query)
        id = query_components.get('id', [None])[0]
        res = get_detail(id)
        self.wfile.write(res.encode('utf-8'))
