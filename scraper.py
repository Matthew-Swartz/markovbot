from fbchat import Client
from fbchat.models import *

user = '<username>'
password = '<password>'
threadname = '<threadid>'

client = Client(user, password)

messages = client.fetchThreadMessages(thread_id=threadname, limit=200000, before=None)

#messages.reverse()

temp = ''

for message in messages:
    if(message.text != None):
        #print(message.text)
        temp = temp +  str(message.text.encode('ascii', 'ignore'))[2:-1]
        
#print(temp)
        
f = open('repo.txt','w')
f.write(temp)
f.close()

        


