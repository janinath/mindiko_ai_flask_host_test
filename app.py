from flask import Flask, request, jsonify
import openai
import os
from dotenv import load_dotenv
from flask_cors import CORS
# Load environment variables
load_dotenv()
openai.api_key = os.getenv("API_KEY")

app = Flask(__name__)
CORS(app)
@app.route('/predict', methods=['POST'])
def predict():
    # Ensure a valid JSON body is provided
    data = request.get_json()
    user_message = data.get("statement", "")
    if not user_message:
        return jsonify({"status": "No input provided"}), 400

    # Manage the chat context
    if not hasattr(predict, "messages"):
        predict.messages = []
    
    predict.messages.append({'role': "user", "content": user_message})
    
    try:
        # Get GPT response
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=predict.messages
        )
        bot_message = response['choices'][0]['message']['content']
        predict.messages.append({'role': 'assistant', 'content': bot_message})
        return jsonify({"status": bot_message})
    except Exception as e:
        return jsonify({"status": f"Error: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
