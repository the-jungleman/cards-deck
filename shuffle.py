from clg import Vector_shuffle_set
from cards import Cards

class Shuffle:
    def __init__(self):
        self.clg = Vector_shuffle_set()
        self.cards = Cards()

    def shuffle_cards(self, objcards, objVector_shuffle_set):
        self.objcards = objcards
        self.objVector_shuffle_set = objVector_shuffle_set
        seed = int(input("\nDigite a semente inicial: "))
        cards_len = len(self.objcards.cards)
        random_nuns = self.objVector_shuffle_set.run_lcg(cards_len, seed)
        cards_shuffled = self.objcards.cards[:]
        for i in range(cards_len):
            swap_idx = random_nuns[i] % cards_len 
            cards_shuffled[i], cards_shuffled[swap_idx] = cards_shuffled[swap_idx], cards_shuffled[i]
        return f"Cartas embaralhadas de acordo com a semente inicial:\n{cards_shuffled}"
