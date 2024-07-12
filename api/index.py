from flask import Flask
import os
import json
from datetime import datetime
import re


app = Flask(__name__)

@app.route('/')
def hello_world():
    return {"code":200,"message":"Welcome to NoneBot GUI API! Deployed by Vercel"}


@app.route('/test')
def hello_flask():
    return {"code":200,"message":"Hello Flask"}