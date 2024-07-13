from http.server import BaseHTTPRequestHandler
import os
import json
from urllib.parse import urlparse, parse_qs


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




class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        url_parts = urlparse(self.path)
        query_params = parse_qs(url_parts.query)
        id = query_params.get('id', [None])[0]
        if id is not None:
            try:
                md_list = json.loads(get_list())
                id = int(id)
                name = next((item['name'] for item in md_list if item['id'] == id), None)
                if name:
                    res_raw = {"content":get_md(name)}
                    res = json.dumps(res_raw,indent=4)
                    status_code = 200
                else:
                    res_raw = {"status":1002, "error":f"ID {id} not found"}
                    res = json.dumps(res_raw,ensure_ascii=False)
                    status_code = 1002

            except TypeError:
                res_raw = {"status": 1001, "error":"Only allow int ID!"}
                res = json.dumps(res_raw,ensure_ascii=False)
                status_code = 1001



        else:
            res_raw = {"status":1000, "error":"ID is required!"}
            res = json.dumps(res_raw,ensure_ascii=False)
            status_code = 1000

        self.send_response(status_code)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.end_headers()
        self.wfile.write(res.encode('utf-8'))