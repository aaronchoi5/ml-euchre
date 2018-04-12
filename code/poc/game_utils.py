import csv

class GameUtils:
    game_data_headers = []
    game_data = []
    data_spacing = []

    def read_game(self, filepath):
        header_row_num = 0
        row_num = 0

        with open(filepath, 'r') as game_file:
            game_reader = csv.reader(game_file)

            for row in game_reader:
                if len(self.game_data_headers) == 0:
                    self.game_data_headers = row

                    for header in self.game_data_headers:
                        tabs_needed = (int)(len(header) / 7) + 1
                        # print('%s: %d' % (header, tabs_needed))
                        self.data_spacing.append('\t' * tabs_needed)

                    row_num += 1
                else:
                    self.game_data.append(row)

    def get_current_state(self, round, trick, player):
        round_data = self.get_round_data(round)
        return self.get_trick_data(round_data, trick, player)

    # FIXME: still a couple spacing bugs
    def print_game(self):
        self.print_data(self.game_data)

    def print_data(self, data_subset):
        print('\t'.join(self.game_data_headers))

        for data_row in data_subset:
            i = 0
            str = ''
            for data_element in data_row:
                str += data_element + self.data_spacing[i]
                i += 1
            print(str)

    def get_header_index(self, header_name):
        name = header_name.strip().lower()
        i = 0
        for header in self.game_data_headers:
            if header.lower() == name:
                return i
            else:
                i += 1

    def get_round_data(self, round):
        i_round = self.get_header_index('Round')

        round_data = []

        for row in self.game_data:
            if (int)(row[i_round]) == round:
                round_data.append(row)
            elif (int)(row[i_round]) > round:
                break

        return round_data

    def get_trick_data(self, round_data, trick, player):
        i_trick = self.get_header_index('Trick')
        i_player = self.get_header_index('Player')

        trick_data = []

        for row in round_data:
            if (int)(row[i_trick]) < trick:
                trick_data.append(row)
            elif (int)(row[i_trick]) == trick and (int)(row[i_player]) < player:
                trick_data.append(row)
            else:
                break

        return trick_data
