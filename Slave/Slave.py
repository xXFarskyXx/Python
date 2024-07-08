#Perfected Function
from math import floor
import random

class player():
    def __init__(self, name , type):
        self.name = name
        self.card_val = []
        self._state = None
        self.type = type #Player or bot

    @property
    def state(self):
        return self._state
    @state.setter
    def state(self , state):
        self._state = state
        game.players_state[self.name] = state
        print("Updated " , self.name , " State: " , self.state)

    def info(self):
        print("Player: " , self.name)
        print("Card: " , self.card_val)
        print("State: " , self.state)
        if self.type:
            print("Type: Bot")
        else:
            print("Type: Player")

    def play(self, cur_card_val , odd_even:bool): #Odd = True , Even = False
        playable = []
        print("---------------- " , self.name , " Turn" , " -------------------")
        if odd_even:
            print("Odd Round!")
        else:
            print("Even Round!")
        print("Current Card: ", order[cur_card_val] , " Value: " , cur_card_val)
        for i in self.card_val:
            if i > cur_card_val:
                playable.append(i)

        #Player
        #1. Check Odd or even this round
        #2. Check Number of Card played - Not same as odd or even, then is invalid
        #3. Check 1 or 3 and 2 or 4 card
        #4. If higher or same, then playable
        #5. Check if the card order is correct
        if not self.type:
            print("-----------------Your Deck---------------")
            for i in playable:
                print("Card: " , order[i] , " Value: " , i)

            #Creating List of card value
            str_play_card = input("Select Your Card(Value): ").split() #Turn input into list of str
            play_card = [int(item) for item in str_play_card]
            max_play_card = max(play_card) #Highest card in playing card

            #Odd
            if odd_even:
                if len(play_card) == 1:
                    print("One Card is Played")
                    if cur_card_val < playable[0]:
                        cur_card_val = playable[0] #Replace Current Card with new Card
                        print("New Current Card: " , cur_card_val)
                        for i in play_card:
                            self.card_val.remove(i)
                        main_deck.append(cur_card_val)
                elif len(play_card) == 3:
                    print("Three Card is Played")
                    card_number = order[(play_card[0])].split()[0] #Default the card
                    #Check if the card is the same number
                    for i in play_card:
                        if order[i].split()[0] != card_number:
                            print("Invalid Combination")
                            return
                    #Overwrite the current value
                    max_play_card += 52 # Make The Value Higher than single card
                    if cur_card_val < max_play_card:
                        cur_card_val = max_play_card #Replace Current Card with Three of a Kind Card
                        print("New Current Card: " , cur_card_val)
                        for i in play_card:
                            self.card_val.remove(i)
                        main_deck.append(cur_card_val)
                elif play_card[0] == 0:
                    print("Pass For This Round")
                elif len(play_card)%2 == 0:
                    print("Can't Play Even Card This Round")
                else:
                    print("Input Error")

            #Even
            else:
                if len(play_card) == 2:
                    print("Two Card is Played")
                    if cur_card_val < max_play_card:
                        cur_card_val = max_play_card
                        print("New Current Card: " , cur_card_val)
                        for i in play_card:
                            self.card_val.remove(i)
                        main_deck.append(cur_card_val)
                elif len(play_card) == 4:
                    print("Four Card is Played")
                    #Check if the card is the same number
                    for i in play_card:
                        if order[i].split()[0] != card_number:
                            print("Invalid Combination")
                            return
                    #Overwrite the current value
                    max_play_card += 52 # Make The Value Higher than single card
                    if cur_card_val < max_play_card:
                        cur_card_val = max_play_card #Replace Current Card with Three of a Kind Card
                        print("New Current Card: " , cur_card_val)
                        for i in play_card:
                            self.card_val.remove(i)
                        main_deck.append(cur_card_val)
                elif play_card[0] == 0:
                    print("Pass For This Round")
                elif len(play_card)%2 == 0:
                    print("Can't Play Odd Card This Round")
                else:
                    print("Input Error")




        #Bot
        else:
            print("Bot is playing card")

            b = len(playable)/2
            y = 10 #highest weight
            c = 1  #lowest weight
            p = (y-c)/b/b
            e = (c/y)**(0.5/b)
            weight = []
            for i in range(len(playable)):
              i += 0.5
              weight.append(  (p*(i-b)*(i-b)+1) #parabola/ratio
                + ((e**i)*10)         #expo*ratio
                )
            randomCard = random.choices(playable, weights=(weight), k=1)
            print("Bot's Deck: ",playable)
            print("Bot Played: ",randomCard)
            main_deck.append(randomCard[0])
            self.card_val.remove(randomCard[0])


