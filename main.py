# How the Game Goes:
# The deck of cards is [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10], Ace is 11, King, Queen and Jack are 10.
# 1) Draw 2 cards for the user and the pc, the user gets to see only one card of the pc's two cards.
# 2) Check for blackjack for each one (if the sum of the cards is 21).
# 3) If no, ask the user whether to draw or pass.
# 4) If the user chooses to draw another card:
#      If the sum of user cards exceeds 21 and has Ace, Ace is modified to be equal 1 instead of 11.
#      If the user has no Ace and they exceed 21, they lose.
#      If the user is still under 21, they are asked whether to draw or pass again.
# 5) If the user chooses to pass:
#      While pc is under 17, pc draws.
#      If pc passes 21 and has Ace, Ace is modified to be equal to 1 instead of 11.
#      If pc has no Ace and exceeds 21, the user wins.
# 6) Compare both user and pc to determine: win, lose or draw.


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
        player_draw(player_hand, pc_hand)


def player_draw(player_hand, pc_hand):
    draw_choice = input("Do you want to draw another card? type 'y' or 'n'.")
    if draw_choice == "y":
        player_hand.append(random.choice(cards))
        modify_11(player_hand)
        print(f"Your cards: {player_hand}, score = {sum(player_hand)}.")
        print(f"Computer's first card: {pc_hand[0]}.")
        if sum(player_hand) > 21:
            printing_scores(player_hand, pc_hand)
            print("You lose.")
            continue_playing()
        elif sum(player_hand) < 21:
            player_draw(player_hand, pc_hand)
        else:
            pc_draw_card(player_hand, pc_hand)
    elif draw_choice == "n":
        pc_draw_card(player_hand, pc_hand)


def pc_draw_card(player_hand, pc_hand):
    while sum(pc_hand) < 17:
        pc_hand.append(random.choice(cards))
    modify_11(pc_hand)
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


def modify_11(either_hand):
    if sum(either_hand) > 21 and 11 in either_hand:
        index_of_11 = either_hand.index(11)
        either_hand[index_of_11] = 1


def printing_scores(player_hand, pc_hand):
    print(f"Your final cards: {player_hand}, score = {sum(player_hand)}.")
    print(f"Computer's final hand: {pc_hand}, score = {sum(pc_hand)}.")


continue_playing()
