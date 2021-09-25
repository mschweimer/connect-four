import numpy as np

# init game field
x = 7
y = 6
win_condition = np.array([1, 1, 1, 1])

field = np.zeros([y, x])

# init test szenario
for i in range(2, 5):
    field[i][5] = 1


def set_game_marker(xpos, ypos, player):
    field[ypos][xpos] = player


def scan_field():
    # checking game field x = 7, y = 6
    winner_found = check_wincondition(field, x, y)

    # check gamefield with transponed matrix
    # therefore rows will be columns
    # => logic for check could be reused
    if not winner_found:
        winner_found = check_wincondition(field.T, y, x)

    return winner_found


def check_wincondition(game_field, x_max, y_max):
    for xpos in range(0, (x_max-3)):
        for ypos in range(0, y_max):
            if np.array_equal(game_field[ypos, xpos: (xpos+4)], win_condition):
                return True

    return False


set_game_marker(5, 1, 1)
print(field)
print(field.T)
result = scan_field()
print(result)
