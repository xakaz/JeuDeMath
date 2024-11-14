import random

NOMBRE_MIN = 1
NOMBRE_MAX = 10
NB_QUESTIONS = 5
score = 0

def poser_question():
    global score
    a = random.randint(NOMBRE_MIN, NOMBRE_MAX)
    b = random.randint(NOMBRE_MIN, NOMBRE_MAX)
    reponse_str = input(f"Calculez {a} + {b} : ")
    if int(reponse_str) == a + b:
        print("Réponse correcte !")
        score += 1
    else:
        print(f"Réponse incorrecte ! {a} + {b} = {a + b}")

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

