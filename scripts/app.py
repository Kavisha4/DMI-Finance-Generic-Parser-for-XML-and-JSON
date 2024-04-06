from flask import Flask, request, jsonify
import os
import json_parse_respobj
import json_parse_norespobj

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/process_json', methods=['POST'])
def process_json():
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file provided'}), 400

        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400

        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)

        if file.filename.lower().startswith("bureau_"):
            metadata = process_bureau_file(file_path)
        else:
            metadata = process_non_bureau_file(file_path)

        return jsonify({'metadata': metadata}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def process_bureau_file(file_path):
    return json_parse_respobj.process_json_file(file_path)

def process_non_bureau_file(file_path):
    return json_parse_norespobj.process_json_file(file_path)

if __name__ == '__main__':
    app.run(debug=True)