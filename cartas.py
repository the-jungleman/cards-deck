class Cartas:
    def __init__(self):
        self.cartas_num = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Q", "J", "K"]
        self.naipes = [u'\u2665', u'\u2666', u'\u2663', u'\u2660']
        self.cartas = []
        for carta in self.cartas_num:
            for naipe in self.naipes:
                self.cartas.append(carta + naipe)
