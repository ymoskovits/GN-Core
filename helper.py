"""Helper
Holds the helper methods
"""

__author__      = "Ehud Adler & Akiva Sherman"
__copyright__   = "Copyright 2018, The Punk Kids"
__license__     = "MIT"
__version__     = "1.0.0"
__maintainer__  = "Ehud Adler & Akiva Sherman"
__email__       = "self@ehudadler.com"
__status__      = "Production"


class State():
    TEST = 0
    DEV  = 1
    PROD = 2

    @staticmethod
    def determine_state(args):
        if args.test:
            print("Running in test mode.....")
            return State.TEST
        elif args.prod:
            return State.PROD
        else:
            # The default is development
            print("Running in dev mode.....")
            return State.DEV
            

class Message():
    _message = ""

    def __init__(self):
        self._message = "Grade Alert 🚨 from Grade Notifier\n\n"

    def message(self):
        return self._message

    def newline(self):
        self._message += "\n"
        return self

    def add(self, text):
        self._message += text
        return self
    
    def sign(self):
         self._message += "\nHope you did well! -- Ehud & Akiva"
         return self