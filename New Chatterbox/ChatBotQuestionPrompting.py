from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
import logging
import subprocess as runProc
import speech_recognition as sr

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
    response_text = ""

    def __init__(self):
        response_text = ""
        return

    def response(self):
        response_text = ""
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
bot = ChatBot("ChatBot")
#conversation = open('C:\Hector\chatterbox\Dialogue.txt', 'r').readlines()
#bot.set_trainer(ListTrainer)
#bot.train(conversation)

# Below is the code to clear memory of chatbot
# bot = ChatBot("...")
# bot.storage.drop()





def getUserInput(thingNeeded):
    counter =0
    userName =''
    verified = False
    vr = VoiceToText()
    #counter = counter+1
    while counter <=3 and userName == '':
        Computer.says("Please say your " + thingNeeded + ".")
        print("Bot: Please say your " + thingNeeded + ".")
           
        r = vr.response()
        r = r.replace(" ","")
        counter=counter+1
        print ("I hear["+r+"]")

        if r !="":
            counter = 0
            userName=str(r)
            Computer.says("Your " + thingNeeded + " is: " + userName + ". Is this correct? Please respond YES to verify and anything else to redo.")
            print("Bot: Your " + thingNeeded + " is: " + userName + ". Is this correct? Please respond YES to verify and anything else to redo.")   
            r = vr.response()    
            
            if r == "":
                counter=counter+1
                Computer.says("Can you repeat what you said")
                print("Bot: Can you repeat what you said")
        
        r = vr.response() 
        
        if (r == 'yes'):    
            Computer.says("You have verified that your " + thingNeeded + " is: " + userName)
            print("Bot: You have verified that your " + thingNeeded + " is: " + userName)
            verified = True
    
    #if verified == False
    Computer.says("Goodbye")
    print("Goodbye")        
    
    if verified == True :
        Computer.says("Hello " + userName + ", how are you?")
        print("Bot: Hello " + userName + ", how are you?")
        r = vr.response()
        if (r == 'good','fine','great'):
            Computer.says("Okay I hear " + r)
            print("Okay I hear " + r)
            Computer.says("What is your favourite food?")
            print("What is your favourite food?")
            r=vr.reponse()

            if (r == 'pizza'):
                Computer.says("Your favourite food is" + thingNeeded)
                print("Your favourite food is" + thingNeeded)

            if(r ==""):
                print("Goodbye")
        if r =="":
            Computer.says("Goodbye")  
        
    
        
        
        # if  r != "NONE_01":
        #     userName=str(r)
        #     Computer.says("Your " + thingNeeded + " is: " + userName + ". Is this correct? Please respond YES to verify and anything else to redo.")
        #     print("Bot: Your " + thingNeeded + " is: " + userName + ". Is this correct? Please respond YES to verify and anything else to redo.")
            
        #     r = vr.response()
        #     if (r == 'yes'):    
        #         Computer.says("You have verified that your " + thingNeeded + " is: " + userName)
        #         print("Bot: You have verified that your " + thingNeeded + " is: " + userName)
        #         verified = True
                    
        #     else:
        #         #Computer.says("Please say your "+thingNeeded+ "again") 
        #         Computer.says("You didn't verify your name")
        #         print("You didn't verify your name")
        # if verified:
        #         Computer.says("Hello " + userName + ", how are you?")
        #         print("Bot: Hello " + userName + ", how are you?")

        #         if (r == 'good', 'great' , 'fine'):
        #             Computer.says("You have confirmed that your day" + thingNeeded + "is" +r)
        #             print("Bot: You have confirmed that your day" + thingNeeded + "is" +r)
        #         else:
        #             Computer.says("Can you repeat what you said")
        #             print("Can you repeat what you said")                 
getUserInput("name")
# getUserInput ("favourite colour")
# getUserInput("FOOD")
# UserFavouriteColour = thingSaidString
# getUserInput ("favourite food")
# UserFavouriteFood = thingSaidString
# while verified == False:
#         r = vr.response()
#         if  (r == ''):
#             Computer.says("Can you repeat what you said")
#             print("Bot: Can you repeat what you said")
        
#         if (r == 'yes'):    
#             Computer.says("You have verified that your " + thingNeeded + " is: " + userName)
#             print("Bot: You have verified that your " + thingNeeded + " is: " + userName)
#             verified = True

#     Computer.says("Hello " + userName + ", how are you?")
#     print("Bot: Hello " + userName + ", how are you?")
#     r = vr.response()
#     if (r == 'good','fine','great'):
#         Computer.says("Okay I hear" + r)
#         print("Okay I hear" + r)
