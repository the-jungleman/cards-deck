class Cards:
    def __init__(self):
        self.cards_set = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Q", "J", "K"]
        self.suits = [u'\u2665', u'\u2666', u'\u2663', u'\u2660']
        self.cards = []
        for card in self.cards_set:
            for suit in self.suits:
                self.cards.append(card + suit)
        self.shuffled_cards = []  
        
    def get_cards(self):
        return self.cards

    def shuffle_cards(self, shuffle):
        self.shuffled_cards = shuffle.shuffle_cards(self, self.cards)
        return self.shuffled_cards

    def draw_cards(self, num_cards):
        if not self.shuffled_cards:
            print("As cartas ainda não foram embaralhadas!")
            return []
        drawn_cards = self.shuffled_cards[:num_cards]
        self.shuffled_cards = self.shuffled_cards[num_cards:]
        return drawn_cards
