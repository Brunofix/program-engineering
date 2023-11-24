import random
from query_handler_base import QueryHandlerBase
class DiceHandler(QueryHandlerBase):
    def can_process_query(self, query):
        if "dice" in query:
            return True
        return False

    def process(self, query):
        # Parse query, if numbers in query, first number is number of dices,
        # the second number is number of sides
        dice_params = query.split()
        if len(dice_params) == 1:
            self.ui.say("OK, rolling dice")
            self.ui.say(f"You got {random.randint(1,6)}")
        elif len(dice_params) == 2:
            try: 
                num_dices = int(dice_params[1])
                self.ui.say(f"OK, rolling {num_dices} dices")
                for _ in range(num_dices):
                    self.ui.say(f"You got {random.randint(1,6)}")
            except:
                self.ui.query_not_understood()
        elif len(dice_params) == 3:
            try: 
                num_dices = int(dice_params[1])
                num_sides = int(dice_params[2])
                self.ui.say(f"OK, rolling {num_dices} {num_sides}-sided dices")
                for _ in range(num_dices):
                    self.ui.say(f"You got {random.randint(1,num_sides)}")
            except:
                self.ui.query_not_understood()
        else:
            self.ui.query_not_understood()
