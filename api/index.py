from fastapi import FastAPI
import os
import json
from datetime import datetime


app = FastAPI()

def get_list():
    json_list = []
    for id, file_name in enumerate(sorted(os.listdir('broadcast'))):
        if file_name.endswith('.md'):
            path = os.path.join('api/broadcast', file_name)
            time = datetime.fromtimestamp(os.path.getmtime(path)).strftime('%Y-%m-%d %H:%M:%S')
            json_list.append({"name": file_name, "time": time, "id": id})
    return json_list

def get_md(name):
    with open(f'broadcast/{name}', 'r', encoding='utf-8') as file:
        markdown_content = file.read()

    content = json.dumps(markdown_content, ensure_ascii=False)

    return content


@app.get('/')
def main():
    return {"code":200,"message":"Welcome to NoneBot GUI API！Deployed by Vercel"}


#获取列表
@app.get('/nbgui/broadcast/')
async def list():
    return get_list()


#获取公告详细内容
@app.get('/nbgui/broadcast/{id}')
async def get_broadcast(id: int):
    data = json.loads(json.dumps(get_list()))
    md_content = next((item for item in data if item['id'] == id), None)
    if md_content:
        name = md_content['name']
        time = md_content['time']
        return {"id":id,"time":time,"content":get_md(name)}
    else:
        return {"code":1001,"message":f"ID {id} not found!"}








if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app=app,
                host="::",
                port=8080,
                workers=1)