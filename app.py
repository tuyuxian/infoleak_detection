"""
Author: Yu-Hsien,Tu
Date: 2020/07/30
Flask 
Version 1.1
"""
from flask import Flask, render_template, url_for, jsonify, request, redirect
import classification

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/detect', methods=['POST'])
def detect_text():
    global num
    data = request.get_json()
    # print(data) 
    text_input = data['text']
    response = classification.get_result(text_input)
    num = response['uuid']
    return jsonify(response)


if __name__ == '__main__':
    app.run()
