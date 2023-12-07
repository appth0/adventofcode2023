
def wins_game(time, distance, button_press_time):
    time_left = time - button_press_time
    speed = button_press_time
    if time_left * speed > distance:
        return True
    return False


def resolve_total_wins(time, distance):
    wins = [x for x in range(time) if wins_game(time, distance, x)]
    return len(wins)


def parse_input(line):
    nums = line.split(": ")[1]
    return [int(x.strip()) for x in nums.split(" ") if len(x.strip()) > 0]


file1 = open('input.txt', 'r')
content = file1.readlines()

times = parse_input(content[0])
dists = parse_input(content[1])
result = 1

for i, x in enumerate(times):
    result *= resolve_total_wins(times[i], dists[i])

print(result)