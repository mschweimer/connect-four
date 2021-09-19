import numpy as np

# init game field
x = 7
y = 6

field = np.zeros([y, x])

# init test szenario
for i in range(2, 5):
    field[3][i] = 1

print(field)


def set_game_marker(xpos, ypos, player):
    field[ypos][xpos] = player


def scan_field():
    for xpos in range(0, (x-3)):
        for ypos in range(0, y):
            print(field[ypos, xpos: (xpos+4)])
            if np.array_equal(field[ypos, xpos: (xpos+4)], [1, 1, 1, 1]):
                return True

    return False


set_game_marker(5, 3, 1)
print(field)
result = scan_field()
print(result)
