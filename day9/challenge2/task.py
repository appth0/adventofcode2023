def get_previous_in_row(history):
    if len(set(history)) == 1:
        return history[0]
    deltas = [history[i+1] - history[i] for i in range(len(history)-1)]
    return history[0] - get_previous_in_row(deltas)


file = open('input.txt', 'r')
content = file.readlines()
histories = [[int(x) for x in h.strip().split(" ") if len(x.strip()) > 0] for h in content if len(h.strip()) > 0]
print(sum([get_previous_in_row(history) for history in histories]))
