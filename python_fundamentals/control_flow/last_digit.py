#!/usr/bin/env python3
# Génère un nombre aléatoire entre -10000 et 10000
number = __import__('random').randint(-10000, 10000)

# Calcule le dernier chiffre en préservant le signe négatif si nécessaire
if number < 0:
    last_digit = number % -10
else:
    last_digit = number % 10

# Vérifie les conditions et affiche le message correspondant
if last_digit > 5:
    print(f"Last digit of {number} is {last_digit} and is greater than 5")
elif last_digit == 0:
    print(f"Last digit of {number} is {last_digit} and is 0")
else:
    print(f"Last digit of {number} is {last_digit} and is less than 6 and not 0")
