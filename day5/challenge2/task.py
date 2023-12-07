def getOverlappingRange(range1, range2):
    r1Begin, r1End = range1
    r2Begin, r2End = range2

    minVal = max(r1Begin, r2Begin)
    maxVal = min(r1End, r2End)
    if minVal < maxVal:
        return [(minVal, maxVal)]
    else:
        return []

def getNotOverlappingRanges(range1, ranges):
    if len(ranges) < 1:
        return [range1]
    overlaps = []
    for x in ranges:
        overlaps += getOverlappingRange(range1, x)
    overlaps.sort()
    result = []

    for i, overlap in enumerate(overlaps[1:]):
        result.append((overlaps[i][1], overlap[0]))

    if len(overlaps) > 0:
        result.append((range1[0], overlaps[0][0]))
        result.append((overlaps[-1][1], range1[1]))

    result = [x for x in result if x[0] != x[1]]
    return result

def resolveSeedRanges(seedValues):
    ranges = []
    while (len(seedValues) > 1):
        seedValue = seedValues.pop(0)
        seedRange = seedValues.pop(0)
        ranges.append((seedValue, seedValue + seedRange))
    return ranges

def parseTable(tableString):
    s = tableString.split(":\n")
    tableContentsSplit = s[1]
    table = [t.split(" ") for t in tableContentsSplit.split("\n") if len(t.strip()) > 0]
    return table

def resolveDestinationValueRanges(table, input_range):
    destination_ranges = []
    found_overlaps = []

    for row in table:
        destinationValue = int(row[0])
        sourceRowValue = int(row[1])
        sourceRowRange = int(row[2])
        sourceRowMax   = sourceRowValue + sourceRowRange
        sourceRange = (sourceRowValue, sourceRowMax)

        overlaps = getOverlappingRange(sourceRange, input_range)
        found_overlaps += overlaps

        for overlap in overlaps:
            delta = (overlap[0] - sourceRowValue)
            overlap_size = overlap[1] - overlap[0]
            destination_ranges.append((destinationValue + delta, destinationValue + delta + overlap_size))

    not_overlapping_ranges = getNotOverlappingRanges(input_range, found_overlaps)
    for no_overlap in not_overlapping_ranges:
        destination_ranges.append(no_overlap)

    return destination_ranges

def resolveDestinationValueRangesForMultipleRanges(table, input_ranges):
    result_ranges = []
    for input_range in input_ranges:
        result_ranges += resolveDestinationValueRanges(table, input_range)
    return result_ranges


file1 = open('input.txt', 'r')
content = file1.read()

contentSplit = content.split("\n\n")
seedString = contentSplit[0]
seedValuesString = seedString.split(": ")[1]
seedValues = [int(x.strip()) for x in seedValuesString.split(" ") if len(x.strip()) > 0]
tablesSplit = contentSplit[1:]

seedRanges = resolveSeedRanges(seedValues)

seedToSoil   = parseTable(tablesSplit[0])
soilToFert   = parseTable(tablesSplit[1])
fertToWater  = parseTable(tablesSplit[2])
waterToLight = parseTable(tablesSplit[3])
lightToTemp  = parseTable(tablesSplit[4])
tempToHum    = parseTable(tablesSplit[5])
humToLoc     = parseTable(tablesSplit[6])

minLocationValue = 9999999999

for seedRange in seedRanges:
    dest = [seedRange]
    dest = resolveDestinationValueRangesForMultipleRanges(seedToSoil, dest)
    dest = resolveDestinationValueRangesForMultipleRanges(soilToFert, dest)
    dest = resolveDestinationValueRangesForMultipleRanges(fertToWater, dest)
    dest = resolveDestinationValueRangesForMultipleRanges(waterToLight, dest)
    dest = resolveDestinationValueRangesForMultipleRanges(lightToTemp, dest)
    dest = resolveDestinationValueRangesForMultipleRanges(tempToHum, dest)
    dest = resolveDestinationValueRangesForMultipleRanges(humToLoc, dest)

    min_val = min([x[0] for x in dest])
    minLocationValue = min(minLocationValue, min_val)

print(minLocationValue)




