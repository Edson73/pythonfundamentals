from aula09 import somar, subtrair
from unittest import TestCase, main

class Testes(TestCase):
    def test_soma(self):
        self.assertEqual(somar(5, 5), 10)
        self.assertLess(somar(5, 5), 11)

    def test_subtracao(self):
        self.assertEqual(subtrair(5, 5), 0)
        self.assertLessEqual(subtrair(15, 5), 10)




if __name__ == "__main__":
    main()