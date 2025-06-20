# llama_inference.py
from langchain_groq import ChatGroq

def initialize_llama_client():
    try:
        # Initialize ChatGroq client with API key and model
        client = ChatGroq(
            model="meta-llama/llama-4-scout-17b-16e-instruct", # model used
            api_key='', # Replace with your actual API key
            temperature=0.35,
            max_tokens=1024
        )
        print("ChatGroq client initialized successfully.")
        return client
    except Exception as e:
        print(f"Error initializing ChatGroq client: {e}")
        return None

def generate_response(client, query, context="",chat_history=[]):
    if client is None:
        return "Error: Client initialization failed. Cannot generate response."

    try:
        # Prepare messages for completion
        messages = [
            ("system", context),
            ("human", query)
        ]
        
        
        # Generate chat completion
        ai_msg = client.invoke(messages)
        return ai_msg.content
    except Exception as e:
        print(f"Error generating response: {e}")
        return "Error: Unable to generate response."
