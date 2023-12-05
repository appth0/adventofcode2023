

file1 = open('input.txt', 'r')
lines = file1.readlines()

sum = 0
for line in lines:
    numbers = [x for x in line if x.isnumeric()]
    num = int(str(numbers[0]) + str(numbers[-1]))
    print(num)
    sum += num

print("SUM: " + str(sum))

