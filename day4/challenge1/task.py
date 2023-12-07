

def parseNumbers(numberString):
    return [x.strip() for x in numberString.split(" ") if len(x.strip()) > 0]

def getWinningNumbers(gameNumbers, ownNumbers):
    return [value for value in gameNumbers if value in ownNumbers]

def getCardScore(cardString):
    cardSplit = cardString.split(": ")
    split = cardSplit[1].split("|")
    gameNumbers = parseNumbers(split[0])
    ownNumbers =  parseNumbers(split[1])
    winningNumbers = getWinningNumbers(gameNumbers, ownNumbers)
    print (winningNumbers)
    if (len(winningNumbers)<=1):
        return len(winningNumbers)
    return  pow(2, len(winningNumbers)-1)


file1 = open('input.txt', 'r')
lines = file1.readlines()

sum = 0
for line in lines:
    cardScore = getCardScore(line)
    sum += cardScore

print(sum)
