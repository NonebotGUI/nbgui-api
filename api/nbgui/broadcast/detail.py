from http.server import BaseHTTPRequestHandler
import os
import json
from urllib import parse


def get_list():
    json_list = []
    for id, file_name in enumerate(sorted(os.listdir('data'), reverse=True)):
        if file_name.endswith('.md'):
            path = os.path.join('data', file_name)
            # 从文件中拿id和时间
            with open(path, 'r', encoding='utf-8') as file:
                lines = file.readlines()[:3]
                id_line = next((line for line in lines if line.startswith('id:')), None)
                time_line = next((line for line in lines if line.startswith('time:')), None)
                if id_line and time_line:
                    id = int(id_line.replace('id: ', '').strip())
                    time = time_line.replace('time: ', '').strip()
                    json_list.append({"name": file_name, "time": time, "id": id})
    return json_list


def get_md(name):
    path = f'data/{name}'
    if not os.path.exists(path):
        return None
    with open(path, 'r', encoding='utf-8') as file:
        markdown_content = file.read()
    return markdown_content

def get_detail(id: int):
    if id is not None:
        try:
            id = int(id)
            md_list = json.loads(get_list())
            name = next((item['name'] for item in md_list if item['id'] == id), None)
            if name:
                res_raw = {"content":get_md(name)}
                res = json.dumps(res_raw,indent=4,ensure_ascii=True)
            else:
                res_raw = {"status":1002, "error":f"ID {id} not found"}
                res = json.dumps(res_raw,ensure_ascii=False)

        except TypeError as e:
            res_raw = {"status": 1001, "error":"Only allow int ID!","id":id}
            res = json.dumps(res_raw,ensure_ascii=False)
            print (e)
    else:
        res_raw = {"status":1000, "error":"ID is required!"}
        res = json.dumps(res_raw,ensure_ascii=False)
    return res


class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.end_headers()
        query = parse.urlparse(self.path).query
        query_components = parse.parse_qs(query)
        id = query_components.get('id', [None])[0]
        id = int(id)
        res = get_detail(id)
        self.wfile.write(res.encode('utf-8'))