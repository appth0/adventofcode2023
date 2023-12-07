import functools

class CamelCard:

    def __init__(self, hand, bid):
        self.hand = hand
        self.bid = bid

    def count_card_occurrences(self):
        unique = set(self.hand)
        occurrences = []
        for u in unique:
            count = 0
            for c in self.hand:
                if c == u:
                    count += 1
            occurrences.append(count)
        occurrences.sort(reverse=True)
        return occurrences

    def get_hand_type(self):
        occurrences = self.count_card_occurrences()
        if len(set(self.hand)) == 1:
            return 7
        if len(set(self.hand)) == 2 and occurrences[0] == 4:
            return 6
        if len(set(self.hand)) == 2:
            return 5
        if len(set(self.hand)) == 3 and occurrences[0] == 3:
            return 4
        if len(set(self.hand)) == 3:
            return 3
        if len(set(self.hand)) == 4:
            return 2
        if len(set(self.hand)) == 5:
            return 1

    def get_highest_possible_type_with_joker(self):
        curr_hand = self.hand
        possible_joker_values = ["2", "3", "4", "5", "6", "7", "8", "8", "9", "T", "Q", "K", "A"]
        max_type = 1
        for joker_val in possible_joker_values:
            self.hand = curr_hand.replace("J", joker_val)
            score = self.get_hand_type()
            if score > max_type:
                max_type = score
        self.hand = curr_hand
        return max_type

    def get_hand_in_hex(self):
        mapping = [("T", "a"), ("J", "1"), ("Q", "c"), ("K", "d"), ("A", "e")]
        hexhand = self.hand
        for k, v in mapping:
            hexhand = hexhand.replace(k, v)
        return hexhand

    def __str__(self):
        return str(((self.hand, self.bid)))


def compare_camel_cards(c1, c2):
    score1 = c1.get_highest_possible_type_with_joker()
    score2 = c2.get_highest_possible_type_with_joker()
    if (score1 == score2):
        value1 = int(c1.get_hand_in_hex(), 16)
        value2 = int(c2.get_hand_in_hex(), 16)
        if (value1 > value2):
            return 1
        return -1
    if (score1 > score2):
        return 1
    return -1

def parse_cards(lines):
    res = []
    for line in lines:
        spl = [x for x in line.split(" ") if len(x) > 0]
        res.append(CamelCard(spl[0], int(spl[1])))
    return res


file1 = open('input.txt', 'r')
content = file1.readlines()

ccards = parse_cards(content)
ccards.sort(key=functools.cmp_to_key(compare_camel_cards))

sum = 0
for i, camel_card in enumerate(ccards):
    rank = i+1
    sum += camel_card.bid * rank

print(sum)
