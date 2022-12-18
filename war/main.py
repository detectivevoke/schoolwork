import random
import string
import json


class War():
    def __init__(self,):
        self.player_deck = []
        self.comp_deck = []
        self.deck = []

        self.values = {"2": 2,"3": 3,"4": 4,"5": 5,"6": 6,"7": 7,"8": 8,"9": 9,"10": 10,"J": 10,"Q": 10,"K": 10,"A": 11}
        self.cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        self.suits = ["S", "H", "D", "C"]

        for x in self.cards:
            for y in self.suits:
                self.deck.append(y + x)

    def random_card(self):
        card = random.choice(self.deck)
        try:
            self.deck.remove(card)
        except Exception as e:
            print(e)
            pass

        return card

    def give_cards(self):
        half = len(self.deck) // 2
        for i in range(half):
            self.comp_deck.append(self.random_card())
        for i in range(half):
            self.player_deck.append(self.random_card())
    
    def main(self):
        
        self.give_cards()
        x = True
        while x:
            r = input()
            pc = random.choice(self.player_deck)
            cc = random.choice(self.comp_deck)
            print("Player ", pc[1:])
            print("Computer ", cc[1:])
            pc_val = self.values.get(pc[1:])
            cc_val = self.values.get(cc[1:])
            if pc_val == cc_val:
                print("Cards are equal")
                new_pc = random.choice(self.player_deck)
                new_cc = random.choice(self.comp_deck)
                print("Player ", pc[1:])
                print("Computer ", cc[1:])
                pc_val = self.values.get(new_pc[1:])
                cc_val = self.values.get(new_cc[1:])

                if pc_val > cc_val:
                    print("Player wins")
                    self.comp_deck.remove(cc)
                    self.comp_deck.remove(new_cc)
                    self.player_deck.append(cc)
                    self.player_deck.append(new_cc)

                if pc_val < cc_val:
                    print("Computer wins")
                    self.comp_deck.append(pc)
                    self.comp_deck.append(new_pc)
                    self.player_deck.remove(pc)
                    self.player_deck.remove(new_pc)


            if pc_val > cc_val:
                print("Player wins")
                self.comp_deck.remove(cc)
                self.player_deck.append(cc)

            if pc_val < cc_val:
                print("Computer wins")
                self.comp_deck.append(pc)
                self.player_deck.remove(pc)

War().main()
