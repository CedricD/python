import unittest

import DM


# @Theo - JE TE LAISSE METTRE LES TESTS LES PLUS PERTINENTS POSSIBLE
class MyTestCase(unittest.TestCase):
    def test_verif_factor(self):
        self.assertFalse(DM.verif_facto([1, 2, 0]))
        self.assertFalse(DM.verif_facto([1, -2]))
        self.assertFalse(DM.verif_facto([3, 2]))
        self.assertTrue(DM.verif_facto([1, 2, 3]))

    def test_base_factorielle_versbase10(self):
        self.assertEqual(DM.base_factorielle_versbase10([1, 1, 1, 1]), 33)

    def test_CreerTabFacto(self):
        self.assertListEqual(DM.CreerTabFacto(1000), [1, 1, 2, 6, 24, 120, 720])

    def test_recherche(self):
        self.assertEqual(DM.recherche(141, [1, 1, 2, 6, 24, 120, 720]), 5)

    def test_recherche2(self):
        self.assertEqual(DM.recherche2(141, [1, 1, 2, 6, 24, 120, 720]), 5)

    def test_base10_vers_basefactorielle(self):
        self.assertListEqual(DM.base10_vers_basefactorielle(1441), [1, 0, 0, 0, 0, 2])

    def test_tab_fibo(self):
        self.assertListEqual(DM.tab_fibo(10), [1, 2, 3, 5, 8, 13, 21, 34, 55, 89])

    def test_decodage_nb(self):
        self.assertEqual(DM.decodage_nb([1, 1, 1, 1, 1, 1]), 32)

    def test_recherche_plus_grand(self):
        self.assertEqual(DM.recherche_plus_grand(200), 12)

    def test_codage_nb(self):
        self.assertListEqual(DM.codage_nb(1000), [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1])

    def test_codage_liste(self):
        self.assertEqual(DM.codage_liste([10, 11, 12]), "010011001011101011")

    def test_decodage_liste(self):
        self.assertListEqual(DM.decodage_liste("010011001011101011"), [10, 11, 12])

    def test_premier00(self):
        self.assertEqual(DM.premier00([0, 1, 1, 0, 0, 1]), 3)

    def test_successeur(self):
        self.assertListEqual(DM.successeur([0, 1, 1, 0, 0, 1]), [0, 0, 0, 1, 0, 1])

    def test_construire(self):
        self.assertListEqual(DM.construire(10),
                             [[0], [1], [0, 1], [0, 0, 1], [1, 0, 1], [0, 0, 0, 1], [1, 0, 0, 1], [0, 1, 0, 1],
                              [0, 0, 0, 0, 1], [1, 0, 0, 0, 1], [0, 1, 0, 0, 1]])


if __name__ == '__main__':
    unittest.main()
