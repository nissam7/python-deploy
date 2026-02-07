from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    name = data.get('name')
    message = data.get('message')

    print(f"Name: {name}, Message: {message}")

    return jsonify({
        "status": "Message received successfully!"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

