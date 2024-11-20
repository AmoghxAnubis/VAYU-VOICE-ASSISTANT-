from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

bot = ChatBot('VEGA')
trainer = ChatterBotCorpusTrainer(bot)
trainer.train('data/ai.yml', 'data/botprofile.yml', '')
while True:
    query = input(">> ")
    print(bot.get_response(query))