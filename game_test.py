import unittest
from main import comparison, repeat, score, NPC_Choice


class MyTestCase(unittest.TestCase):
    def test_result(self):
        self.assertEqual("Draw", comparison(1, 1))
        self.assertEqual("Draw", comparison(2, 2))
        self.assertEqual("Draw", comparison(3, 3))
        self.assertEqual("NPC choose Rock, Paper covers Rock\nUser Win!",comparison(2, 1))
        self.assertEqual("NPC choose Rock, Rock smashes Scissor\nUser Lose!", comparison(3, 1))

        self.assertEqual("NPC choose Paper, Paper covers Rock\nUser Lose!", comparison(1, 2))
        self.assertEqual("NPC choose Paper, Scissor cuts Paper\nUser Win!", comparison(3, 2))

        self.assertEqual("NPC choose Scissor, Rock smashes Scissor\nUser Win!", comparison(1, 3))
        self.assertEqual("NPC Choose Scissor, Scissor cuts Paper\nUser Lose!", comparison(2, 3))
    def test_repeat(self):
        self.assertEqual(True, repeat('y'))
        self.assertEqual(False, repeat('n'))
        self.assertEqual(False, repeat('N'))
        self.assertEqual(False, repeat('Y'))
        self.assertEqual(False, repeat('abc'))

    def test_score(self):
        self.assertEqual("User Win!", score(5,0))
        self.assertEqual("User Win!", score(5,1))
        self.assertEqual("User Win!", score(5,2))
        self.assertEqual("User Win!", score(5,3))
        self.assertEqual("User Win!", score(5,4))
        self.assertEqual("NPC Win!", score(0,5))
        self.assertEqual("NPC Win!", score(1,5))
        self.assertEqual("NPC Win!", score(2,5))
        self.assertEqual("NPC Win!", score(3,5))
        self.assertEqual("NPC Win!", score(4,5))

    def test_NPC_choice(self):
        self.assertIn(NPC_Choice(), [1, 2, 3])
        self.assertIn(NPC_Choice(), [1, 2, 3])
        self.assertIn(NPC_Choice(), [1, 2, 3])
        self.assertIn(NPC_Choice(), [1, 2, 3])
        self.assertIn(NPC_Choice(), [1, 2, 3])
        self.assertIn(NPC_Choice(), [1, 2, 3])
        self.assertIn(NPC_Choice(), [1, 2, 3])
        self.assertIn(NPC_Choice(), [1, 2, 3])
        self.assertIn(NPC_Choice(), [1, 2, 3])
        self.assertIn(NPC_Choice(), [1, 2, 3])
        self.assertIn(NPC_Choice(), [1, 2, 3])






if __name__ == '__main__':
    unittest.main()
