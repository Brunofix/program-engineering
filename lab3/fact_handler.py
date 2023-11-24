import random
from query_handler_base import QueryHandlerBase
class FactHandler(QueryHandlerBase):
    FACTS = [
        ["It is impossible for most people to lick their own elbow. (try it!)"],
        ["A crocodile cannot stick its tongue out."],
        ["A shrimp's heart is in its head."],
        ["It is physically impossible for pigs to look up into the sky."],
        ["The \"sixth sick sheik's sixth sheep's sick\" is believed ",
         "to be the toughest tongue twister in the English language."],
        ["If you sneeze too hard, you could fracture a rib."],
        ["Wearing headphones for just an hour could increase the bacteria",
         "in your ear by 700 times."],
        ["Some lipsticks contain fish scales."]
    ]

    def can_process_query(self, query):
        if "fact" in query:
            return True
        return False

    def process(self, query):
        fact = random.choice(self.FACTS)
        self.ui.say("OK, here's a fun fact:")
        for line in fact:
            self.ui.say(line)
        self.ui.say("Isn't that amazing?")
