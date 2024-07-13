from flask import Flask,request
import requests

app = Flask(__name__)

@app.route('/')
def get_broadcast():
    return {"code":200,"message":"Welcome to NoneBot GUI API! Deployed by Vercel"}
