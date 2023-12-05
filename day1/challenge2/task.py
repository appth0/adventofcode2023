
def replaceNumStringsWithNum(string):
    mapping = [
        ("one", "o1ne"),
        ("two", "t2wo"),
        ("three", "t3hree"),
        ("four", "f4our"),
        ("five", "f5ive"),
        ("six", "s6ix"),
        ("seven", "s7even"),
        ("eight", "e8ight"),
        ("nine", "n9ine")
    ]
    for k, v in mapping:
        string = string.replace(k, v)
    return string

file1 = open('input.txt', 'r')
lines = file1.readlines()

sum = 0
c = 1
for line in lines:
    line = replaceNumStringsWithNum(line)
    numbers = [x for x in line if x.isnumeric()]
    num = int(str(numbers[0]) + str(numbers[-1]))
    sum += num
    c += 1


print("SUM: " + str(sum))