chokun = player("Chokun", 0)
bot1 = player("Bot 1", 1)
bot2 = player("Bot 2" , 1)
bot3 = player("Bot 3" , 1)

class game():
    def __init__(): #Not going to create instance, just want to see intializer
        pass

    player_instance = [chokun , bot1 , bot2 , bot3]
    player_name = [player_instance[0].name , player_instance[1].name , player_instance[2].name , player_instance[3].name]
    players_state = {player_name[0]: chokun.state, player_name[1]: bot1.state , player_name[2] : bot2.state , player_name[3] : bot3.state}
    current_card_val = []
    card_number = None #1 card 2 card 3 card or 4 card


    def init_deck():
        global order
        order = {}
        suit = ["Club" , "Diamond" , "Heart" , "Spade"]
        card_order = ["3" , "4" , "5" , "6" , "7" , "8" , "9" , "10" , "Jack" , "Queen" , "King" , "Ace" , "2"]
        print("Initializing Deck...")
        for i in range(1 , 53):
            order.update({i : str(card_order[floor((i-1)/4)] + " " + suit[(i-1)%4])})
        print("Deck Order: " , order)

    #Deck distribution
    def shuffle():
        global main_deck
        chokun.card_val = []
        bot1.card_val = []
        bot2.card_val = []
        bot3.card_val = []
        main_deck = []
        for i in range(1 , 53):
            main_deck.append(i)

        for i in range(13):
            #Player
            temp = random.choice(main_deck)
            main_deck.remove(temp)
            chokun.card_val.append(temp)
            #Bot 1
            temp = random.choice(main_deck)
            main_deck.remove(temp)
            bot1.card_val.append(temp)
            #Bot 2
            temp = random.choice(main_deck)
            main_deck.remove(temp)
            bot2.card_val.append(temp)
            #Bot 3
            temp = random.choice(main_deck)
            main_deck.remove(temp)
            bot3.card_val.append(temp)

        chokun.card_val = quick_sort(chokun.card_val)
        bot1.card_val = quick_sort(bot1.card_val)
        bot2.card_val = quick_sort(bot2.card_val)
        bot3.card_val = quick_sort(bot3.card_val)
        print("Main deck: " , main_deck)
        print("Chokun's Deck: " , chokun.card_val)
        print("Bot1's Deck: " , bot1.card_val)
        print("Bot2's Deck: " , bot2.card_val)
        print("Bot3's Deck: " , bot3.card_val)

    def firstplayer_1stRound(player1,player2,player3,player4):
        cards = [player1.card_val[0], player2.card_val[0], player3.card_val[0], player4.card_val[0]]
        min_card = min(cards)
        if min_card in player1.card_val:
            return player1.name
        if min_card in player2.card_val:
            return player2.name
        if min_card in player3.card_val:
            return player3.name
        if min_card in player4.card_val:
            return player4.name

    def rotate_dir():
        global play_order
        play_order = []
        #First Game
        print("Length of Player State: " , len(game.players_state))
        print("Player State: " , game.players_state)
        print("Player State Value: " , list(game.players_state.values()))
        if list(game.players_state.values()) == [None , None , None , None]: # If 0, Find Lowest Card. Else, find king
            idx = game.player_name.index(game.firstplayer_1stRound(chokun, bot1, bot2, bot3))
            print("Starter: " , game.firstplayer_1stRound(chokun, bot1, bot2, bot3))
            #print("Starting Index: " , idx)
            #Play in CW order
            for i in range(len(game.player_name)):
                print("Index of Play Order: " , idx)
                play_order.append(game.player_instance[idx])
                idx += 1
                if idx == 4:
                    idx = 0

        #Need more work on rotation away from slave
        else:
            print("Player Value: " , list(game.players_state.values()).index("King"))
            king = list(game.players_state.keys())[list(game.players_state.values()).index("King")]
            slave = list(game.players_state.keys())[list(game.players_state.values()).index("Slave")]
            print("King Player:" , king)
            print("Slave Player: " , slave)
            #make slave player become last
            king_idx = idx_cw = idx_ccw = list(game.players_state.values()).index("King")
            slave_idx = list(game.players_state.values()).index("Slave")
            for i in range(len(game.player_instance)):
                idx_cw += 1  #Offset from the first player index
                idx_ccw -= 1
                if idx_cw == 4:
                    idx_cw = 0
                if idx_ccw == -1:
                    idx_ccw = 3
                if idx_ccw == slave_idx: #CW > CCW, so play in CW
                    for j in range(len(game.player_instance)):
                        play_order.append(game.player_instance[king_idx])
                        king_idx += 1
                        if king_idx == 4:
                            king_idx = 0
                    break
                if idx_cw == slave_idx: #CCW > CW, so play in CCW
                    for j in range(len(game.player_instance)):
                        play_order.append(game.player_instance[king_idx])
                        king_idx -= 1
                        if king_idx == -1:
                            king_idx = 3
                    break
        print("Rotate Direction: ")
        for i in range(4):
            print("Player Order " , i , ": " , play_order[i].name)

    # for slave and second slave giving cards to king and queen
    def slave_giving(player):
        if player.state == "Slave":
            for i in range(len(game.player_instance)):
                    if game.player_instance[i].state == "King":
                        receiver = game.player_instance[i]
            give = 2

        elif player.state == "Vice Slave":
            for i in range(len(game.player_instance)):
                    if game.player_instance[i].state == "Queen":
                        receiver = game.player_instance[i]
            give = 1
        for i in range(give):
            removed_card_value = player.card_val[len(player.card_val) - 1]
            player.card_val.remove(removed_card_value)
            receiver.card_val.append(removed_card_value)
        quick_sort(player.card_val)
        quick_sort(receiver.card_val)
        print("------------------- After Slave Card Exchange -------------------")
        print("Chokun's Deck: " , chokun.card_val)
        print("Bot1's Deck: " , bot1.card_val)
        print("Bot2's Deck: " , bot2.card_val)
        print("Bot3's Deck: " , bot3.card_val)

    #For king and queen giving cards to slave and second
    def win_giving(player):
        if player.type == 0 : #person
            if player.state == "King":
                for i in range(len(game.player_instance)):
                    if game.player_instance[i].state == "Slave":
                        receiver = game.player_instance[i]
                give = 2

            elif player.state == "Queen":
                for i in range(len(game.player_instance)):
                    if game.player_instance[i].state == "Vice Slave":
                        receiver = game.player_instance[i]
                give = 1

            for i in range(give):
                cardGiven = input("What card do you want to give?: ")
                key_list = list(order.keys())
                val_list = list(order.values())

                givenKey = key_list[val_list.index(cardGiven)]
                player.card_val.remove(givenKey)
                receiver.card_val.append(givenKey)
        elif player.type == 1: #Bot
            if player.state == "King":
                for i in range(len(game.player_instance)):
                    if game.player_instance[i].state == "Slave":
                        receiver = game.player_instance[i]
                give = 2

            elif player.state == "Queen":
                for i in range(len(game.player_instance)):
                    if game.player_instance[i].state == "Slave":
                        receiver = game.player_instance[i]
                give = 1

            for i in range(give):
                givenKey = player.card_val[0]
                player.card_val.remove(givenKey)
                receiver.card_val.append(givenKey)

        quick_sort(player.card_val)
        quick_sort(receiver.card_val)
        print("------------------- After Winner Card Exchange -------------------")
        print("Chokun's Deck: " , chokun.card_val)
        print("Bot1's Deck: " , bot1.card_val)
        print("Bot2's Deck: " , bot2.card_val)
        print("Bot3's Deck: " , bot3.card_val)


def quick_sort(arr):
    for i in range(len(arr) - 1  , -1 , -1):
        max = i
        for j in range(i):
            if arr[max] <= arr[j]:
                max = j
                #Switch
        temp = arr[max]
        arr[max] = arr[i]
        arr[i] = temp
    return arr

#str --> class
import sys
def get_class(class_name):
    return getattr(sys.modules[__name__], class_name)

#chokun.state = "Slave"
#bot1.state = "Queen"
#bot2.state = "Vice Slave"
#bot3.state = "King"

chokun.info()

#Starting Game without Looping
game.init_deck()

game.shuffle()

game.rotate_dir()
#Just simulate state
odd_even = False

#game.slave_giving(chokun)
#game.win_giving(bot3)


chokun.play(1 , odd_even)

#Game Loop
play_idx = 0
game_end = False
while not game_end:
    pass