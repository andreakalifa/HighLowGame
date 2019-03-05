# coding=utf-8

from random import randint

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


while True:

    n = start_game()
    punteggi.append(n)
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













