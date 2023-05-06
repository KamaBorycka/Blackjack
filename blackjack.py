import os
from random import choice

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
    """Return a random 2 cards from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_card = choice(cards)
    return random_card


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "You lose, you went over"
    if user_score == computer_score:
        return "Draw 🙈"
    elif computer_score == 0:
        return "Computer has Blackjack 😢"
    elif user_score == 0:
        return "Win, you have blackjack 🥳"
    elif user_score > 21:
        return "You lose, your score is over 21 😞"
    elif computer_score > 21:
        return "You win, computer score is over 21 😁"
    elif user_score > computer_score:
        return "You win 👍🏻"
    else:
        return "You lose 😔"


def play_game():
    user_cards = []
    computer_cards = []
    playing = True

    for card in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while playing:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards:{user_cards} and your score: {user_score}")
        print(f"Computer card:{computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            playing = False
        else:
            draw_card = input("Do you want to draw a card? ")
            if draw_card == "yes":
                user_cards.append(deal_card())
                user_score = calculate_score(user_cards)
            else:
                playing = False

    while computer_score < 17 and computer_score != 0:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Computer final cards:{computer_cards} and final score {computer_score}")

    print(compare(user_score=user_score, computer_score=computer_score))


while input("Do you want to play the game? ").lower() == "yes":
    os.system("clear")
    play_game()
