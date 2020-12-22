from collections import deque


def one(lines):
    cards = []
    for i, player in enumerate(lines.split('\n\n')):
        cards.append(deque(map(int, player.strip().splitlines()[1:])))

    while len(cards[0]) > 0 and len(cards[1]) > 0:
        cur_cards = [cards[0].popleft(), cards[1].popleft()]
        if cur_cards[0] > cur_cards[1]:
            winner = 0
        else:
            winner = 1

        cards[winner].append(cur_cards.pop(winner))
        cards[winner].append(cur_cards.pop())

    if len(cards[0]) > 0:
        winner = 0
    else:
        winner = 1

    ans = 0
    for i, card in enumerate(reversed(cards[winner])):
        ans += (i + 1) * card
    return ans


def two(lines):
    cards = []
    for i, player in enumerate(lines.split('\n\n')):
        cards.append(deque(map(int, player.strip().splitlines()[1:])))

    def play(cards):
        old_rounds = set()
        while len(cards[0]) > 0 and len(cards[1]) > 0:
            cards_tuple = list(map(tuple, cards))
            if cards_tuple[0] in old_rounds or cards_tuple[1] in old_rounds:
                return 0
            old_rounds.add(cards_tuple[0])
            old_rounds.add(cards_tuple[1])

            cur_cards = [cards[0].popleft(), cards[1].popleft()]
            if len(cards[0]) >= cur_cards[0] and len(cards[1]) >= cur_cards[1]:
                sub_cards0 = list(cards[0])[:cur_cards[0]]
                sub_cards1 = list(cards[1])[:cur_cards[1]]
                winner = play([deque(sub_cards0), deque(sub_cards1)])
            else:
                if cur_cards[0] > cur_cards[1]:
                    winner = 0
                else:
                    winner = 1

            cards[winner].append(cur_cards.pop(winner))
            cards[winner].append(cur_cards.pop())
        if len(cards[0]) > 0:
            return 0
        else:
            return 1

    winner = play(cards)

    ans = 0
    for i, card in enumerate(reversed(cards[winner])):
        ans += (i + 1) * card
    return ans


if __name__ == '__main__':
    with open('inputs/22.txt') as f:
        lines = f.read().strip()
    print(one(lines))
    print(two(lines))
