from cards import Cards
from shuffle import Shuffle
import os

if __name__ == "__main__":
    os.system("clear")
    cards = Cards()
    shuffle = Shuffle()
    print("Cartas não embaralhadas:\n" + " ".join(cards.get_cards()))
    shuffled_cards = shuffle.shuffle_cards(cards)
    print("\nCartas embaralhadas:\n" + " ".join(shuffled_cards))
    num_to_draw = int(input("\nQuantas cartas você quer tirar do topo?\n>>"))
    drawn_cards = shuffled_cards[:num_to_draw]
    print("\nCartas retiradas do topo:\n" + " ".join(drawn_cards))
