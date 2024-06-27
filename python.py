from getpass import getpass as input
print("===Bienvenue au tournoi de 🪨📄✂️===")
print()
print("(Veuillez répondre par P, F ou C)")
print()
nom_joueur_1 = input("Que l'un des deux joueurs écrive son prénom.")
nom_joueur_2 = input("Que l'autre joueur écrive son prénom a son tour")
print()
Joueur_1 = str(input("Que le joueur 1 indique ce qu'il veut jouer !"))
Joueur_2 = str(input("Que le joueur 2 indique ce qu'il veut jouer !"))
print()

if Joueur_1 == "P":
  if Joueur_2 == "P":
    print("Les pierres des deux joueurs s'entrent choquent, matche nul !!!")
  elif Joueur_2 == "F":
    print("La feuille de",nom_joueur_2," étouffe la pierre de ",nom_joueur_1,", victoire de",nom_joueur_2,"!!!")
  elif Joueur_2 == "C":
    print("La pierre de",nom_joueur_1," atomise à grands coup les ciseaux de",nom_joueur_2,", victoire de",nom_joueur_1," !!!")
  else :
    print(nom_joueur_2," n'a pas bien écris, veuillez recommencer.")

elif Joueur_1 == "F":
  if Joueur_2 == "F":
    print("Les feuilles des deux joueurs se collent, matche nul !!!")
  elif Joueur_2 == "P":
    print("La feuille de",nom_joueur_1," étouffe la pierre de",nom_joueur_2,", victoire de",nom_joueur_1," !!!")
  elif Joueur_2 == "C":
    print("Les ciseaux de",nom_joueur_2," tranchent en mille morceaux la feuille de",nom_joueur_1,", victoire de",nom_joueur_2,"!!!")
  else :
    print(nom_joueur_2," n'a pas bien écris, veuillez recommencer.")

elif Joueur_1 == "C":
  if Joueur_2 == "C":
    print("Les ciseaux des deux joueurs se bloquent, matche nul !!!")
  elif Joueur_2 == "F":
    print("Les ciseaux de",nom_joueur_1," tranchent en mille morceaux la feuille de",nom_joueur_2,", victoire de",nom_joueur_1," !!!")
  elif Joueur_2 == "P":
    print("La pierre de",nom_joueur_2," atomise à grands coup les ciseaux de",nom_joueur_1,", victoire de",nom_joueur_2," !!!")
  else :
    print(nom_joueur_2," n'a pas bien écris, veuillez recommencer.")
else:
  print(nom_joueur_1," n'a pas bien écris, veuillez recommencer.")
