from flask import Flask, request, jsonify
import random

app = Flask(__name__)

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    model_name = data['model_name']
    result = random.randint(1, 1000)
    response = {
        "reason": model_name,
        "result": result
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

