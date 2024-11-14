import random

NOMBRE_MIN = 1
NOMBRE_MAX = 10
continuer = True

def poser_question():
    a = random.randint(NOMBRE_MIN, NOMBRE_MAX)
    b = random.randint(NOMBRE_MIN, NOMBRE_MAX)
    reponse_str = input(f"Calculez {a} + {b} : ")
    if int(reponse_str) == a + b:
        print("Réponse correcte !")
    else:
        print(f"Réponse incorrecte ! {a} + {b} = {a + b}")

while continuer:
    poser_question()
    continuer_str = input("Voulez-vous continuer ? (o/n) :")
    if continuer_str == "n":
        continuer = False
