from query_handler_base import QueryHandlerBase
import random

class NameYourHandler(QueryHandlerBase):
    def can_process_query(self, query):
        # Returns true if the query contains words that this parser is
        # supposed to process
        # Else, returns false
        pass

    def process(self, query):
        # Processes the query using the self.ui.say(), self.ui.ask() and
        # self.ui.query_not_understood() methods.
        # Doesn't return a value
        pass

