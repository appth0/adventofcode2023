
def parseTable(tableString):
    s = tableString.split(":\n")
    tableContentsSplit = s[1]
    table = [t.split(" ") for t in tableContentsSplit.split("\n") if len(t.strip()) > 0]
    return table


def resolveDestinationValue(table, inputValue):
    for row in table:
        destinationValue = int(row[0])
        sourceRowValue = int(row[1])
        sourceRowRange = int(row[2])
        sourceRowMax   = sourceRowValue + sourceRowRange
        if (inputValue >= sourceRowValue and inputValue <= sourceRowMax):
            difference = inputValue - sourceRowValue
            return destinationValue + difference
    return inputValue


file1 = open('input.txt', 'r')
content = file1.read()

contentSplit = content.split("\n\n")
seedString = contentSplit[0]
seedValuesString = seedString.split(": ")[1]
seeds = [int(x.strip()) for x in seedValuesString.split(" ") if len(x.strip()) > 0]
tablesSplit = contentSplit[1:]

seedToSoil   = parseTable(tablesSplit[0])
soilToFert   = parseTable(tablesSplit[1])
fertToWater  = parseTable(tablesSplit[2])
waterToLight = parseTable(tablesSplit[3])
lightToTemp  = parseTable(tablesSplit[4])
tempToHum    = parseTable(tablesSplit[5])
humToLoc     = parseTable(tablesSplit[6])

locationValues = []

for s in seeds:
    dest = s
    dest = resolveDestinationValue(seedToSoil, dest)
    dest = resolveDestinationValue(soilToFert, dest)
    dest = resolveDestinationValue(fertToWater, dest)
    dest = resolveDestinationValue(waterToLight, dest)
    dest = resolveDestinationValue(lightToTemp, dest)
    dest = resolveDestinationValue(tempToHum, dest)
    dest = resolveDestinationValue(humToLoc, dest)
    locationValues.append(dest)

print(min(locationValues))




