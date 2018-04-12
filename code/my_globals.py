# coding:utf-8

import codecs
import datetime

# if True:  # black characters
#     heart = u"\u2665"
#     spade = u"\u2660"
#     diamond = u"\u2666"
#     club = u"\u2663"
# else:  # white characters
#     heart = u"\u2661"
#     spade = u"\u2664"
#     diamond = u"\u2662"
#     club = u"\u2667"

heart = "H"
spade = "S"
diamond = "D"
club = "C"

val_to_str = {
    '14': 'A',
    '13': 'K',
    '12': 'Q',
    '11': 'J',
    '10': '10',
    '9': '9'
}

suit_to_str = {
    'S': 'Spades',
    'H': 'Hearts',
    'D': 'Diamonds',
    'C': 'Clubs'
}


class Logger:
    def __init__(self, logging_file):
        self.the_log = codecs.open(logging_file, encoding='utf-8', mode='w')

    def log(self, info):
        self.the_log.write(info.replace('\n', '\r\n'))
        self.the_log.write('\r\n')


class Info:

    def __init__(self):
        # trick level
        self.dealer = None  # player
        self.lead = None  # suit
        self.center = {}  # array of {card:player} for cards in center of table

        # round level
        self.trump = None  # suit
        self.caller = None  # player
        self.tricksA = 0  # tricks gotten
        self.tricksB = 0

        # game level
        self.scoreA = 0  # total score
        self.scoreB = 0

    def resetTrick(self):
        self.lead = None
        self.center = {}

    def resetRound(self):
        self.trump = None
        self.caller = None
        self.tricksA = 0
        self.tricksB = 0

game = Info()


class Card(object):

    def __init__(self, suit, num):
        self.suit = suit
        self.num = num

    def __str__(self):
        if self.num > 10:
            return ["11", "12", "13", "14"][self.num - 11] + self.suit
        # elif self.num == 10:
        #     return str(self.num) + self.suit
        else:
            prefix = ""
            if self.num == 9:
                prefix = "0"

            return "%s%d%s" % (prefix, self.num, self.suit)
            # return str(self.num) + self.suit

    def __repr__(self):
        return '<%s %s>' % (self.__class__.__name__, self.__dict__)

    # NOTE: for testing purposes
    # def __repr__(self):
    #     num_str = '%d' % (self.num)
    #     return '%s of %s' % (val_to_str[num_str], suit_to_str[self.suit])


# a list of all possible cards, done as a tuple so that it cannot be
# accidently changed at runtime
allcards = tuple([Card(s, c) for s in (diamond, spade, club, heart)
                  for c in (14, 13, 12, 11, 10, 9)])


def offSuit(trump_suit):
    """
    Takes a suit and returns what the off hand suit would be.
    """
    if trump_suit == heart:
        return diamond
    elif trump_suit == diamond:
        return heart
    elif trump_suit == spade:
        return club
    else:
        return spade


def query_yes_no(question, default="yes"):
    """
        Ask a yes/no question via raw_input() and return their answer.
        source: http://stackoverflow.com/a/3041990
    """
    valid = {"yes": True,   "y": True,  "ye": True,
             "no": False,     "n": False}

    if default == None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        print(question + prompt)
        choice = raw_input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            print "Please respond with 'yes' or 'no' (or 'y' or 'n').\n"

def curCardVal(card):
        # This might need to become a global function
    if card.suit == game.trump:
        if card.num == 11:  # card is right bower
            return card.num + 15
        else:
            return card.num + 10

    elif card.num == 11 and card.suit == offSuit(game.trump):
        # card is left bower
        return card.num + 14
    elif card.suit == game.lead:
        return card.num
    else:
        return 0

# This gets hypothetical card values
def hypo_curCardVal(card, trump):
    # This might need to become a global function
    if card.suit == trump:
        if card.num == 11:  # card is right bower
            return card.num + 15
        else:
            return card.num + 10

    elif card.num == 11 and card.suit == offSuit(trump):
        # card is left bower
        return card.num + 14
    else:
        return card.num
