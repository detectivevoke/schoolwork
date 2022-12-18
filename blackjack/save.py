import random
import itertools
class BlackJack():
    def __init__(self, players):
        self.current_player = 0
        self.num_players = players
        self.players_stuck = []
        self.values = {
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "10": 10,
        "J": 10,
        "Q": 10,
        "K": 10,
        "A": 11,}
        self.game = {"players": {}}
        self.deck = []
        self.cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        self.suits = ["S", "H", "D", "C"]
        self.players = []

        #creates the deck fully
        for x in self.cards:
            for y in self.suits:
                self.deck.append(y + x)
        for player in range(players):
            self.players.append(player)
        self.cycle=itertools.cycle(self.players)

        

#pre-game, gives cards to players
    def give_cards(self, players, cards):
    #cycles through number of players
        for player in range(players):
            self.game["players"][str(player)] = {"cards": []}

            for card in range(cards):
                #get random card
                card = self.random_card()
                self.game["players"][str(player)]["cards"].append(card)
                #removes the card itself from deck

    def random_card(self):
        x = random.choice(self.cards)
        y = random.choice(self.suits)
        try:
            self.deck.remove(str(y)+str(x))
        except:
            pass
        return str(y)+str(x)

    def get_card_val(self,player):
        card_value = 0
        for card in self.game["players"][str(player)]["cards"]:
            val = card[len(card)//2:]
            num_val = self.values.get(val)
            card_value += num_val
        return card_value


    def hit(self, player):
        player_deck = self.game["players"][str(player)]["cards"]
        card = self.random_card()
        player_deck.append(card)
        self.game["players"][str(player)]["cards"] = player_deck

    def stand(self,player):
        self.players.remove(player)
        self.cycle=itertools.cycle(self.players)
        return True


    def player_update(self):
        if self.current_player+1>=self.num_players:
                self.current_player = self.current_player - self.num_players
                self.current_player +=1
        else:
            self.current_player +=1
        return True

    def pr(self, arg):
        print("(Player {}) - {}".format(self.current_player, arg))
        
    def check_win(self):
        dv = self.get_card_val(str(self.current_player))
        self.pr("Deck Value: {}".format(dv))

        if int(dv) > 21:
            if "A" in self.game["players"][str(self.current_player)]["cards"]:
                return False
            else:
                self.pr("You have gone above 21! You are out!")
                if self.current_player in self.players:
                    self.players.remove(self.current_player)

                if self.current_player in self.players_stuck:
                    self.players_stuck.remove(self.current_player)

            return False
        elif int(dv) == 21:
            self.pr("You have won!")
            return True

    def start(self):
        self.give_cards(int(self.num_players),2)
        host_card = self.random_card()
        print("Hosts Card: {}".format(host_card))
        while True:
            if not self.players:
                host_val = 0
                host_card_2 = self.random_card()
                num_val = self.values.get(host_card[len(host_card)//2:])
                host_val += num_val
                num_val = self.values.get(host_card_2[len(host_card_2)//2:])
                host_val += num_val
                print("The hosts cards: {}, {}".format(host_card,host_card_2))
                if host_val>21:
                    print("Host is bust! Every player still in wins!")
                elif host_val == 21:
                    print("The host wins!")
                elif host_val <= 17:
                    host_val += self.values.get(host_card_2[len(host_card_2)//2:])
                else:
                    for player in range(self.num_players):
                        if self.get_card_val(player) > host_val:
                            print("Player {} wins!".format(player))
                        elif self.get_card_val(player) == host_val:
                            print("There is a draw with the host and {}.".format(player))
                        else:
                            print("Host wins!")
                break
            if self.current_player in self.players:
                
                if self.current_player in self.players_stuck:
                    print(str(self.current_player) + " is stuck!")
                    self.player_update()
                    print(self.players)

                if len(self.players_stuck) == self.num_players:
                    print("EVERYONE IS STUCK, DRAWING CARDS")

                if self.check_win():
                        break
                x = input("(Player {}) - Hit or Stick (H/S)? ".format(self.current_player))

                if x.upper() == "H":
                    self.hit(self.current_player)
                    if self.check_win():
                        break
                    else:
                        pass

                elif x.upper() == "S":
                    print("You have sticked!")
                    self.players_stuck.append(self.current_player)
                    self.players.remove(self.current_player)
                    if self.check_win():
                        break
                    pass
                else:
                    print("You didn't produce a valid response. You sticked.")
                    self.players_stuck.append(self.current_player)
                    self.players.remove(self.current_player)
                    if self.check_win():
                        break
                    pass
                self.player_update()
     
num_of_players = 1
BlackJack(num_of_players).start()