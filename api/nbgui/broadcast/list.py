from http.server import BaseHTTPRequestHandler
import os
import json

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


class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        json_list = get_list()
        res = json.dumps(json_list, ensure_ascii=False, indent=4)
        self.send_response(200)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.end_headers()
        self.wfile.write(res.encode('utf-8'))