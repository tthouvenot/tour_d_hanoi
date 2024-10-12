# Contexte : 
#
# Le problème des tours d'Hanoï est un casse-tête mathématique qui consiste à déplacer un ensemble de disques de tailles différentes entre trois tours, en respectant des règles précises. Il existe une solution récursive élégante pour résoudre ce problème, qui peut être implémentée efficacement en Python. 
#
# Problématique : 
# 
# Vous devez implémenter un programme Python qui résout le problème des tours d'Hanoï pour un nombre arbitraire de disques ( n ). 

# Le principe de la tour d'Hanoi:
#
# Il y a 3 tours 
# Sur la tour de départ il y a N disques allant du plus grand en bas au plus petit en haut. 
#
# Tous les 3 tours on répète le même mouvement: 
#   - Soit x le tour , x+N le tour suivant: A vers C
#   - x+1, x+1+N le tour suivant: A vers B
#   - x+2, x+2+N le tour suivant: C vers B 
# 
# L'affichage se fait à travers une liste décroissante avec 
#   - le disque le plus grand (en bas de la tour) à gauche 
#   - le disque le plus petit (en haut de la tour) à droite

# On crée la fonction qui gère l'affichage des tours
def tower_representation(towers):
    
    # Pour chaque tour et chaque disque on affiche l'état acuel des tours
    print()
    print("----------------")
    for tower, disks in towers.items():
        # Affiche les disques présents sur chaque tour
        print(f"Tour {tower}: {disks}")
    print("----------------")
    print()

# On crée la fonction qui permet d'afficher le nombre minimum de mouvements nécessaires
def minimum_moves(n):
    return 2 ** n - 1

# On crée la fonction de la tour d'hanoi
def hanoi(n, source, destination, auxiliaire, towers):

    # Représente toujours le mouvement du disque le plus petit
    if n == 1:
        # On supprime le disque de la source
        disk = towers[source].pop()
        # On ajoute le disque à la tour de destination
        towers[destination].append(disk)
        # On gère l'affichage
        print(f"Déplace le disque 1 de {source} à {destination}")
        tower_representation(towers)

        # Return puisque c'est le plus petit disque
        return
    
    # Représente le tour x+1. Déplace le disque n-1 de la source vers l'auxiliaire avant de déplacer le plus grand
    hanoi(n-1, source, auxiliaire, destination, towers)

    disk = towers[source].pop()
    towers[destination].append(disk)
    print(f"Déplace le disque {n} de {source} à {destination}")
    tower_representation(towers)
    
    # Représente le tour x+2. Déplace les n-1 disques de l'auxiliaire vers la destination
    hanoi(n-1, auxiliaire, destination, source, towers)

# L'utilisateur défini le nombre disque
good_input = False

# On vérifie que l'input est un nombre entier positif supérieur à 1
while not good_input:

    try:
        disk_number = int(input("Combien de disque souhaitez vous mettre dans votre tour d'Hanoï? "))

        if disk_number <= 1:
            print("Erreur: Pour jouer à la tour d'Hanoï vous devez mettre au moins 2 disques.")
        else:
            print(f"Vous avez choisi {disk_number} disques. La tour sera résolu en {minimum_moves(disk_number)} mouvements.")
            good_input = True
    except ValueError:
        print("Erreur: la saisie est incorrect. Elle doit être un nombre entier")

# On crée l'affichage des tours avec le nombre de disque choisi par l'utilisateur dans la tour A
towers = {
    "A": list(range(disk_number, 0, -1)),
    "B": [],
    "C": []
}

# On appelle la fonction hanoi
hanoi(disk_number, "A", "C", "B", towers)