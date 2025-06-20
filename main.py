from flask import Flask, request, jsonify
from user_interface import start_chatbot
from flask_cors import CORS
from flask_socketio import SocketIO, emit

app = Flask(__name__)

socketio = SocketIO(app, cors_allowed_origins="*")

CORS(app)

chat_history = []

@socketio.on('user_message')
def handle_message(data):
    user_message = data['message']
    bot_response = start_chatbot(user_message,chat_history)
    print(bot_response)
    emit('bot_response',{'message':bot_response})

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    if not user_message:
        return jsonify({'error': 'No message provided'}), 400

    # Assuming start_chatbot function processes the message and returns a response
    bot_response = start_chatbot(user_message,chat_history)
    return jsonify({'response': bot_response})


if __name__ == "__main__":
    print("Starting RiskIQ.AI API...")
    # app.run(host='0.0.0.0', port=5000)
    app.run(port=5000)
    
    