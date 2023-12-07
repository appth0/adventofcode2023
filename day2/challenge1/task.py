

def getGameId(line):
    return int((line.split(":")[0]).split(" ")[1])

def getQubesFromDraw(draw):
    qDraws = draw.split(", ")
    colNum = {}
    for q in qDraws:
        colNum[(q.split(" ")[1]).strip()] = int(q.split(" ")[0])
    print(colNum)
    return colNum

def isValidDraw(draw):
    print(draw)
    if draw.get("red", 0) <=12 and draw.get("green", 0) <=13 and draw.get("blue", 0) <=14:
        return True
    return False

def isValidGame(gameString):
    drawString = gameString.split(": ")[1]
    draws = drawString.split("; ")
    for draw in draws:
        if not isValidDraw(getQubesFromDraw(draw)):
            return False
    return True
        
file1 = open('input.txt', 'r')
lines = file1.readlines()

sum = 0
for line in lines:
    if (isValidGame(line)):
        gameId = getGameId(line)
        print(gameId)
        sum += gameId

print(sum)