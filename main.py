from cards import Cards
from clg import Vector_shuffle_set
from shuffle import Shuffle
<<<<<<< HEAD
import os
=======
<<<<<<< HEAD
import os
=======
import  os
>>>>>>> 6992a3a (finished)
>>>>>>> origin/main

if __name__ == "__main__":
    os.system("clear")
    cards = Cards()
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> origin/main
    print("Cartas não embaralhadas:")
    print(" ".join(cards.get_cards()))
    vector_shuffle = Vector_shuffle_set()
    shuffle = Shuffle()
    result = shuffle.shuffle_cards(cards, vector_shuffle)
    print("\nCartas embaralhadas:")
    print(" ".join(result))

<<<<<<< HEAD
=======
=======
    vector_shuffle = Vector_shuffle_set()
    shuffle = Shuffle()
    print("Cartas não embaralhadas")
    for i   in  cards.get_cards():
        print(f"{i}",end=' ')
    result = shuffle.shuffle_cards(cards, vector_shuffle)
    print(result)
>>>>>>> 6992a3a (finished)
>>>>>>> origin/main
