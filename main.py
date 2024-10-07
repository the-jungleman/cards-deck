from cards import Cards
from clg import Vector_shuffle_set
from shuffle import Shuffle
import os

if __name__ == "__main__":
    os.system("clear")
    cards = Cards()
    print("Cartas nao embaralhadas:\n"+" ".join(cards.get_cards()))
    vector_shuffle = Vector_shuffle_set()
    shuffle = Shuffle()
    result = shuffle.shuffle_cards(cards, vector_shuffle)
    print("\nCartas embaralhadas:\n"+" ".join(result))
