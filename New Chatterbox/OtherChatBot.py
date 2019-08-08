from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
import logging
import subprocess as runProc
import speech_recognition as sr
import time

class ComputerTalking:
    statement =""
    def __init__(self):
        self.statement = ""
        return

    def says(self, statement):
        self.statement = statement

        runProc.check_output(['C:\Program Files (x86)\eSpeak\command_line\espeak', '-a', '50', self.statement])
        return

class VoiceToText:
    response_text = "Sorry, I didn't catch that. Could you say that again?"

    def __init__(self):
        response_text = "Sorry, I didn't catch that. Could you say that again?"
        return

    def response(self):
        response_text = "Sorry, I didn't catch that. Could you say that again?"
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)

        # recognize speech using Google Speech Recognition
        try:
            # for testing purposes, we're just using the default API key
            # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
            # instead of `r.recognize_google(audio)`
            response_text=r.recognize_google(audio)
            #pc
        except sr.UnknownValueError:
            print('Bot: Sorry, I didn\'t catch that. Could you say that again?')
            # Google Speech Recognition could not understand audio
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return response_text

Computer = ComputerTalking()

print("Bot: Please say something to start.")
Computer.says("Please say something to start.")

bot = ChatBot("ChatBot")

#conversation = open('C:\Hector\chatterbox\Dialogue.txt', 'r').readlines()
#bot.set_trainer(ListTrainer)
#bot.train(conversation)

# Below is the code to clear memory of chatbot
# bot = ChatBot("...")
# bot.storage.drop()

#The following loop will execute each time the user enters input

while True:
    try:
        vr = VoiceToText()
        r = vr.response()
        thingSaid = r
        thingSaidString = str(thingSaid)
        if (thingSaidString == 'Sorry, I didn\'t catch that. Could you say that again?'):
            Computer.says('Sorry, I didn\'t catch that. Could you say that again?')
            continue
        else:
            print("You: " + thingSaidString)
            botSays = str(bot.get_response(thingSaidString))
            print("Bot: " + botSays)
            Computer.says(botSays)
    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        Computer.says('Shutting Down.')
        print('Shutting Down.')
        break