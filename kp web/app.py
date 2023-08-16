from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

predictions = []  # Store predictions globally

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload_json', methods=['POST'])
def upload_json():
    try:
        data = request.json
        predictions.append(data)
        return jsonify({'message': 'JSON data received successfully'})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/get_predictions', methods=['GET'])
def get_predictions():
    return jsonify(predictions)

if __name__ == '__main__':
    app.run(debug=True)
