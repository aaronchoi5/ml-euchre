from my_globals import *
from my_classes import *
import AIs
import datetime


def main():
    logging_enabled = query_yes_no("Would you like to log these games?")
    game_count = 0
    total_games = 1

    if logging_enabled:
        now = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        detail_log_filename = 'logs/detail_%s.csv' % (now)
        detail_log = Logger(detail_log_filename)

        overview_log_filename = 'logs/overview_%s.csv' % (now)
        overview_log = Logger(overview_log_filename)

        detail_log.log("GAME,TRUMP,CALLER,A_PTS,B_PTS,PA1_1,PA2_1,PB1_1,PB2_1,WIN_1,PA1_2,PA2_2,PB1_2,PB2_2,WIN_2,PA1_3,PA2_3,PB1_3,PB2_3,WIN_3,PA1_4,PA2_4,PB1_4,PB2_4,WIN_4,PA1_5,PA2_5,PB1_5,PB2_5,WIN_5,CALL_TEAM,A_TRICKS,B_TRICKS,CALL_TEAM_TRICKS")
        overview_log.log("GAME,TRUMP,CALLER_TEAM,CALLER,WINNER_TEAM,PA1_C1,PA1_C2,PA1_C3,PA1_C4,PA1_C5,PA2_C1,PA2_C2,PA2_C3,PA2_C4,PA2_C5,PB1_C1,PB1_C2,PB1_C3,PB1_C4,PB1_C5,PB2_C1,PB2_C2,PB2_C3,PB2_C4,PB2_C5")

        while game_count < total_games:
            game = Euchre(logging_enabled, detail_log, overview_log)
            game.playGame(game_count)
            game_count = game_count + 1
    else:
        while game_count < total_games:
            game = Euchre(logging_enabled)
            game.playGame(game_count)
            game_count = game_count + 1

if __name__ == "__main__":
    main()
