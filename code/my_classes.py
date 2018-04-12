from my_globals import *
import AIs
import random

# holder and runner of the entire game


class Euchre():

    def __init__(self, logging_enabled = False, detail_log = None, overview_log = None):
        # initialize AI's here
        self.playerA1 = AIs.SimpleStat("PA1", "A")
        # self.playerA2 = AIs.RandomPlay("PA2")
        # self.playerB1 = AIs.RandomPlay("PB1")
        # self.playerB2 = AIs.RandomPlay("PB2")
        self.playerA2 = AIs.SimpleStat("PA2", "A")
        self.playerB1 = AIs.SimpleStat("PB1", "B")
        self.playerB2 = AIs.SimpleStat("PB2", "B")

        # make a list of the players for rotations
        self.players = [self.playerA1, self.playerB1,
                        self.playerA2, self.playerB2]

        self.playerA1.setRelations(self.playerA2, self.playerB1, self.playerB2)
        self.playerA2.setRelations(self.playerA1, self.playerB2, self.playerB1)
        self.playerB1.setRelations(self.playerB2, self.playerA1, self.playerA2)
        self.playerB2.setRelations(self.playerB1, self.playerA2, self.playerA1)

        # get a deep copy of all_cards for dealing
        self.deck = list(allcards[:])

        self.is_logging_enabled = logging_enabled
        if self.is_logging_enabled:
            self.detail_log = detail_log
            self.overview_log = overview_log

    def playGame(self, game_number):  # begins the first round
        # determine first dealer
        # start at last player so that the first rotate in playRound has the
        # first player deal
        game.dealer = self.playerB2

        # moved the multiple playRound calls into here
        # iterative instead of recursive
        while not self.hasWinner():
            self.playRound(game_number)
            for p in self.players:
                p.reset()
        self.endGame()

    def dealCards(self):
        random.shuffle(self.deck)  # mutates deck
        deal_index = self.players.index(game.dealer)

        # TODO: change dealing method to reflect actual game dealing
        for x in range(1, 5):
            self.players[(x + deal_index) % 4].setHand(self.deck[:5])
            self.deck = self.deck[5:]

    def rotateDeal(self):  # rotate the dealer
        # use this if game.dealer is a direct reference
        game.dealer = self.players[(self.players.index(game.dealer) + 1) % 4]

    def playRound(self, game_number):  # begins the next 5 tricks
        game.resetRound()
        self.rotateDeal()
        self.deck = list(allcards[:])
        self.dealCards()
        self.round_detail_log = ""
        self.round_overview_log = ""

        # prepare for round
        print 'Dealer: %s' % (game.dealer.name)
        game.caller = self.orderUpDealerSec()
        if game.caller:
            # TODO
            # have dealer pick up and discard
            game.trump = self.deck[0].suit
            print game.caller.name
            self.deck[0] = game.dealer.pickUp(self.deck[0])
        else:
            game.caller, game.trump = self.pickSuitSec(self.deck[0].suit)
            # TODO
            # stick the dealer
            pass

        for p in self.players:
            p.trumpIsSet()

        overview_log_trump_called = "%s,%s,%s" % (game.trump, game.caller.team_name, game.caller.name)
        self.round_overview_log = self.round_overview_log + overview_log_trump_called

        overview_log_player_hands = self.logPlayerHands()

        # play 5 tricks
        winner = self.players[(self.players.index(game.dealer) + 1) % 4]
        for x in range(5):
            winner = self.playTrick(winner)
            cards_played = game.center.keys()

            console_trick_end = "End of trick:\n%s, %s, %s, %s\nWinner:%s\n" % (
                cards_played[0], cards_played[1], cards_played[2], cards_played[3], winner.name)
            print console_trick_end

            detail_log_trick_end = "%s,%s,%s,%s,%s," % (
                cards_played[0], cards_played[1], cards_played[2], cards_played[3], winner.name)
            self.round_detail_log = self.round_detail_log + detail_log_trick_end

            for p in self.players:
                p.updateInfo(winner)

        # This method mutates self.round_detail_log
        self.allotScore()

        console_round_end = "End of round:\nTrump: %s\nCaller: %s\nScores A: %d B: %d\n" % (
            game.trump, game.caller.name, game.scoreA, game.scoreB)
        print console_round_end

        detail_log_round_meta_data = "%s,%s,%d,%d," % \
            (game.trump, game.caller.name, game.scoreA, game.scoreB)
        self.round_detail_log = str(game_number) + "," + detail_log_round_meta_data + self.round_detail_log

        self.round_overview_log = self.round_overview_log + "," + self.getWinningTeamName() + overview_log_player_hands
        self.round_overview_log = str(game_number) + "," + self.round_overview_log

        if self.is_logging_enabled:
            self.detail_log.log(self.round_detail_log)
            self.overview_log.log(self.round_overview_log)

    def playTrick(self, leader):
        game.resetTrick()

        # get the start card from leader
        # assume cards played are legal
        played = leader.playCard()
        game.center[played] = leader

        # handle the lead/left bower problem
        if played.num == 11 and played.suit == offSuit(game.trump):
            game.lead = offSuit(game.trump)
        else:
            game.lead = played.suit

        # play the trick
        leader_index = self.players.index(leader)
        for x in range(1, 4):
            played = self.players[(leader_index + x) % 4].playCard()
            game.center[played] = self.players[(leader_index + x) % 4]

        # return the winner of the trick
        win_card = self.getWinningCard()
        win_player = game.center[win_card]
        if win_player == self.playerA1 or win_player == self.playerA2:
            game.tricksA += 1
        else:
            game.tricksB += 1
        return win_player

    def allotScore(self):
        # simple rules used, no going alone
        if game.caller == self.playerA1 or game.caller == self.playerA2:  # caller is in team A
            c_team = "A"
            c_tricks = game.tricksA
        else:
            c_tricks = game.tricksB
            c_team = "B"

        # NOTE: we may or may not need this data in the long run
        detail_log_end_round_summary = "%s,%d,%d,%d" % (c_team, game.tricksA, game.tricksB, c_tricks)
        self.round_detail_log = self.round_detail_log + detail_log_end_round_summary

        # If the caller gets euchred
        if c_tricks < 3:
            if c_team == "A":
                game.scoreB += 2
            else:
                game.scoreA += 2
        # If the caller takes 3 or 4 tricks
        elif c_tricks < 5:
            if c_team == "A":
                game.scoreA += 1
            else:
                game.scoreB += 1
        # If the caller takes all 5 tricks
        else:
            if c_team == "A":
                game.scoreA += 2
            else:
                game.scoreB += 2

    def hasWinner(self):
        if game.scoreA >= 10:
            print "Team A Has won!"
            return True
        elif game.scoreB >= 10:
            print "Team B Has won!"
            return True
        else:
            return False

    def endGame(self):  # ends the game
        if game.scoreA >= 10:
            print "Players %s and %s have won!" % (self.playerA1.name, self.playerA2.name)
            # out.log("Players %s and %s have won!" %
            #         (self.playerA1.name, self.playerA2.name))
        elif game.scoreB >= 10:
            print "Players %s and %s have won!" % (self.playerB1.name, self.playerB2.name)
            # out.log("Players %s and %s have won!" %
            #         (self.playerB1.name, self.playerB2.name))
        print "With a score of %d to %d." % (game.scoreA, game.scoreB)
        # out.log("With a score of %d to %d." % (game.scoreA, game.scoreB))

        game.scoreA = 0
        game.scoreB = 0

    def getWinningCard(self):
        return sorted(game.center, key=curCardVal, reverse=True)[0]

        # temp = [(x, self.curCardVal(x)) for x in game.center]
        # best = temp[0][1]
        # bext_x = 0

        # for x in range(1, len(temp)):
        # if temp[x][1] > best:
        # best = temp[x][1]
        # best_x = x

        # return temp[x][0]

    def orderUpDealerSec(self):
        deal_index = self.players.index(game.dealer)
        for x in range(1, 5):
            cur_player = self.players[(deal_index + x) % 4]
            print cur_player.name,

            if cur_player.orderUp(self.deck[0]):
                placed = game.dealer.pickUp(self.deck[0])
                self.deck[0] = placed
                print 'called'
                return cur_player
            else:
                print 'passed'
                pass  # display that the player passed
        return None

    def pickSuitSec(self, out_suit):
        print
        print self.deck[0]
        for x in range(1, 5):
            cur_player = self.players[
                (self.players.index(game.dealer) + x) % 4]
            print cur_player.name,
            stuck = cur_player == game.dealer,

            picked = cur_player.pickSuit(out_suit, stuck)
            if picked:
                print 'picked'
                return self.players[(self.players.index(game.dealer) + x) % 4], picked
            else:
                print 'passed'
                pass  # display that the player passed
        return None

    def logPlayerHands(self):
        playerA1_hand = ",%s" % (self.playerA1.getHandCsv())
        playerB1_hand = ",%s" % (self.playerB1.getHandCsv())
        playerA2_hand = ",%s" % (self.playerA2.getHandCsv())
        playerB2_hand = ",%s" % (self.playerB2.getHandCsv())

        handCsv = "%s%s%s%s" % (playerA1_hand, playerB1_hand, playerA2_hand, playerB2_hand)
        return handCsv

    def getWinningTeamName(self):
        a_team_won = True if game.tricksA >= 3 else False
        return "A" if a_team_won else "B"
