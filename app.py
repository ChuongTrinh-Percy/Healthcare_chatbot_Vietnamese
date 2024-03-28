from flask import Flask, render_template, request, jsonify

from model.chatbot import ChatBot
from model.preprocessing import input_features_dict, max_encoder_seq_length, num_encoder_tokens
from model.prediction import decode_response
chatbot = ChatBot(max_encoder_seq_length, num_encoder_tokens, input_features_dict, decode_response)

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('chat.html')


@app.route("/get", methods=["GET", "POST"])
def chat():

    msg = request.form["msg"]
    input = msg
    return chatbot.start_chat(input)


if __name__ == '__main__':
    app.run()
