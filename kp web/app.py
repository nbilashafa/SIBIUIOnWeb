from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload_json', methods=['POST'])
def upload_json():
    try:
        data = request.json  # Parse JSON data from the request
        # Process the data as needed
        response = {'message': 'JSON data received successfully'}
        return jsonify(response)
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
