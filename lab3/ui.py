import random
import sys
from query_parser import QueryParser

class UI:
    me = "Billy"
    def __init__(self):
        self.you = input(f"Hi, I'm {self.me}, what's your name? ")
        print(f"Well {self.you}, nice to meet you!")

    def ask(self, input_text=None):
        if input_text == None:
            print(f"\n{self.me} >>> What can I do for you {self.you}?")
        else:
            print(f"\n{self.me} >>> {input_text}")
        return input(f"{self.you} >>> ")

    def say(self, text):
        print(f"{self.me} >>> {text}")

    def main_loop(self):
        parser = QueryParser(self)
        query = None
        while True:
            query = self.ask()
            handler = parser.get_query_handler(query)
            handler.process(query)

    def bye(self):
        self.say("Glad to be of service, bye to you too.")
        self.say("Find me again if you have any questions.")
        sys.exit(0)

    def query_not_understood(self):
        self.say("I'm sorry, I don't understand")
        self.say("Try asking me again!")


