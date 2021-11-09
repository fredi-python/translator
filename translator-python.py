from googletrans import Translator

question1 = input('in which language do you want to translate? type: de, en etc')
question2 = input('what do you want to translate?')

translator = Translator()

print(translator.translate(text=question2, dest=question1).text)

