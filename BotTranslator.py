######################
# Bot Language Translator
#######################
from googletrans import Translator  # Import Translator module from googletrans package
from chatterbot import ChatBot



translator = Translator() # Create object of Translator
translated = translator.translate('Buon giorno, come stai?') 
# Source language auto detect by google trans
# By default destination language is English
#Return value of translate API is a Translated class object, which has the following member variables.

#   src – source language (default: auto)
#   dest – destination language (default: en)
#   origin – original text
#    text – translated text
#    pronunciation – pronunciation

#To access the translated string and source language, access member variables of translated object.


print(" Source Language:" + translated.src) 
# Output: Source Language: it

print(" Translated string:" + translated.text)
# Output: Translated string: Good morning, how are you?



chatbot = ChatBot('Pippo', trainer = 'chatterbot.trainers.ListTrainer')

def main():
    lang = input("What language would you like your text 
    translated to?").lower()
    while True:
        request = input("Human: ")
        response = str(chatbot.get_response(request))
        print("Bot: " + translator.outputTranslation(response,lang))

if __name__ == '__main__':
    try:
        print("Welcome")
        main()

except KeyboardInterrupt:
        print("Program Interrupted")