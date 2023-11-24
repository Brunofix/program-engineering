from query_handler_base import QueryHandlerBase
import random

class RockPaperScissorsHandler(QueryHandlerBase):
    def can_process_query(self, query):
        if "rock" in query or "rps" in query:
            return True
        return False

    def process(self, query):
        self.ui.say("Ok, let's play Rock-Paper-Scissors")
        you = self.ui.ask("Choose: rock, paper or scissors? ")
        me = random.choice(["rock", "paper", "scissors"])
        self.ui.say(f"I choose {me}")
        winner = None

        if "rock" in you:
            if me == "rock":
                winner = "draw"
            elif me == "paper": 
                winner = "me"
            elif me == "scissors":
                winner = "you"
        elif "paper" in you:
            if me == "rock":
                winner = "you"
            if me == "paper": 
                winner = "draw"
            if me == "scissors":
                winner = "me"
        elif "scissors" in you:
            if me == "rock":
                winner = "me"
            if me == "paper": 
                winner = "you"
            if me == "scissors":
                winner = "draw"

        if winner == "me":
            self.ui.say(f"I won, you lost, {me} beats {you}")
        elif winner == "you":
            self.ui.say(f"Good job, You won, {you} beats {me}")
        elif winner == "draw":
            self.ui.say("It's a draw!")
        else:
            self.ui.say(f"You have to choose between rock, paper and scissors.")
            self.ui.say(f"{you} is not a valid choice! Type rps to play again.")
