
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
    nums_list = [(x.strip()) for x in nums.split(" ") if len(x.strip()) > 0]
    return int(''.join(nums_list))


file1 = open('input.txt', 'r')
content = file1.readlines()

time = parse_input(content[0])
dist = parse_input(content[1])

result = resolve_total_wins(time, dist)
print(result)
