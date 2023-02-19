from flask import Flask, jsonify, request
import json
import tempfile
import os

app = Flask(__name__)

@app.route('/')
def index():
    text = 'This is a key-values storage API. Use /api/v1/storage/json for POST and GET requests <br> \
            Получить все данные хранилища WEB: http://{HOSTNAME:PORT}/api/v1/storage/json/all <br> \
            Получить все данные хранилища CURL:curl -i -X GET http://{HOSTNAME:PORT}/api/v1/storage/json/all <br> \
            Получить данные хранилища по ключу WEB:http://{HOSTNAME:PORT}/api/v1/storage/json?key=test <br> \
            Получить данные хранилища по ключу CURL:curl -i -GET http://{HOSTNAME:PORT}/api/v1/storage/json/read?key=test <br> \
            Добавить данные в хранилище хранилища WEB:curl -i -H \"Content-Type: application/json\" -X POST -d \'{\"test3\": \"value4\"}\' http://{HOSTNAME:PORT}/api/v1/storage/json/write'
    return text

@app.route('/api/v1/storage/json', methods=['GET'])
def storage():
    if request.method == 'GET':
        try:
            with open('storage.data', 'r') as f:
                data = json.load(f)
        except FileNotFoundError:
            data = {}

        key = request.args.get('key')

        if not key or key not in data:
            return '', 204

        return jsonify({key: data[key]}), 200

@app.route('/api/v1/storage/json/all', methods=['GET'])
def getallvalue():
    if request.method == 'GET':
        try:
            with open('storage.data', 'r') as f:
                data = json.load(f)
        except FileNotFoundError:
            data = {}

        return jsonify(data), 200

@app.route('/api/v1/storage/json/write', methods=['POST'])
def postvalue():
    if request.method == 'POST':
        try:
            with open('storage.data', 'r') as f:
                data = json.load(f)
        except FileNotFoundError:
            data = {}

        new_data = request.get_json()
        if new_data:
            data.update(new_data)
            with open('storage.data', 'w') as f:
                json.dump(data, f)
                return jsonify({"message": "Successfully added data to storage"}), 201
        else:
            return jsonify({"message": "Request body must be in JSON format"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
