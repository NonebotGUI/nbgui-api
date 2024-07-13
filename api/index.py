from flask import Flask,request
import os
import json
from frontmatter import Frontmatter
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False



def get_list():
    json_list = []
    for id, file_name in enumerate(sorted(os.listdir('data'))):
        if file_name.endswith('.md'):
            path = os.path.join('data', file_name)
            md = Frontmatter.read_file(path)
            time = md['attributes']['time']
            json_list.append({"name": file_name, "time": time, "id": id})
    return json.dumps(json_list, ensure_ascii=False, indent=4)

def get_md(name):
    path = f'data/{name}'
    if not os.path.exists(path):
        return None
    with open(path, 'r', encoding='utf-8') as file:
        markdown_content = file.read()
    return markdown_content


@app.route('/',methods=['GET'])
def index():
    return {"status":200,"message":"Welcome to NoneBot GUI API! Deployed by Vercel"}

@app.route('/nbgui/broadcast',methods=['GET'])
def list():
    res = get_list()
    return res

@app.route('/nbgui/broadcast/detail/<int:id>')
def get_detail(id):
    try:
        md_list = json.loads(get_list())
        name = next((item['name'] for item in md_list if item['id'] == id), None)

        if name:
            return {"content":get_md(name)}
        else:
            return {"status":1002, "message":f"ID {id} not found"}
    except TypeError:
        return {"status": 1001, "error":"String is not allowed!"}


