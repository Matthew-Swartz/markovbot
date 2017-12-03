# markovbot
Scrapes data from Facebook groupchat and then generates a message similar to an average message in that group
Uses fbchat library.  For full API go to: https://fbchat.readthedocs.io/en/master/

chatbot.py is the main function, when running will generate messages on command
generator.py is the generating function
scraper.py creates the initial library of message samples for generator to use

chatbot.py and scraper.py will need the 
user = '<username>'
password = '<password>'
threadname = '<threadid>'
variables to be modified to the users credentials for the program to work corrrectly.

If you have any questions/errors/feature ideas please shoot me a message: mjswartz92@gmail.com
