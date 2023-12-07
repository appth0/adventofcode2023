from functools import reduce

def parseNumbers(numberString):
    return [x.strip() for x in numberString.split(" ") if len(x.strip()) > 0]

def getWinningNumbers(gameNumbers, ownNumbers):
    return [value for value in gameNumbers if value in ownNumbers]

def getWinningNUmbersCount(cardString):
    cardSplit = cardString.split(": ")
    split = cardSplit[1].split("|")
    gameNumbers = parseNumbers(split[0])
    ownNumbers =  parseNumbers(split[1])
    winningNumbers = getWinningNumbers(gameNumbers, ownNumbers)
    return len(winningNumbers)


file1 = open('input.txt', 'r')
lines = file1.readlines()

winningNumbersCountList = []
cardsCount = []
for line in lines:
    winningNumbersCount = getWinningNUmbersCount(line)
    winningNumbersCountList.append(winningNumbersCount)
    cardsCount.append(1)

row = 0
for winningNumbers in winningNumbersCountList:
    for x in range(int(winningNumbers)):
        for i in range(int(cardsCount[row])):
            if (row + x + 1) < len(cardsCount):
                cardsCount[row + x + 1] += 1
    row += 1

sum = reduce(lambda x, y: x+y, cardsCount)

print(sum)