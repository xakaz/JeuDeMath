import random

# Constantes &
NOMBRE_MIN = 1
NOMBRE_MAX = 10
NB_QUESTIONS = 5
score = 0
operateur_str = ""
calcul = 0

# Fonctions
def addition(a, b):
    return a + b

def multiplication(a, b):
    return a * b

def soustraction(a, b):
    return a - b

def choix_opérateur(a,b):
    global operateur_str
    global calcul
    operation = random.choice([addition, multiplication, soustraction])
    operateur_str = "+"
    calcul = addition(a, b)

    if operation == soustraction:
        operateur_str = "-"
        calcul = soustraction(a, b)
    elif operation == multiplication:
        operateur_str = "x"
        calcul = multiplication(a, b)

def poser_question():
    global score
    global calcul
    a = random.randint(NOMBRE_MIN, NOMBRE_MAX)
    b = random.randint(NOMBRE_MIN, NOMBRE_MAX)
    choix_opérateur(a,b)


    reponse_str = input(f"Calculez {a} {operateur_str} {b} : ")
    if int(reponse_str) == calcul:
        print("Réponse correcte !")
        score += 1
    else:
        print(f"Réponse incorrecte ! {a} {operateur_str} {b} = {calcul}")


# Programme principal
for i in range(0,NB_QUESTIONS):
    print(f"Question {i+1}/{NB_QUESTIONS}")
    poser_question()
    print()

if score == NB_QUESTIONS:
    print(f"Bravo, vous avez eu {score}/{NB_QUESTIONS} !")
elif score == 0:
    print(f"Vous avez eu {score}/{NB_QUESTIONS}... Il va falloir réviser.")
elif score < NB_QUESTIONS:
    print(f"Vous avez eu {score}/{NB_QUESTIONS}. Pas mal, mais vous pouvez mieux faire.")

