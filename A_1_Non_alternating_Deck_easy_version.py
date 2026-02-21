t = int(input())
for _ in range(t):
    n = int(input())
    alice_cards = 0
    bob_cards = 0
    remaining_cards = n
    i = 1
    while remaining_cards > 0:
        if remaining_cards > i + i + 4:
            alice_cards += i
            remaining_cards -= i
            i += 4 
            bob_cards += i 
            remaining_cards -= i
            i += 4
        elif remaining_cards > i:
            alice_cards += i
            remaining_cards -= i
            bob_cards += remaining_cards
            remaining_cards = 0
        else:
            alice_cards += remaining_cards

            remaining_cards = 0

    print(alice_cards, bob_cards)



