# from aula09 import somar, subtrair
from unittest import TestCase, main
from aula09 import validar_par

# class Testes(TestCase):
#     def test_soma(self):
#         self.assertEqual(somar(5, 5), 10)
#         self.assertLess(somar(5, 5), 11)

#     def test_subtracao(self):
#         self.assertEqual(subtrair(5, 5), 0)
#         self.assertLessEqual(subtrair(15, 5), 10)




# if __name__ == "__main__":
#     main()




class Teste(TestCase):
    def test_par(self):
        self.assertEqual(validar_par(4), True)
        self.assertEqual(validar_par(1000), True)

    def test_impar(self):
        self.assertEqual(validar_par(5), False)
        self.assertEqual(validar_par(1001), False)

    def test_string(self):
        self.assertEqual(validar_par('102'), True)
        self.assertEqual(validar_par('1059'), False)
        self.assertEqual(validar_par('string'), None)

if __name__ == "__main__":
    main()