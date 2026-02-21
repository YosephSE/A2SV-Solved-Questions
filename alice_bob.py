from math import ceil
t = int(input())
for _ in range(t):
    n = int(input())
    alice_cards = [0, 0]
    bob_cards = [0, 0]
    remaining_cards = n
    i = 1
    while remaining_cards > 0:
        if remaining_cards > i + i + 4:
            if i % 2 == 1:
                alice_cards[0] += ceil(i / 2)
                alice_cards[1] += int(i // 2)
                remaining_cards -= i
                i += 4 
                bob_cards[0] += ceil(i / 2) 
                bob_cards[1] += int(i // 2)
                remaining_cards -= i
                i += 4
            else:
                alice_cards[0] += int(i // 2)
                alice_cards[1] += ceil(i / 2)
                remaining_cards -= i
                i += 4 
                bob_cards[0] += int(i // 2)
                bob_cards[1] += ceil(i / 2) 
                remaining_cards -= i
                i += 4

        elif remaining_cards > i:
            if i % 2 == 1:
                alice_cards[0] += ceil(i / 2)
                alice_cards[1] += int(i // 2)
                remaining_cards -= i
                bob_cards[0] += ceil(remaining_cards / 2)
                bob_cards[1] += int(remaining_cards // 2)
                remaining_cards = 0
            else:                
                alice_cards[0] += int(i / 2)
                alice_cards[1] += int(i / 2)
                remaining_cards -= i
                bob_cards[1] += ceil(remaining_cards / 2)
                bob_cards[0] += int(remaining_cards // 2)


        else:
            if i % 2 == 1:
                alice_cards[0] += ceil(remaining_cards / 2)
                alice_cards[1] += int(remaining_cards // 2)
                remaining_cards = 0
            else:
                alice_cards[0] += int(remaining_cards // 2)
                alice_cards[1] += ceil(remaining_cards / 2)
                remaining_cards = 0

    print(alice_cards[0], alice_cards[1], bob_cards[0], bob_cards[1])



