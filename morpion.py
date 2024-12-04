# Initialisation du plateau de jeu (une liste de 9 cases vides)
plateau = [" " for _ in range(9)]

# Fonction pour afficher le plateau
def afficher_plateau():
    print(f"""
     {plateau[0]} | {plateau[1]} | {plateau[2]}
    ---|---|---
     {plateau[3]} | {plateau[4]} | {plateau[5]}
    ---|---|---
     {plateau[6]} | {plateau[7]} | {plateau[8]}
    """)

# Fonction pour vérifier si un joueur a gagné
def verifier_victoire(joueur):
    # Liste des combinaisons gagnantes
    combinaisons_gagnantes = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8), # Lignes
        (0, 3, 6), (1, 4, 7), (2, 5, 8), # Colonnes
        (0, 4, 8), (2, 4, 6)             # Diagonales
    ]
    # Vérifie si une combinaison est remplie par le même joueur
    for comb in combinaisons_gagnantes:
        if plateau[comb[0]] == plateau[comb[1]] == plateau[comb[2]] == joueur:
            return True
    return False

# Fonction pour vérifier si le plateau est plein (match nul)
def plateau_plein():
    return " " not in plateau

# Jeu principal
print("Bienvenue au Tic Tac Toe !")
afficher_plateau()

# Définition du joueur actuel ("X" commence)
joueur_actuel = "X"

# Boucle principale du jeu
while True:
    # Demander au joueur de choisir une case
    try:
        case = int(input(f"Joueur {joueur_actuel}, entrez un numéro de case (1-9) : ")) - 1
        if case < 0 or case > 8 or plateau[case] != " ":
            print("Case invalide, essayez à nouveau.")
            continue
    except ValueError:
        print("Entrée invalide, veuillez entrer un chiffre entre 1 et 9.")
        continue

    # Placer le symbole du joueur sur le plateau
    plateau[case] = joueur_actuel
    afficher_plateau()

    # Vérifier si le joueur actuel a gagné
    if verifier_victoire(joueur_actuel):
        print(f"Félicitations, le joueur {joueur_actuel} a gagné !")
        break

    # Vérifier si le plateau est plein
    if plateau_plein():
        print("Match nul ! Le plateau est plein.")
        break

    # Passer au joueur suivant
    joueur_actuel = "O" if joueur_actuel == "X" else "X"
