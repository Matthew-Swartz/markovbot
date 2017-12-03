
from fbchat import log, Client
from fbchat.models import *
from generator import generate_text, train_char_lm

user = '<username>'
password = '<password>'
threadname = '<threadid>'

class PSPBot(Client):
    threadname = '<threadid>'
    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        
        order = 7
        info = "I am a robot that Matthew created to simulate typical discussion in this thread.  I scrape this group message for posts and compile it into a library.  Then I use a conditional probability text generator on the library to simulate a message. \n https://github.com/Matthew-Swartz"
        if message_object.text == '!Mimicbot' and thread_type == ThreadType.GROUP and thread_id == threadname:
            lm = train_char_lm("repo.txt", order=order)        
            gen = generate_text(lm, order)            
            #log.info('{} requested from {}'.format(author_id, thread_id))
            self.send(Message(text=gen), thread_id=thread_id, thread_type=thread_type)
        elif message_object.text == '!Mimicbotinfo' and thread_type == ThreadType.GROUP and thread_id == threadname:          
            #log.info('{} requested from {}'.format(author_id, thread_id))
            self.send(Message(text=info), thread_id=thread_id, thread_type=thread_type)   
        elif thread_type == ThreadType.GROUP and thread_id == threadname and author_id != self.uid:
            #print(message_object.text)
            if(message_object.text != None and type(message_object.text) == str):
                f = open('repo.txt','r')
                temp = f.read()
                f.close()
                f = open('repo.txt','w')
                f.write(str(message_object.text.encode('ascii', 'ignore'))[2:-1])
                f.write('\n')
                f.write(temp)
                f.close()                        
                
        else:
            # Sends the data to the inherited onMessage, so that we can still see when a message is recieved
            super(PSPBot, self).onMessage(author_id=author_id, message_object=message_object, thread_id=thread_id, thread_type=thread_type, **kwargs)
            
    
client = PSPBot(user, password)
client.listen()


        
        