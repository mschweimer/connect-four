import numpy as np

# init game field
X = 7
Y = 6
win_condition = np.array([1, 1, 1, 1])

field = np.zeros([Y, X])


def set_game_marker(xpos, ypos, player):
    field[ypos][xpos] = player


def scan_field():
    # checking game field x = 7, y = 6
    # print(field)
    winner_found = check_wincondition(field, X, Y)

    # check gamefield with transponed matrix
    # therefore rows will be columns
    # => logic for check could be reused
    if not winner_found:
        winner_found = check_wincondition(field.T, Y, X)

    if not winner_found:
        transformed_field = transform_game_field(field)
        winner_found = check_wincondition(transformed_field, X, Y)

    if not winner_found:
        transformed_field = transform_game_field(field)
        winner_found = check_wincondition(transformed_field.T, Y, X)

    return winner_found


def check_wincondition(game_field, x_max, y_max):
    for xpos in range(0, (x_max-3)):
        for ypos in range(0, y_max):
            if np.array_equal(game_field[ypos, xpos: (xpos+4)], win_condition):
                return True

    return False


def transform_game_field(game_field):
    fields_to_move = Y-1
    columns_to_add = np.zeros([Y, fields_to_move])
    transformed_field = np.hstack((game_field, np.atleast_2d(columns_to_add)))
    print(transformed_field)

    for i in range(fields_to_move, -1, -1):
        row_result = np.roll(transformed_field[i], (fields_to_move-i))
        transformed_field[i] = row_result

    print(transformed_field)
    return transformed_field
