import os
import json
import boto3
from flask import Flask, render_template, request, redirect, send_file

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
BUCKET="spotify-dataset"
FILE_NAME='spotify-dataset.json'


def download_s3_file():
        s3 = boto3.client('s3')
        s3.download_file(BUCKET, FILE_NAME, FILE_NAME)
        f = open(FILE_NAME)
        data = json.load(f)
        f.close()
        return data


@app.route('/')
def entry_point():
    
    return download_s3_file()

if __name__ == "__main__":
    
    app.run(debug=True, host='0.0.0.0')

