import numpy as np

# init game field
x = 7
y = 6
win_condition = np.array([1, 1, 1, 1])

field = np.zeros([y, x])

# init test szenario
for i in range(2, 5):
    field[i][5] = 1

print(field)


def set_game_marker(xpos, ypos, player):
    field[ypos][xpos] = player


def scan_field():
    for xpos in range(0, (x-3)):
        for ypos in range(0, y):
            print(field[ypos, xpos: (xpos+4)])
            if np.array_equal(field[ypos, xpos: (xpos+4)], win_condition):
                return True

    # TODO: add reshape and then searching for the vertical winner

    return False


set_game_marker(5, 1, 1)
print(field)
result = scan_field()
print(result)
