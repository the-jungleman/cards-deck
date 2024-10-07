from cards import Cards
from clg import Vector_shuffle_set
from shuffle import Shuffle
import  os

if __name__ == "__main__":
    os.system("clear")
    cards = Cards()
    vector_shuffle = Vector_shuffle_set()
    shuffle = Shuffle()
    print("Cartas não embaralhadas")
    for i   in  cards.get_cards():
        print(f"{i}",end=' ')
    result = shuffle.shuffle_cards(cards, vector_shuffle)
    print(result)