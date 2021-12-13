import numpy as np


class ConnectFourGame:
    def __init__(self):
        self.x = 7
        self.y = 6
        self.win_condition = np.array([1, 1, 1, 1])
        self.field = np.zeros([self.y, self.x])

    def set_game_marker(self, xpos, ypos, player):
        self.field[ypos][xpos] = player

    def scan_field(self):
        # checking game field x = 7, y = 6
        # print(field)
        winner_found = self.check_wincondition(self.field, self.x, self.y)

        # check gamefield with transponed matrix
        # therefore rows will be columns
        # => logic for check could be reused
        if not winner_found:
            winner_found = self.check_wincondition(self.field.T, self.y, self.x)

        if not winner_found:
            transformed_field = self.transform_game_field(self.field)
            winner_found = self.check_wincondition(transformed_field, self.x, self.y)

        if not winner_found:
            transformed_field = self.transform_game_field(self.field)
            winner_found = self.check_wincondition(transformed_field.T, self.y, self.x)

        return winner_found

    def check_wincondition(self, game_field, x_max, y_max):
        for xpos in range(0, (x_max-3)):
            for ypos in range(0, y_max):
                if np.array_equal(game_field[ypos, xpos: (xpos+4)], self.win_condition):
                    return True

        return False

    def transform_game_field(self, game_field):
        fields_to_move = self.y-1
        columns_to_add = np.zeros([self.y, fields_to_move])
        transformed_field = np.hstack((game_field, np.atleast_2d(columns_to_add)))
        print(transformed_field)

        for i in range(fields_to_move, -1, -1):
            row_result = np.roll(transformed_field[i], (fields_to_move-i))
            transformed_field[i] = row_result

        print(transformed_field)
        return transformed_field
