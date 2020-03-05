import random
class Card:
    def __init__(self, suite, value, name):
        self.suite = suite
        self.value = value
        self.name = name

class Deck:
    def __init__(self):
        self.deck = []
        for i in range(1,14):
            self.cardHelper("Hearts", i)
        for i in range(1,14):
            self.cardHelper("Diamonds", i)
        for i in range(1,14):
            self.cardHelper("Spades", i)
        for i in range(1,14):
            self.cardHelper("Clubs", i)
        self.deck.append(Card("joker",14,"Joker"))
    
    def cardHelper(self, suite, value):
        if (value == 1):
            self.deck.append(Card(suite, value, "Ace"))
        elif(value == 11):
            self.deck.append(Card(suite, value, "Jack"))
        elif(value == 12):
            self.deck.append(Card(suite, value, "Queen"))
        elif(value == 13):
            self.deck.append(Card(suite, value, "King"))
        else:
            self.deck.append(Card(suite, value, str(value)))
    def display_deck(self):
            for i in range(len(self.deck)):
                if self.deck[i].value == 11 or self.deck[i].value == 12 or  self.deck[i].value == 13 :
                    print(f"{self.deck[i].suite} - {self.deck[i].name} ")
                else :
                    print(f"{self.deck[i].suite} - {self.deck[i].name} ")


class Player:
    def __init__(self,name):
        self.hand = []
        self.name = name
    def add_card(self,card):
        self.hand.append(card)
    def rem_card_at(self,index):
        return self.hand.pop(index)
    def isEmpty(self):
        if (len(self.hand) == 0):
            return True
        else:
            return False

    def display_hand(self):
        for i in range(len(self.hand)):
            print(f"{self.hand[i].suite} - {self.hand[i].name} ")
    def remove_duplicates(self):
        for i in range(len(self.hand)):
            for j in range(i+1,len(self.hand)):
                if self.hand[i].value == self.hand[j].value:
                    self.hand[i].value = None
                    self.hand[j].value = None
                    break
        for i in range(len(self.hand)-1, -1,-1):
            if self.hand[i].value == None:
                self.hand.pop(i)
        # cnt =-1
        # for i in range(len(self.hand)-1,cnt):
        #     for j in range( i-1,-1,-1):
        #         if self.hand[i].value == self.hand[j].value :
        #             self.hand.pop(j)
        #             self.hand.pop(i)
        #             cnt = -2
        #             break;
        #         else :
        #             cnt =-1


        return self


class Game:
    def __init__(self):
        self.player_list =[]
        self.playing_deck = Deck()

    def add_player(self,player):
        self.player_list.append(player)

    def start_game(self):

        pass
    def distribute_cards(self):
        #shuffle the deck
        random.shuffle(self.playing_deck.deck)
        #self.playing_deck.display_deck()
        #Till End of Deck add_card to the players from the list
        for i in range(len(self.playing_deck.deck)):
            self.player_list[i%len(self.player_list)].add_card(self.playing_deck.deck[i])

            # if i%3 == 0 :
            #     self.player_list[0].add_card(self.playing_deck.deck[i])
            # elif i%3 == 1:
            #     self.player_list[1].add_card(self.playing_deck.deck[i])
            # else :
            #     self.player_list[2].add_card(self.playing_deck.deck[i])
        # displaying the players hand
        # for i in range(len(self.player_list)):
        #     print (f"{i}" * 50)
        #     self.player_list[i].display_hand()

        # Removing the duplicates
        for i in range(len(self.player_list)):
            self.player_list[i].remove_duplicates()

        # for i in range(len(self.player_list)):
        #     print (f"{i}" * 50)
        #     self.player_list[i].display_hand()



    def start_game(self):
        self.distribute_cards()
        #
        turn = 0 
        isEmptyHand = False
        num_of_players = len(self.player_list)

        while (isEmptyHand == False):
            print(f" {self.player_list[turn%num_of_players].name} -- It is your turn to pick a card from next player {self.player_list[(turn+1)%num_of_players].name}")
            #print(f"Player{turn%num_of_players} -- It is your turn to pick a card from next player Player{(turn+1)%num_of_players}")
            print(f"\n{self.player_list[turn%num_of_players].name}'s hand")
            self.player_list[(turn)%num_of_players].display_hand()
            print(f"\nChoose the card from 1 to {len(self.player_list[(turn+1)%num_of_players].hand)}") 
            print(f"\n{self.player_list[(turn+1)%num_of_players].name}'s hand")       
            self.player_list[(turn+1)%num_of_players].display_hand()
            while (True):
                card_no = input("\nEnter the Card Number")
                try:
                    if (int(card_no) <= 0 or int(card_no) > len(self.player_list[(turn+1)%num_of_players].hand)):
                    #if((int(card_no)) != 1 or int(card_no) != 2 or int(card_no) != 3 or int(card_no)!= 4 or int(card_no)!= 5 or int(card_no)!= 6 or int(card_no)!=7 or int(card_no)!= 8 or int(card_no)!= 9 ):
                        print("Wrong card number")
                    else:
                        break
                except:
                    print("Display Valid Integer")

            new_card = self.player_list[(turn+1)%num_of_players].rem_card_at(int(card_no)-1)
            self.player_list[(turn)%num_of_players].add_card(new_card)
            random.shuffle(self.player_list[(turn)%num_of_players].hand)
            # displaying current player cards
            print(f"\n{self.player_list[turn%num_of_players].name}")
            self.player_list[(turn)%num_of_players].display_hand()
            print(f"\n{self.player_list[(turn+1)%num_of_players].name}")
            # displaying current player cards
            self.player_list[(turn+1)%num_of_players].display_hand()

            print("\nRemoving the duplicates from the current player")
            self.player_list[(turn)%num_of_players].remove_duplicates()
            print(f"\n{self.player_list[turn%num_of_players].name} hand after removing duplicates")
            self.player_list[(turn)%num_of_players].display_hand()

            turn+= 1
            # 

            for i in range(num_of_players):
                if (self.player_list[i].isEmpty()):
                    print(f"Contrats {self.player_list[i].name} you won!")
                    self.player_list.pop(i)
                    num_of_players -= 1
                    break;

            if len(self.player_list) == 1:
                print (f"{self.player_list[0].name} -- Sorry you lost") 
                break



game = Game()
print("*"*80)
print("Welcome to Catch  Thief")
print("*"*80)
print("\n")
while True:
    try:
        player_cnt = int(input("Input Number of Players between 2 and 5\n"))
        if (player_cnt > 5 or player_cnt < 2):
            print("Please Enter valid number\n")
        else :
            break
    except:
        print("Please Enter valid number\n")


for i in range(player_cnt) :
    name = input(f"Player {i} name\n")
    game.add_player(Player(name))


# p1 = Player("Mike")
# p2 = Player("Vishnu")
# p3 =Player("George")
# p4 = Player("Cody")
# game.add_player(p1)
# game.add_player(p2)
# game.add_player(p3)
# game.add_player(p4)
game.start_game()






