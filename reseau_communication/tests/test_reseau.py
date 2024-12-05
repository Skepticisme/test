import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from src.validateur_sequence import ValidateurSequence
from src.generateur_reseau import GenerateurReseau

class TestValidateurSequence(unittest.TestCase):
    def test_est_graphique_valide(self):
        self.assertTrue(ValidateurSequence.est_graphique([3, 3, 2, 3, 3, 2]))
        self.assertTrue(ValidateurSequence.est_graphique([2, 2, 2, 2]))
        self.assertTrue(ValidateurSequence.est_graphique([4, 3, 3, 2, 2, 2]))

    def test_est_graphique_invalide(self):
        self.assertFalse(ValidateurSequence.est_graphique([5, 3, 2, 2]))
        self.assertFalse(ValidateurSequence.est_graphique([1, 1, 1, 1, 1]))

class TestGenerateurReseau(unittest.TestCase):
    def test_generation_reseaux(self):
        sequence = [3, 3, 2, 3, 3, 2]
        generateur = GenerateurReseau(sequence)
        reseaux = generateur.generer_reseaux()
        self.assertEqual(len(reseaux), 54)  
        self.assertIsInstance(reseaux, list)

    def test_generation_aucun_reseau(self):
        with self.assertRaises(ValueError):
            GenerateurReseau([5, 3, 2, 2])  

    def test_connectivite(self):
        sequence = [2, 2, 2, 2]
        generateur = GenerateurReseau(sequence)
        reseaux = generateur.generer_reseaux()
        for reseau in reseaux:
            visited = [False] * len(reseau)
            stack = [0]
            while stack:
                node = stack.pop()
                if not visited[node]:
                    visited[node] = True
                    stack.extend(reseau[node])
            self.assertTrue(all(visited))  

if __name__ == "__main__":
    unittest.main()
