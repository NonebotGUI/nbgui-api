from http.server import BaseHTTPRequestHandler
import os
import json
from datetime import datetime
import re

def get_list():
    json_list = []
    for id, file_name in enumerate(sorted(os.listdir('data'))):
        if file_name.endswith('.md'):
            path = os.path.join('data', file_name)
            time = datetime.fromtimestamp(os.path.getmtime(path)).strftime('%Y-%m-%d %H:%M:%S')
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
        try:
            if self.path == "/":
                self.send_response(200)
                self.send_header('Content-Type', 'text/plain; charset=utf-8')
                self.end_headers()
                self.wfile.write(b'{"code":200,"message":"Welcome to NoneBot GUI API! Deployed by Vercel"}')

            elif re.match(r'^/nbgui/broadcast/(\d+)$', self.path):
                match = re.match(r'^/nbgui/broadcast/(\d+)$', self.path)
                if match:
                    broadcast_id = match.group(1)
                    id = int(broadcast_id)
                    data = get_list()
                    md_content = next((item for item in data if item['id'] == id), None)
                    if md_content:
                        name = md_content['name']
                        time = md_content['time']
                        content = get_md(name)
                        if content:
                            res = {"id": id, "time": time, "content": content}
                        else:
                            res = {"code": 1002, "message": f"File {name} not found!"}
                    else:
                        res = {"code": 1001, "message": f"ID {broadcast_id} not found!"}
                    
                    self.send_response(200)
                    self.send_header('Content-type', 'application/json; charset=utf-8')
                    self.end_headers()
                    self.wfile.write(json.dumps(res, ensure_ascii=False, indent=4).encode('utf8'))
                else:
                    self.send_error(404, '')

            elif self.path == "/nbgui/broadcast/list":
                json_list = get_list()
                res = json.dumps(json_list, ensure_ascii=False, indent=4)
                self.send_response(200)
                self.send_header('Content-Type', 'application/json; charset=utf-8')
                self.end_headers()
                self.wfile.write(res.encode('utf-8'))
                
        except FileNotFoundError as e:
            self.send_error(404, f"File not found: {str(e)}")
        except Exception as e:
            self.send_error(500, f"Internal Server Error: {str(e)}")
        finally:
            # 确保在处理完请求后关闭连接
            self.close_connection = True

