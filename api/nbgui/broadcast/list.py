from http.server import BaseHTTPRequestHandler
import os
import json
from datetime import datetime

def get_list():
    json_list = []
    for file_name in enumerate(sorted(os.listdir('data'),reverse=True)):
        if file_name.endswith('.md'):
            path = os.path.join('data', file_name)
            #从文件中拿id
            with open(path, 'r', encoding='utf-8') as file:
                lines_id = file.readlines()[:2]
                lines_time = file.readlines()[:3]
                id = int(lines_id[1].replace('id: ',''))
                time = str(lines_time[1].replacestrip())
            json_list.append({"name": file_name, "time": time, "id": id})
    return json_list


class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        json_list = get_list()
        res = json.dumps(json_list, ensure_ascii=False, indent=4)
        self.send_response(200)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.end_headers()
        self.wfile.write(res.encode('utf-8'))