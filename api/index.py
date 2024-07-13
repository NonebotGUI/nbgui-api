from flask import Flask,request
import os
import json
from frontmatter import Frontmatter
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/',methods=['GET'])
def index():
    return {"status":200,"message":"Welcome to NoneBot GUI API! Deployed by Vercel"}