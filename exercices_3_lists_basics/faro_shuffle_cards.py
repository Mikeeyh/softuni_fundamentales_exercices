deck_of_cards = input().split()
faro_shuffles_count = int(input())

for shuffle in range(faro_shuffles_count):
    final_deck = []
    middle_of_the_deck = len(deck_of_cards) // 2 #to receive int not float
    left_part = deck_of_cards[0:middle_of_the_deck] #can be write without '0'
    right_part = deck_of_cards[middle_of_the_deck:]

    for card_index in range(len(right_part)):
        final_deck.append(left_part[card_index])
        final_deck.append(right_part[card_index])
    deck_of_cards = final_deck
print(final_deck)