from flask import Flask
import os
import json
from frontmatter import Markdown

def get_list():
    json_list = []
    for id, file_name in enumerate(sorted(os.listdir('data'))):
        if file_name.endswith('.md'):
            path = os.path.join('data', file_name)
            with open(path, 'r', encoding='utf-8') as file:
                markdown_content = file.read()
            md = Markdown(path)
            time = md.metadata.get('time', '')
            json_list.append({"name": file_name, "time": time, "id": id, "conetent":markdown_content})
    return json.dumps(json_list, ensure_ascii=True, indent=4)


app = Flask(__name__)

@app.route('/')
def get_broadcast():
    return get_list()
