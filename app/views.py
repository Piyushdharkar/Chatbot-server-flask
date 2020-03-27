from app import app
from flask import render_template, request, redirect, current_app

@app.route('/')
@app.route('/chatbot')
def chatbot():
    return render_template('/public/chatbot.html')

@app.route("/get", methods=['GET', 'POST'])
def get_bot_response():
    user_text = request.args.get('msg')
    print('User text : ' + user_text)
    return current_app.chat_bot.respond(user_text)