import numpy as np

# init game field
x = 7
y = 6
win_condition = np.array([1, 1, 1, 1])

field = np.zeros([y, x])

# init test szenario
# for i in range(2, 5):
#    field[i][5] = 1

field[1][2] = 1
field[2][3] = 1
field[3][4] = 1


def set_game_marker(xpos, ypos, player):
    field[ypos][xpos] = player


def scan_field():
    # checking game field x = 7, y = 6
    # print(field)
    winner_found = check_wincondition(field, x, y)

    # check gamefield with transponed matrix
    # therefore rows will be columns
    # => logic for check could be reused
    if not winner_found:
        winner_found = check_wincondition(field.T, y, x)
        # print(field.T)

    if not winner_found:
        # transformed_field = np.reshape(field, (8, 9))
        # print(transformed_field)#
        transform_game_field()

    return winner_found


def check_wincondition(game_field, x_max, y_max):
    for xpos in range(0, (x_max-3)):
        for ypos in range(0, y_max):
            if np.array_equal(game_field[ypos, xpos: (xpos+4)], win_condition):
                return True

    return False


def transform_game_field():
    fields_to_move = y-1
    columns_to_add = np.zeros([y, fields_to_move])
    transformed_field = np.hstack((field, np.atleast_2d(columns_to_add)))
    print(transformed_field)

    for i in range(fields_to_move, -1, -1):
        row_result = np.roll(transformed_field[i], (fields_to_move-i))
        transformed_field[i] = row_result

    print(transformed_field)
    return transformed_field


set_game_marker(1, 0, 1)
result = scan_field()
print(result)
