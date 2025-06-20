# user_interface.py
from query_bot import query_bot_response

def start_chatbot(user_message,chat_history):
    print("Welcome to RiskIQ.AI model!")
    print("Type 'exit' to end the conversation.\n")

    response = query_bot_response(user_message,chat_history)
    return response
