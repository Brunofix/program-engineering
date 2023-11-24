import random
from query_handler_base import QueryHandlerBase
class JokeHandler(QueryHandlerBase):
    JOKES = [
        ["Why did the chicken cross the road?",
         "To get to the other side!"],
        ["I went to find some camo pants, but couldn't find any..."],
        ["I used to have a handle on life, but then it broke"],
        ["I want to die peacefully in my sleep, like my grandfather...",
         "Not screaming and yelling like the passengers in his car."]
    ]

    def can_process_query(self, query):
        if "joke" in query:
            return True
        return False

    def process(self, query):
        joke = random.choice(self.JOKES)
        self.ui.say("OK, here's one:")
        for line in joke:
            self.ui.say(line)
        self.ui.say("ahahahaha")
