import Card_module, Game

class BJ_card(Card_module.Positionable_Card):
    ACE_VALUE = 1

    @property
    def value(self):
        if self.is_face_up:
            v = BJ_card.RANKS.index(self.rank) + 1
            if v > 10:
                v = 10
            else:
                v = None
            return v

class BJ_Deck(Card_module.Deck):
    def populate(self):
        for suit in BJ_card.SUITS:
            for rank in BJ_card.RANKS:
                self.cards.append(BJ_card(rank, suit))

class BJ_Hand(Card_module.Hand):
    def __init__(self, name):
        super(BJ_Hand, self).__init__()
        self.name = name

    def __str__(self):
        rep = self.name + ":\t" + super(BJ_Hand, self).__str__()
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

class BJ_Game:
    def __init__(self, names):
        self.players = []
        for name in names:
            player = BJ_Player(name)
            self.players.append(player)
        self.dealer = BJ_Dealer("Дилер")
        self.Deck = BJ_Deck()
        self.Deck.populate()
        self.Deck.shuffle()
    @property
    def still_playing(self):
        sp = []
        for player in players:
            if not player.is_busted():
                sp.append(player)
        return sp
    def __additional_cards(self, player):
        while not player.is_busted() and player.is_hitting():
            self.Deck.deal([player])
            print(player)
            if player.is_busted():
                player.bust()
    def play(self):
        self.Deck.deal(self.players + [self.dealer], per_hand = 2)
        self.dealer.flip_first_card()
        for player in self.players:
            print(player)
        print(self.dealer)

        for player in self.players:
            self.__additional_cards(player)
        self.dealer.flip_first_card()

        if not self.still_playing:
            print(self.dealer)
        else:
            print(self.dealer)
            self.__additional_cards(self.dealer)

            if self.dealer.is_busted():
                for player in self.still_playing:
                    player.win()
            else:
                for player in self.still_playing:
                    if player.total > self.dealer.total:
                        player.win()
                    elif player.total < self.dealer.total:
                        plaer.lose()
                    else:
                        player.push()

        if player in self.players:
            player.clear()
        self.dealer.clear()

def main():
    print("\t\t Добро пожаловать в Блек-Джек!\n")
    names = []
    number = Game.ask_number("Сколько всего игроков? (1-7): ", low = 1, high = 7)
    for i in range(number):
        name = input("Введите имя игрока № " + str(i + 1) + " :")
        names.append(name)
    print()

    game = BJ_Game(names)
    again = None
    while again != "n":
        game.play()
        again= games.ask_yes_no("\n Хотите сыграть еще раз?")

main()


