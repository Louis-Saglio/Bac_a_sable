# Les méthodes de str

test = "Lettre"

# s.capitalize() -> str
# Ne prend pas de paramètre
# Renvoi une copie de l'objet avec une majuscule au début
# Ne modifie pas l'objet. En renvoi une copie modifiée
# Si la première lettre est déjà une majuscule ou n'a pas de majuscule correspondante, elle n'est pas modifiée
test.capitalize()  # -> Lettre
"Maison".capitalize()  # -> Maison
"18h".capitalize()  # -> 18h

print(test.center(15, '.'))

print(test.casefold())

