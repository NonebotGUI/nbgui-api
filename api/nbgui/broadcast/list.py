from http.server import BaseHTTPRequestHandler
import os
import json
from datetime import datetime

def get_list():
    #从文件中拿id
    with open('data/加入我们的QQ群聊.md', 'r', encoding='utf-8') as file:
        lines_id = file.readlines()[:2]
        lines_time = file.readlines()[:3]
        id = int(lines_id[1].replace('id: ','').strip())
        time = str(lines_time[2].replace('time: ','').strip())
    return {"name": 'file_name', "time": time, "id": id}



class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        json_list = get_list()
        res = json.dumps(json_list, ensure_ascii=False, indent=4)
        self.send_response(200)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.end_headers()
        self.wfile.write(res.encode('utf-8'))