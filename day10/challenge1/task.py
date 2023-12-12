
def find_s(map):
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == 'S':
                return i, j


def follow_pipe(field, coordinates, last_coordinates):
    x, y = coordinates
    x_last, y_last = last_coordinates
    if field[x][y] == 'S':
        return x + 1, y  # solution specific hack
    if field[x][y] == '-':
        return x, y + 1 if y_last == y - 1 else y - 1
    if field[x][y] == '|':
        return (x + 1, y) if x_last == x - 1 else (x - 1, y)
    if field[x][y] == '7':
        return (x + 1, y) if y_last == y - 1 else (x, y - 1)
    if field[x][y] == 'J':
        return (x - 1, y) if y_last == y - 1 else (x, y - 1)
    if field[x][y] == 'L':
        return (x, y + 1) if x_last == x - 1 else (x - 1, y)
    if field[x][y] == 'F':
        return (x, y + 1) if x_last == x + 1 else (x + 1, y)


file = open('input.txt', 'r')
map = file.readlines()
s_coordinates = find_s(map)
current_coordinates = follow_pipe(map, s_coordinates, (0, 0))
last_coordinates = s_coordinates

steps = 1
while map[current_coordinates[0]][current_coordinates[1]] != 'S':
    next_coordinates = follow_pipe(map, current_coordinates, last_coordinates)
    last_coordinates = current_coordinates
    current_coordinates = next_coordinates
    steps += 1

print(steps / 2)
