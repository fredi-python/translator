from googletrans import Translator

frage = input('was soll ins englische übersetzt werden? \n')

trans = Translator()

print(trans.translate(text=frage, dest='en').text)
