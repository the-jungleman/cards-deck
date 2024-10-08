from clg import Vector_shuffle_set
from cards import Cards

class Shuffle:
    def __init__(self):
        self.clg = Vector_shuffle_set() 

    def shuffle_cards(self, objcards):
        seed = int(input("\nDigite a semente inicial: "))
        cards_len = len(objcards.cards)
        random_nuns = self.clg.run_lcg(cards_len, seed)
        cards_shuffled = objcards.cards[:]
        for i in range(cards_len):
            swap_idx = random_nuns[i] % cards_len
            cards_shuffled[i], cards_shuffled[swap_idx] = cards_shuffled[swap_idx], cards_shuffled[i]
        return cards_shuffled
