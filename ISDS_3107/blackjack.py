import random

card_values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
sum = card
turn = "hit"
hand = [card]

while turn == "hit":
  next_card = random.choice(card_values)
  hand.append(next)
  print("You were given card: (card)")
  sum += card
  if sum < 21:
    turn = input("What do you want to do? (hit or stop) ")
  print("You currently have: " + str(sum))
  turn = input("What do you want to do? ")
    else: 
        turn = "stop"

if sum == 21:
  print("You win!")
elif sum > 21:
    print("You went over 21!")
else:
  print("You stopped at: " + str(sum))