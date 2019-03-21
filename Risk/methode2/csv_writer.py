def recup_nombre(chaine):
    rep = ""
    save = False
    for lettre in chaine:
        if lettre.isdigit():
            rep += lettre
            save = True
        elif save:
            rep += ";"
            save = False
    return rep


fichier = "log"
rep = ""
with open(fichier) as file:
    for ligne in file:
        rep += recup_nombre(ligne) + "\n"
with open("lelog.csv", "w") as frfr:
    print(rep, file=frfr)
