import Card_module, Game

class BJ_card(Card_module.Positionable_Card):
    ACE_VALUE = 1

    @property
    def value(self):
        if self.is_face_up:
            v = BJ_Card.RANKS.index(self.rank) + 1
            if v > 10:
                v = 10
            else:
                v = None
            return v

class BJ_Deck(Card_module.Deck):
    def populate(self):
        for suit in BJ_card.SUIT:
            for rank in BJ_card.RANKS:
                self.cards.append(BJ_card(rank, suit))

class BJ_Hand(Card_module.Hand):
    def __init__(self, name):
        super(BJ_Hand, self).__init__()
        self.name = name

    def __str__(self):
        rep = self.name + ":/t" + super(BJ_Hand, self).__str__()
        if self.total:
            rep += "(" + str(self.total) + ")"
        return rep

    @property
    def total(self):
        for card in self.cards:
            if not card.value:
                return None

        t = 0
        contains_ace = False
        for card in self.cards:
            t += card.value
            if card.value == BJ_card.ACE_VALUE:
                contains_ace = True
        if contains_ace and t <= 11:
            t += 10
        return t

    def is_busted(self):
        return self.total > 21

class BJ_Player(BJ_Hand):
    def is_hitting(self):
        response = Game.ask_yes_no("\n" + self.name + "Будете брать еще карту?")
        return response == "y"

    def bust(self):
        print(self.name, " Вы перебрали.")
        self.lose()

    def lose(self):
        print(self.name, "Вы проиграли.")

    def win(self):
        print(self.name, "Вы выиграли.")

    def push(self):
        print(self.name, "Вы сыграли с диллером в ничью.")

class BJ_Dealer(BJ_Hand):
    def is_hitting(self):
        return self.total < 17

    def bust(self):
        print(self.name, "Перебрал.")

    def flip_first_card(self):
        first_card = self.cards[0]
        first_card.flip()

