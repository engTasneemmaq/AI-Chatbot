from flask import Flask, render_template, request, jsonify
from chatbot import chatbot_response

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False  # Enable Arabic text in JSON responses

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    print(f"User Input: {user_input}")  # Debugging
    response = chatbot_response(user_input)
    print(f"Bot Response: {response}")  # Debugging
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
