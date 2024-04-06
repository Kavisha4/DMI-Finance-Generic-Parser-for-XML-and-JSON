from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_json():
    try:
        # Check if request contains JSON data
        if request.is_json:
            # Access JSON data from request
            json_data = request.get_json()
            # Process the JSON data as needed
            print(json_data)
            return jsonify({'success': True, 'data': json_data})
        else:
            return jsonify({'error': 'Request does not contain JSON data'})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
