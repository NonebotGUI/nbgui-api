from http.server import BaseHTTPRequestHandler
import os
import json
from datetime import datetime
import re



def get_list():
    json_list = []
    for id, file_name in enumerate(sorted(os.listdir('./broadcast'))):
        if file_name.endswith('.md'):
            path = os.path.join('./broadcast', file_name)
            time = datetime.fromtimestamp(os.path.getmtime(path)).strftime('%Y-%m-%d %H:%M:%S')
            json_list.append({"name": file_name, "time": time, "id": id})
    return json_list

def get_md(name):
    with open(f'./broadcast/{name}', 'r', encoding='utf-8') as file:
        markdown_content = file.read()

    content = json.dumps(markdown_content, ensure_ascii=False)

    return content





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

        #获取对应id的公告
        elif re.match(r'^/nbgui/broadcast/(\d+)$', self.path):
            match = re.match(r'^/nbgui/broadcast/(\d+)$', self.path)
            if match:
                broadcast_id = match.group(1)
                id = int(broadcast_id)
                data = get_list()
                md_content = [item for item in data if item['id'] == id]
                if md_content:
                    name = md_content[0]['name']
                    time = md_content[0]['time']
                    res = {"id":id,"time":time,"content":get_md(name)}
                else:
                    res = {"code":1001,"message":f"ID {broadcast_id} not found!"}
                self.send_response(200)
                self.send_header('Content-type', 'application/json; charset=utf-8')
                self.end_headers()
                self.wfile.write(json.dumps(res, ensure_ascii=False, indent=4).encode('utf8'))
            else:
                self.send_error(404, '')

        #获取公告列表
        elif self.path == "/nbgui/broadcast/list":
            json_list = get_list()
            res = json.dumps(json_list, ensure_ascii=False, indent=4)
            self.send_response(200)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.end_headers()
            self.wfile.write(res.encode('utf-8'))



