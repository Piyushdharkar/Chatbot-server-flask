from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

class Chat_bot_controller():
    def __init__(self):
        self.bot = ChatBot("Candice")

        trainer = ChatterBotCorpusTrainer(self.bot)
        trainer.train('chatterbot.corpus.english')

        #self.bot.set_trainer(ListTrainer)
        #self.bot.set_trainer(trainer)


    def respond(self, request):
        return str(self.bot.get_response(request))