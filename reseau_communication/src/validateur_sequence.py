class ValidateurSequence:
    """
    Utilitaire de validation pour les séquences de degrés.
    """
    @staticmethod
    def est_graphique(sequence_degres):
        """
        Vérifie si une séquence de degrés est graphique en utilisant le critère de Havel-Hakimi.

        :param sequence_degres: Liste des degrés des sommets
        :return: True si la séquence est graphique, False sinon
        """
        n = len(sequence_degres)
        sequence_triee = sorted(sequence_degres, reverse=True)
        
        for k in range(1, n + 1):
            somme_partielle = sum(sequence_triee[:k])
            somme_max_deg = k * (k - 1) + sum(min(d, k) for d in sequence_triee[k:])
            
            if somme_partielle > somme_max_deg:
                return False
        
        return sum(sequence_degres) % 2 == 0
