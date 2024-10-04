from clg import Vector_shuffle_set
from cartas import Cartas

class Embaralhar:
    def __init__(self):
        self.clg = Vector_shuffle_set()
        self.cartas = Cartas()

    def embaralhar_cartas(self, objCartas, objVector_shuffle_set):
        self.objCartas = objCartas
        self.objVector_shuffle_set = objVector_shuffle_set

        seed = int(input("Digite a semente inicial: "))  # Converter para inteiro
        cartas_len = len(self.objCartas.cartas)

        # Executa o algoritmo de geração de números pseudoaleatórios
        self.cartas_embaralhadas = self.objVector_shuffle_set.run_lcg(cartas_len, seed)
        return f"Cartas embaralhadas de acordo com a semente inicial:\n{self.cartas_embaralhadas}"
