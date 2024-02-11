# How the Game Goes:
# 1) draw 2 for each
# 2) check for blackjack for each
# 3) ask player whether to draw or to pass
# 4) Draw:
#  go for a function that checks if he passes 21 and has Ace, if so Ace is modified
#  if he is above 21 and has no Ace he loses
#  if he is under 21 we ask draw or pass
# 5) Pass:
#  while pc is under 17 and under player, pc draws
#  go for a function that checks if pc passes 21 and has Ace, if so Ace is modified
#  if pc is above 21 and has no Ace, player wins
#  if pc = player, draw
#  if pc higher than player, pc wins


import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def continue_playing():
  decision = input("Do you want to play? Type 'y' or 'n'")
  if decision == "y":
    player_hand = random.choices(cards, k=2)
    pc_hand = random.choices(cards, k=2)
    print(f"Your cards: {player_hand}, score = {sum(player_hand)}.")
    print(f"Computer's first card: {pc_hand[0]}.")
    check_blackjack(player_hand, pc_hand)
    player_draw_card(player_hand, pc_hand)


def player_draw_card(player_hand, pc_hand):
  draw_another_card = input("Do you want to draw another card? type 'y' or 'n'.")
  if draw_another_card == "y":
    player_hand.append(random.choice(cards))
    modif_11(player_hand)
    print(f"Your cards: {player_hand}, score = {sum(player_hand)}.")
    print(f"Computer's first card: {pc_hand[0]}.")
    if sum(player_hand) > 21:
      printing_scores(player_hand, pc_hand)
      print("You lose.")
      continue_playing()
    elif sum(player_hand) < 21:
      player_draw_card(player_hand, pc_hand)
    else:
      pc_draw_card(player_hand, pc_hand)
  elif draw_another_card == "n":
    pc_draw_card(player_hand, pc_hand)


def pc_draw_card(player_hand, pc_hand):
  while sum(pc_hand) < 17 and sum(pc_hand) < sum(player_hand):
    pc_hand.append(random.choice(cards))
  modif_11(pc_hand)
  if sum(pc_hand) > 21 or sum(player_hand) > sum(pc_hand):
    printing_scores(player_hand, pc_hand)
    print("You win")
    continue_playing()
  elif sum(pc_hand) == sum(player_hand):
    printing_scores(player_hand, pc_hand)
    print("It's draw.")
    continue_playing()
  elif sum(pc_hand) > sum(player_hand):
    printing_scores(player_hand, pc_hand)
    print("You Lose.")
    continue_playing()


def check_blackjack(player_hand, pc_hand):
  if sum(player_hand) == 21:
    print("You win with a Blackjack.")
    continue_playing()
  elif sum(pc_hand) == 21:
    print("PC wins with a Blackjack.")
    continue_playing()


def modif_11(cards):
  if sum(cards) > 21 and 11 in cards:
    index_of_11 = cards.index(11)
    cards[index_of_11] = 1


def printing_scores(player_hand, pc_hand):
  print(f"Your final cards: {player_hand}, score = {sum(player_hand)}.")
  print(f"Computer's final hand: {pc_hand}, score = {sum(pc_hand)}.")


continue_playing()
