from query_handler_base import QueryHandlerBase
from joke_handler import JokeHandler
from fact_handler import FactHandler
from dice_handler import DiceHandler
from rps_handler import RockPaperScissorsHandler
from love_handler import LoveHandler

class QueryNotUnderstoodHandler(QueryHandlerBase):
    def process(self, query):
        self.ui.query_not_understood()

class ByeHandler(QueryHandlerBase):
    def can_process_query(self, query):
        if "bye" in query:
            return True
        return False

    def process(self, query):
        self.ui.bye()

class QueryParser:
    # Instead of requiring QueryParser to know the details of the
    # implementation for each particular parser, we can let each parser to
    # determine if that query is meant for them. This way we can add new
    # QueryHandlers without needing to change the QueryParser class. If we
    # wanted to add a new query handler, the only change required would be
    # adding the new query handler class to the list of registered query
    # handlers in the self.HANDLERS class variable.
    #
    # We can add handler classes to the HANDLERS list and initalize each
    # handler in a constructor for this class (__init__)
    HANDLERS = [
        ByeHandler,
        FactHandler,
        DiceHandler,
        JokeHandler,
        RockPaperScissorsHandler,
        LoveHandler,
    ]

    def __init__(self, ui):
        self.ui = ui
        # When initializing all the handlers from self.HANDLERS in this way,
        # our QueryParser class does not have to know anything about the
        # queries themselves. We can simply iterate through all the handlers
        # and let each handler to determine if they are responsible for that
        # particular query
        #
        # We have to initialize all the query handlers, since they need a
        # reference to `ui` to be able to say and ask.
        self.handlers = [ handler(self.ui) for handler in self.HANDLERS ]

    def __str__(self):
        return "; ".join([str(handler) for handler in self.handlers])

    def get_query_handler(self, query):
        # We simply iterate through all the configured (initialized) handlers
        # and each handler decides for itself if it's able to process the
        # query. Take care, we iterate through self.handlers, not
        # self.HANDLERS, because the latter is a list of classes and does not
        # have a reference to ui.
        for handler in self.handlers:
            # However, now every query handler has to implement the
            # `can_process_query` method for themselves. The advantage is that
            # any improvement in the query parsing for each handler is
            # contained to the class for that handler. No other class has to
            # know anything about that handler's query processing.
            if handler.can_process_query(query):
                # We return the handler that can process the query.
                return handler
        # If none of the handlers can process the query:
        return QueryNotUnderstoodHandler(self.ui)
