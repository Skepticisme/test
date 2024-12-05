from src.generateur_reseau import GenerateurReseau
import sys

def main():
    """
    Fonction principale qui permet à l'utilisateur d'entrer une séquence de degrés
    soit manuellement, soit à partir d'un fichier texte. Ensuite, génère les réseaux
    en utilisant la classe GenerateurReseau et affiche les résultats.
    """
    # Demander à l'utilisateur de choisir une méthode d'entrée pour la séquence de degrés
    choix = input("Voulez-vous entrer une séquence de degrés manuellement (m) ou charger à partir d'un fichier (f) ? (m/f): ").strip().lower()

    if choix == "f":
        # Charger une séquence à partir d'un fichier
        fichier_path = input("Entrez le chemin du fichier texte : ").strip()
        try:
            with open(fichier_path, "r") as fichier:
                sequences_test = [
                    list(map(int, ligne.strip()[1:-1].split(", ")))  # Convertir chaque ligne en liste d'entiers
                    for ligne in fichier.readlines()
                ]
        except FileNotFoundError:
            print(f"Erreur : Le fichier '{fichier_path}' n'a pas été trouvé.")
            sys.exit(1)
        except ValueError:
            print("Erreur : Le fichier contient des données mal formatées.")
            sys.exit(1)
    elif choix == "m":
        # Entrer la séquence manuellement
        sequences_test = []
        while True:
            try:
                sequence = input("Entrez une séquence de degrés sous forme de liste (ex: [3, 2, 1]) : ")
                sequence = eval(sequence)  # Utiliser eval() pour convertir la chaîne en liste
                if not all(isinstance(x, int) for x in sequence):
                    raise ValueError("La séquence doit contenir uniquement des entiers.")
                sequences_test.append(sequence)
            except (SyntaxError, ValueError) as e:
                print(f"Erreur dans la séquence : {e}")
            continuer = input("Voulez-vous ajouter une autre séquence ? (o/n) : ").strip().lower()
            if continuer != "o":
                break
    else:
        print("Choix invalide. Veuillez choisir 'm' pour manuel ou 'f' pour fichier.")
        sys.exit(1)

    # Générer et afficher les réseaux pour chaque séquence
    for sequence in sequences_test:
        print(f"\nGénération des réseaux pour la séquence : {sequence}")
        try:
            generateur = GenerateurReseau(sequence)
            reseaux = generateur.generer_reseaux()
            
            print(f"Nombre total de réseaux uniques : {len(reseaux)}")
            for i, reseau in enumerate(reseaux, 1):
                print(f"Réseau {i} : {reseau}")
        except ValueError as e:
            print(f"Erreur : {e}")

if __name__ == "__main__":
    main()
