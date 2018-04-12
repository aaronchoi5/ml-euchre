from game_utils import GameUtils

# This file is meant for smoke testing code

utils = GameUtils()
utils.read_game('game1_play_data.csv')

# utils.print_game()

# r1 = utils.get_round_data(1)
# print(r1)
# utils.print_data(r1)

# r1t3p4 = utils.get_trick_data(r1, 3, 4)
# utils.print_data(r1t3p4)

r1t3p4 = utils.get_current_state(1, 3, 4)
# utils.print_data(r1t3p4)
utils.print_game()
