# coding=utf-8

"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces.

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

from random import randint

punteggi = []
users = []
users_more_rank = []

def check_best_rank(users_more_rank):
    best_rank_for_player = []
    best_player = []
    for element in users_more_rank:
        if type(element) != list:
            rank_index = users_more_rank.index(element) + 1
            best_rank_for_player.append([element] + [min(users_more_rank[rank_index])])

    lower = 1000

    for element in best_rank_for_player:
        if element[1] < lower:
            lower = element[1]

    for element in best_rank_for_player:
        if element[1] == lower:
            best_player.append(element)

    return best_player


def checkUser(user):
    is_clone = False
    if len(users) > 0:
        for u in users:
            if u.lower() == user.lower():
                is_clone = True
                break

    return is_clone

def start_game_session():
    RN = randint(1,10)
    n = 0
    while n > -1:
        n += 1
        try:
            number = int(input("Choose a number from 1 to 10: "))
            if number < 1 or number > 10:
                raise ValueError
        except:
            print("You should choose a number from 1 to 10")
            print()
            n -= 1
            continue


        if number > RN:
            print("ADVICE: the random number is lower.")
            continue
        elif number < RN:
            print("ADVICE: the random number is higher.")
            continue
        elif number == RN:
            print("Good ! you caught the correct number at attempt number {}".format(n))
            print()
            break
    return n



def start_game():
    """Psuedo-code Hints

    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".

    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.

    ( You can add more features/enhancements if you'd like to. )
    """
    while True:
        try:
            username = input("What's your username? ")
            if len(username) < 3:
                raise ValueError
        except ValueError:
            print("Please, username must have at least 3 characters!")
            continue

        username = username.capitalize()
        if username in users:
            print()
            print("Nice to see you again {}!".format(username))
        else:
            users.append(username)
            users.append([])
            print()
            print("Welcome to HIGH-LOW Game {}!".format(username))
            print("""
            To be the WINNER at this game, you must guess the invisible Random Number 
            with fewer attempts! 
            If you exit from the game, all rankings will be delete!
            """)
        n = start_game_session()
        index_user = users.index(username)
        punteggi.append(n)
        users[index_user + 1].append(n)
        best_ranking = check_best_rank(users)

        if len(best_ranking) > 1:
            usernames = []
            rank = best_ranking[0][1]
            for user in best_ranking:
                usernames.append(user[0])
            print("==========BEST RANKING===========")
            print("These users are winning with the same score: {} attempts".format(rank))
            for u in usernames:
                print(u)
            print("=================================")
        else:
            print("==========BEST RANKING===========")
            print("{} is winning with a score of: {} attempts".format(best_ranking[0][0], best_ranking[0][1]))
            print("=================================")

        confirm = ""

        while (confirm != "n" and confirm != "y"):
            try:
                confirm = input("Do you want to continue playing? y/n ")
                confirm = confirm.lower()
                if confirm != "y" and confirm != "n":
                    raise ValueError
            except:
                print("You should write 'Y' if you want continue or 'N' if you want stop the game.")
                print()
            continue

        if confirm == "y":
            continue
        elif confirm == "n":
            break


if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()
















