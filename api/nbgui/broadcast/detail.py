from http.server import BaseHTTPRequestHandler
import os
import json
from frontmatter import Frontmatter


def get_list():
    json_list = []
    for file_name in enumerate(sorted(os.listdir('data'),reverse=True)):
        if file_name.endswith('.md'):
            path = os.path.join('data', file_name)
            #从文件中拿id
            with open(path, 'r', encoding='utf-8') as file:
                lines_id = file.readlines()[:2]
                lines_time = file.readlines()[:3]
                id = int(lines_id[1].replace('id: ','').strip())
                time = str(lines_time[1].replace('time: ','').strip())
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
        id_str = self.path.split('?')[1].split('=')[1] if '?' in self.path else ''
        id = int(id_str) if id_str else None
        if id is not None:
            try:
                md_list = json.loads(get_list())
                name = next((item['name'] for item in md_list if item['id'] == id), None)
                if name:
                    res_raw = {"content":get_md(name)}
                    res = json.dumps(res_raw,indent=4)
                    self.send_response(200)
                    self.send_header('Content-Type', 'application/json; charset=utf-8')
                    self.end_headers()
                    self.wfile.write(res.encode('utf-8'))
                else:
                    res_raw = {"status":1002, "error":f"ID {id} not found"}
                    res = json.dumps(res_raw,ensure_ascii=False)
                    self.send_response(1002)
                    self.send_header('Content-Type', 'application/json; charset=utf-8')
                    self.end_headers()
                    self.wfile.write(res.encode('utf-8'))

            except TypeError:
                res_raw = {"status": 1001, "error":"String is not allowed!"}
                res = json.dumps(res_raw,ensure_ascii=False)
                self.send_response(1001)
                self.send_header('Content-Type', 'application/json; charset=utf-8')
                self.end_headers()
                self.wfile.write(res.encode('utf-8'))



        else:
            self.send_response(1000)
            self.end_headers()
            res_raw = {"status":1000, "error":"ID is required!"}
            res = json.dumps(res_raw,ensure_ascii=False)
            self.wfile.write(res.encode('utf-8'))