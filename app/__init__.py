from flask import Flask
from app.controllers import Chat_bot_controller

app = Flask(__name__)
app.chat_bot = Chat_bot_controller()

from app import views