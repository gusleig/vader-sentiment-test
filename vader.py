from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import requests


from googletrans import Translator

analyser = SentimentIntensityAnalyzer()

translator = Translator()


def sentiment_analyzer_scores(sentence):
    score = analyser.polarity_scores(sentence)
    print("{:-<40} {}".format(sentence, str(score)))



frase = 'Bolsonaro é um homem mau'
frase = 'O Lula esta preso babaca!'
frase = translator.translate(frase, dest='en').text

resultado = sentiment_analyzer_scores(frase)['compound']

print("fim: " + str(resultado))