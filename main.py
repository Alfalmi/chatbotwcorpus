from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.logic import MathematicalEvaluation, BestMatch

my_bot = ChatBot(name='PyBot', read_only=True,
                 logic_adapters=
                 ['chatterbot.logic.MathematicalEvaluation',
                  'chatterbot.logic.BestMatch'])

corpus_trainer = ChatterBotCorpusTrainer(my_bot)
corpus_trainer.train('chatterbot.corpus.english')

small_talk = ['hi there!',
              'hi',
              'how do you do',
              'how are you',
              'i\'m cool',
              'fine, you?',
              'always cool',
              'i\'m ok',
              'glad to hear that.',
              'i\'m fine',
              'i feel awesome',
              'excellent, glad to hear that',
              'not so good',
              'sorry to hear that.',
              'what\'s your name?',
              'i\'m PyBot. ask me a math question please'
              ]

small_talk_1 = ['pythagorean theorem',
                'a squared plus b squared equals c squared.']

small_talk_2 = ['law of cosines',
                'c**2 = a**2 + b**2 - 2 * a * b *cos(gamma)']

list_trainer = ListTrainer(my_bot)

for item in (small_talk, small_talk_1, small_talk_2):
    list_trainer.train(item)

    print(my_bot.get_response("hi"))
