

def get_question_mark_positions(l):
    return [i for i, x in enumerate(l) if x == '?']


def is_valid_arrangement(record, required_config):
    record_parts = [x for x in record.strip().split(".") if len(x) > 0]
    if len(record_parts) != len(required_config):
        return False
    for i, req in enumerate(required_config):
        if len(record_parts[i]) != req:
            return False
    return True


def get_valid_arrangements(record, required_config):
    question_mark_indices = [i for i, x in enumerate(record) if x == '?']
    if len(question_mark_indices) == 0:
        return 1 if is_valid_arrangement(record, required_config) else 0
    index = question_mark_indices[0]
    rec1 = record[:index] + "." + record[index + 1:]
    rec2 = record[:index] + "#" + record[index + 1:]
    return get_valid_arrangements(rec1, required_config) + get_valid_arrangements(rec2, required_config)


file = open('input.txt', 'r')
rows = list(map(lambda x: x.strip(), file.readlines()))

print("rows to check")
print(len(rows))

sum = 0
for row in rows:
    print(row)
    s = row.split(" ")
    record = s[0]
    required_config = [int(x) for x in s[1].split(",")]
    sum += get_valid_arrangements(record, required_config)

print(sum)