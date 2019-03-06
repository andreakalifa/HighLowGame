# coding=utf-8

from random import randint

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

def start_game():
    RN = randint(1,10)
    n = 0
    while n > -1:
        n += 1
        try:
            number = int(input("Scegli un numero tra 1 e 10: "))
            if number < 1 or number > 10:
                raise ValueError
        except:
            print("Dovresti scegliere un numero tra 1 e 10")
            n -= 1
            continue


        if number > RN:
            print("Il numero è più basso.")
            continue
        elif number < RN:
            print("Il numero è più alto.")
            continue
        elif number == RN:
            print("Bravo! Hai azzeccato al tentativo {}".format(n))
            break
    return n

punteggi = []
users = []
users_more_rank = []
best_ranking = []


while True:

    username = input("What's your username? ")
    if username in users:
        print("Nice to see you again {}!".format(username))
    else:
        users.append(username)
        users.append([])
        print("Welcome to HIGH-LOW Game {}!".format(username))
    n = start_game()
    index_user = users.index(username)
    punteggi.append(n)
    users[index_user + 1].append(n)
    print(check_best_rank(users))

    print(users)
    print("Il miglior punteggio è stato fatto in {} tentativi".format(min(punteggi)))
    confirm = ""
    confirmationY = confirm.capitalize() != "Y"
    confirmationN = confirm.capitalize() != "N"
    while (confirm.capitalize() != "N" and confirm.capitalize() != "Y"):
       try:
          confirm = input("Vuoi continuare? y/n ")
          if confirm.capitalize() != "Y" and confirm.capitalize() != "N":
              raise ValueError
       except:
           print("Dovresti inserire Y se vuoi continuare o N se vuoi abbandonare.")
       continue

    if confirm.capitalize() == "Y":
        continue
    elif confirm.capitalize() == "N":
        break













