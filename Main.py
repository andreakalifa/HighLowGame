# coding=utf-8

from random import randint

def start_game(RN):
    n = 0
    while n > -1:
        n += 1
        try:
            number = int(input("Scegli un numero tra 1 e 10: "))
        except NameError:
            print("Dovresti scegliere un numero tra 1 e 10")
        except SyntaxError:
            print("Dovresti scegliere un numero tra 1 e 10")

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

while True:

    n = start_game(randint(1, 10))
    punteggi.append(n)
    print("Il miglior punteggio è stato fatto in {} tentativi".format(min(punteggi)))
    confirm = input("Vuoi continuare? y/n ")
    if confirm == "y":
        continue
    elif confirm == "n":
        break













