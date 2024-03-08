  # BlackJack

---

You can play the game [here](https://games.washingtonpost.com/games/blackjack) to get familiar with its rules, I wrote a brief about them below.

This game is a great application of:
- Logical `if` statements.
- `functions` with inputs.
- `random` module.
- `while` loops.

![blackjack_screenshot](https://github.com/Abdelrahman-Elsaudy/Blackjack/assets/158151388/a3ed0159-e85f-4208-8d0e-f5011e58164c)
---

## Game Rules:
Ace is 11, King, Queen and Jack are 10.
```
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
```
1) Draw 2 cards for the user and the pc, the user gets to see only one card of the pc's two cards.
2) Check for blackjack for each one (if the sum of the cards is 21).
3) If no, ask the user whether to draw or pass.
4) If the user chooses to draw another card:
- If the sum of user cards exceeds 21 and has Ace, Ace is modified to be equal 1 instead of 11.
```
def modify_11(either_hand):
    if sum(either_hand) > 21 and 11 in either_hand:
        index_of_11 = either_hand.index(11)
        either_hand[index_of_11] = 1
```
- If the user has no Ace and they exceed 21, they lose.
- If the user is still under 21, they are asked whether to draw or pass again.
5) If the user chooses to pass:
- While pc is under 17, pc draws.
- If pc passes 21 and has Ace, Ace is modified to be equal to 1 instead of 11.
- If pc has no Ace and exceeds 21, the user wins.
6) Compare both user and pc to determine: win, lose or draw.

---

_Credits to: 100-Days of Code Course on Udemy._