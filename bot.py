#!/bin/python3
from sdk_bot.client import Client
from sys import path

bot_token = '5hA9lHRiGzLEQ8jmPMFnBBvPPJnEf9EOux38K4yCNrU2fIt7iajd9Udi0aZ6joBok2huKeR9OeG4KWb1z6R9NxRTB2lsbNWQ48BTWNhVsRudA-LCt0cNxH8KtUdA4GeX7xgLcGIeCDqLqKcp'

bot = Client(bot_token)
try:
    messages = bot.get_messages()
    for message in messages:
        print("New Message Received: " + str(message))
except Exception as e:
          print(e.args[0])
