from clg import Vector_shuffle_set
from cartas import Cartas

class Embaralhar:
    def __init__(self):
        self.clg    =   Vector_shuffle_set()
        self.cartas =   Cartas()

    def embaralhar_cartas(self,objCartas,objVector_shuffle_set):
        self.objCartas  =   objCartas
        self.objVector_shuffle_set  =   objVector_shuffle_set
        seed    =   int(input("Digite a semente inicial: "))
        random_nuns =   self.objVector_shuffle_set.run_lcg(len(self.objCartas.cartas),seed)
        shuffled_cards  =   self.objCartas.cartas[:]
        for i   in  range(len(self.objCartas.cartas)):
            swap_idx=random_nuns[i]%len(self.objCartas.cartas)
            shuffled_cards[i],shuffled_cards[swap_idx]=shuffled_cards[swap_idx],shuffled_cards[i]
        return f"Cartas embaralhadas de acordo com a semente inicial:\n{shuffled_cards}"
