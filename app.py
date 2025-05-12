from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello from Render!'

@app.route('/iot', methods=['POST'])
def iot():
    data = request.json
    print("Received data:", data)
    return "Received", 200