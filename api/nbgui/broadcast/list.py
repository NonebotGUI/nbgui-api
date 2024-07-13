from flask import Flask, request
import requests
import os
import json
from frontmatter import Frontmatter

def get_list():
    json_list = []
    for id, file_name in enumerate(sorted(os.listdir('data'))):
        if file_name.endswith('.md'):
            path = os.path.join('data', file_name)
            md = Frontmatter.read_file(path)
            time = md['attributes']['time']
            json_list.append({"name": file_name, "time": time, "id": id})
    return json.dumps(json_list, ensure_ascii=False, indent=4)


app = Flask(__name__)

@app.route('/')
def get_broadcast():
    return get_list()
