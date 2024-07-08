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

    def play(self, cur_card_val): #Odd = True , Even = False
        global odd_even #Odd = "Odd" , Even = "Even" , Not Set = "None"
        playable = []
        print("---------------- " , self.name , " Turn" , " -------------------")
        if odd_even == "Odd" or odd_even == "Even":
            print(odd_even , " Round!")
            if cur_card_val == 0:
                print("First Card of this Round")
            else:
                if cur_card_val > 52:
                    print("Current Card: ", order[cur_card_val - 52] , " Value: " , cur_card_val)
                else:
                    print("Current Card: ", order[cur_card_val] , " Value: " , cur_card_val)
        elif odd_even == "None":
            print("First Card of the Round! (Set Odd or Even)")

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
            #Let Player Play the whole Deck
            print("-----------------Your Deck---------------")
            print("All Cards: " , self.card_val)
            print("Playable:")
            for i in self.card_val:
                print("Card: " , order[i] , " Value: " , i)

            #Creating List of card value
            str_play_card = input("Select Your Card(Value): ").split() #Turn input into list of str
            play_card = [int(item) for item in str_play_card]
            max_play_card = max(play_card) #Highest card in playing card

            for i in play_card:
                if i not in self.card_val and play_card[0] != 0:
                    print("Card not in Your Deck!")
                    self.play(cur_card_val)
                    return

            #Odd
            if odd_even == "Odd":
                if play_card[0] == 0:
                    play_order_round.remove(self)
                    print("Skip For This Round")
                elif len(play_card) == 1:
                    print("One Card is Played")
                    if cur_card_val < play_card[0]:
                        cur_card_val = play_card[0] #Replace Current Card with new Card
                        print("New Current Card: " , cur_card_val)
                        for i in play_card:
                            self.card_val.remove(i)
                        main_deck.append(cur_card_val)
                    elif cur_card_val > max_play_card:
                        print("Can't Play Lower Cards")
                        self.play(cur_card_val)
                elif len(play_card) == 3:
                    print("Three Card is Played")
                    card_number = order[(play_card[0])].split()[0] #Default the card
                    #Check if the card is the same number
                    for i in range(0 , len(play_card) - 1):
                        if order[play_card[i]].split()[0] != card_number:
                            print("Invalid Combination")
                            self.play(cur_card_val)
                            return
                        #Fix playable same card
                        if play_card[i - 1] == play_card[i] and i != 0:
                            print("Can't Play Same Card")
                            self.play(cur_card_val)
                            return
                    #Overwrite the current value
                    max_play_card += 52 # Make The Value Higher than single card
                    if cur_card_val < max_play_card:
                        cur_card_val = max_play_card #Replace Current Card with Three of a Kind Card
                        print("New Current Card: " , cur_card_val)
                        for i in play_card:
                            self.card_val.remove(i)
                        main_deck.append(max_play_card)
                    elif cur_card_val > max_play_card:
                        print("Can't Play Lower Cards")
                        self.play(cur_card_val)
                elif len(play_card)%2 == 0:
                    print("Can't Play Even Card This Round")
                    self.play(cur_card_val)
                    return
                else:
                    print("Input Error")
                    self.play(cur_card_val)
                    return

            #Even
            elif odd_even == "Even":
                if len(play_card) == 2:
                    print("Two Card is Played")
                    card_number = order[(play_card[0])].split()[0] #Default the card
                    #Check if the card is the same number
                    for i in range(0 , len(play_card) - 1):
                        if order[play_card[i]].split()[0] != card_number:
                            print("Invalid Combination")
                            self.play(cur_card_val)
                            return
                        if play_card[i - 1] == play_card[i] and i != 0:
                            print("Can't Play Same Card")
                            self.play(cur_card_val)
                            return
                    if cur_card_val < max_play_card:
                        cur_card_val = max_play_card
                        print("New Current Card: " , cur_card_val)
                        for i in play_card :
                            self.card_val.remove(i)
                        main_deck.append(cur_card_val)
                    elif cur_card_val > max_play_card:
                        print("Can't Play Lower Cards")
                        self.play(cur_card_val)
                elif len(play_card) == 4:
                    print("Four Card is Played")
                    card_number = order[(play_card[0])].split()[0] #Default the card
                    #Check if the card is the same number
                    for i in range(0 , len(play_card)):
                        if order[play_card[i]].split()[0] != card_number:
                            print("Invalid Combination")
                            self.play(cur_card_val)
                            return
                        if play_card[i - 1] == play_card[i] and i != 0:
                            print("Can't Play Same Card")
                            self.play(cur_card_val)
                            return

                    #Overwrite the current value
                    max_play_card += 52 # Make The Value Higher than single card
                    if cur_card_val < max_play_card:
                        cur_card_val = max_play_card #Replace Current Card with Three of a Kind Card
                        print("New Current Card: " , cur_card_val)
                        for i in play_card:
                            self.card_val.remove(i)
                        main_deck.append(cur_card_val)
                    elif cur_card_val > max_play_card:
                        print("Can't Play Lower Cards")
                        self.play(cur_card_val)
                elif play_card[0] == 0:
                    play_order_round.remove(self)
                    print("Skip For This Round")
                elif len(play_card)%2 == 1:
                    print("Can't Play Odd Card This Round")
                    self.play(cur_card_val)
                else:
                    print("Input Error")
                    self.play(cur_card_val)
            elif odd_even == "None" and self.card_val[0]:
                print("Playing First Card of the Round!")
                #1. Check if card is the same number
                #2. Check if odd or even
                #3. Set round to be odd or even and set new card
                if self.card_val[0] == 1:
                    if 1 not in play_card:
                        print("Must play 3 of Club")
                        self.play(cur_card_val)
                        return
                elif play_card[0] == 0:
                    print("First Player Must Play Some Card")
                    self.play(cur_card_val)
                    return
                card_number = order[(play_card[0])].split()[0] #Default the card
                for i in range(0 , len(play_card)):
                    if order[play_card[i]].split()[0] != card_number:
                        print("Invalid Combination")
                        self.play(cur_card_val)
                        return
                    if play_card[i - 1] == play_card[i] and i != 0:
                        print("Can't Play Same Card")
                        self.play(cur_card_val)
                        return
                if len(play_card)%2 == 1:
                    odd_even = "Odd"
                else:
                    odd_even = "Even"
                print("First Player Set Game to " , odd_even)
                for i in play_card:
                    self.card_val.remove(i)
                main_deck.append(max_play_card)
                print("New Current Card: " , max_play_card)




        #Bot
        else:
            print("Bot is playing card")
            print("Bot's All Cards: " , self.card_val)
            playable.append(999)
            if odd_even == "None":
                playable.remove(999)
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
            #Odd
            if odd_even == "Odd":
                randomCard = random.choices(playable, weights=(weight), k=1)
                print("Bot's Playable Card: ", playable)
                print("Bot Played: " , randomCard)

                if randomCard[0] != 999:
                    main_deck.append(randomCard[0])
                    self.card_val.remove(randomCard[0])
                else:
                    play_order_round.remove(self)
                    print("Bot Skipped")
                    return
            #Even
            elif odd_even == "Even":
                randomCard = random.choices(playable, weights=(weight), k=1)
                print("Bot's Playable Card: ", playable)
                print("Bot Check if bot skipped or not: " , randomCard)

                if randomCard[0] == 999:
                    play_order_round.remove(self)
                    print("Bot Skipped Turn")
                    return
                playable.remove(999)
                for i in range(20):
                    randomCard = random.choices(playable, weights=None, k=2)
                    #print("Bot's Deck: ",playable)
                    #print("Bot Played: ",randomCard)
                    if order[randomCard[0]].split()[0] == order[randomCard[1]].split()[0] and randomCard[0] != randomCard[1]:
                        main_deck.append(max(randomCard))
                        self.card_val.remove(randomCard[1])
                        self.card_val.remove(randomCard[0])
                        print("Bot Played: " , randomCard)
                        return
                print("Bot Skipped Turn(No Playable Card)")
                play_order_round.remove(self)

            elif odd_even == "None":
                #Can't Skip First Round
                if self.card_val[0] == 1:
                    for i in range(20):
                        randomCard = random.choices(playable, weights=(weight), k=2)
                    #print("Bot's Deck: ",playable)
                    #print("Bot Played: ",randomCard)
                    #floor(randomCard[0] /4) == floor(randomCard[1]/4)
                        if  order[randomCard[0]].split()[0] == order[randomCard[1]].split()[0] and randomCard[0] != randomCard[1] and 1 in randomCard:
                            main_deck.append(max(randomCard))
                            self.card_val.remove(randomCard[1])
                            self.card_val.remove(randomCard[0])
                            print("Bot Played: " , randomCard)
                            print("Bot Played Even Card")
                            odd_even = "Even"
                            return
                    main_deck.append(self.card_val[0]) #Playing 3 of Club
                    self.card_val.remove(self.card_val[0])
                    print("Bot Played: " , randomCard)
                    print("Bot Played Odd Cards")
                    odd_even = "Odd"
                    return
                for i in range(20):
                        randomCard = random.choices(playable, weights=(weight), k=2)
                    #print("Bot's Deck: ",playable)
                    #print("Bot Played: ",randomCard)
                    #floor(randomCard[0] /4) == floor(randomCard[1]/4)
                        if  order[randomCard[0]].split()[0] == order[randomCard[1]].split()[0] and randomCard[0] != randomCard[1]:
                            main_deck.append(max(randomCard))
                            self.card_val.remove(randomCard[1])
                            self.card_val.remove(randomCard[0])
                            print("Bot Played: " , randomCard)
                            print("Bot Played Even Card")
                            odd_even = "Even"
                            return
                randomCard = random.choices(playable, weights=(weight), k=1)
                main_deck.append(randomCard[0])
                self.card_val.remove(randomCard[0])
                print("Bot Played: " , randomCard)
                print("Bot Played Odd Cards")
                odd_even = "Odd"


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

# Define a function to print a card
def print_card(card_name):
    card_dict = {
        "King of Spades": [
            "┌───────┐",
            "│ ♠   ♠ │",
            "│   K   │",
            "│ ♠   ♠ │",
            "└───────┘"
        ],
        "Queen of Hearts": [
            "┌───────┐",
            "│ ♥   ♥ │",
            "│   Q   │",
            "│ ♥   ♥ │",
            "└───────┘"
        ],
        "Jack of Hearts": [
            "┌───────┐",
            "│ ♥   ♥ │",
            "│   J   │",
            "│ ♥   ♥ │",
            "└───────┘"
        ],
        "10 of Clubs": [
            "┌───────┐",
            "│ ♣   ♣ │",
            "│   10  │",
            "│ ♣   ♣ │",
            "└───────┘"
        ]
    }

    if card_name in card_dict:
        card = card_dict[card_name]
        print(card_name)
        for line in card:
            print(line)
    else:
        print("Card not found.")


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

#game.slave_giving(chokun)
#game.win_giving(bot3)

import copy
#Game Loop
play_idx = 0
game_end = False
play_order_round = play_order.copy()
#Let bot play
#play_order = [bot1 , bot2 , bot3]
#play_order_round = play_order.copy()
ranking = 0
odd_even = "None"
dir = True
last_player = None # Last Player in the round
last_second_player = None #Second Last player in the match
reset = False
king_slave_switch = False
while not game_end:

    #If 2 player got state in the same rounda
    if last_player == None and len(play_order) != 4 and len(play_order_round) == 0:
        main_deck = []
        play_order_round = play_order.copy()
        if dir:
            play_idx = 0
        elif not dir:
            play_idx = len(play_order_round) - 1
        print("Round Ended")
        print("---------------- Starting New Round In Reverse Order --------------")
        odd_even = "None"
        print("Setting odd_even to " , odd_even)
        last_player = None
        last_second_player = None
        dir = not dir

    #If all player skip, then reset main_deck + reverse play_order_round direction
    elif play_order_round[play_idx] == last_player and len(play_order) != 4:
        main_deck = []
        play_order_round = play_order.copy()
        play_idx = play_order.index(last_player)
        print("Round Ended")
        print("---------------- Starting New Round In Reverse Order --------------")
        odd_even = "None"
        print("Setting odd_even to " , odd_even)
        last_player = None
        last_second_player = None
        dir = not dir

    print("------------------------------------------")
    last_turn_len = len(play_order_round) #Player Length
    last_main_deck = len(main_deck)
    if last_player != None:
        last_second_player = last_player
        print("Last Second Player: " , last_second_player.name)
    #Playing Card
    print("Play Index: " , play_idx)
    print("Length of Last Main Deck: ", last_main_deck)

    if len(main_deck) == 0:
        play_order_round[play_idx].play(0)
    elif len(main_deck) != 0:
        play_order_round[play_idx].play(main_deck[len(main_deck) - 1])
    print("Length of current Main Deck: " , len(main_deck))

    #Game Ender and  Status Assigner(Perfected)
    for i in play_order:
        if len(i.card_val) == 0:
            print("Player: ", i.name)
            match ranking:
                case 0:
                    if i.state == "Slave":
                        king_slave_switch = True
                        #If slave become king -> king will beconme slave instead
                        for j in game.player_instance:
                            if j.state == "King":
                                j.state = "Slave"
                                play_order.remove(j)
                                slave = j
                        print("King become Slave and Slave Become King!")
                    i.state = "King"
                    king = i
                    print_card("King of Spades")
                    print("\n")
                case 1:
                    i.state = "Queen"
                    print_card("Queen of Hearts")
                    print("\n")
                    queen = i
                case 2:
                    i.state = "Vice Slave"
                    print_card("Jack of Hearts")
                    print("\n")
                    vice_slave = i
                #Last Guy Don't need to have rank

            #Set Index of the last player



            print("Removed Player: " , i.name)
            play_order.remove(i)
            play_order_round.remove(i)
            print("Player Left: ")
            for i in play_order:
                print(play_order.index(i), ". " , i.name)

            ranking += 1
        if len(play_order) == 1:
            if not king_slave_switch:
                play_order[0].state = "Slave"
                slave = play_order[0]
            elif king_slave_switch:
                play_order[0].state = "Vice Slave"
                vice_slave = play_order[0]
            print("The game has ended with the rankings:")
            print("1. King: " , king.name)
            print("2. Queen: " , queen.name)
            print("3. Vice Slave: " , vice_slave.name)
            print("4. Slave: " , slave.name)

            # Call the function to print the cards
            print_card("King of Spades")
            print("\n")
            print_card("Queen of Hearts")
            print("\n")
            print_card("Jack of Hearts")
            print("\n")
            print_card("10 of Clubs")
            print("\n")
            respond = input("The Game has ended. Would you like to play again?[Y/N]")
            if respond == "Y":
                print("Restarting the game with the State of Player in Consideration")
                game.shuffle()
                game.slave_giving(slave)
                game.slave_giving(vice_slave)
                game.win_giving(king)
                game.win_giving(queen)
                game.rotate_dir()
                reset = True
                print("---------------------- Start the Game ---------------------")
            elif respond == "N":
                game_end = True
            else:
                print("Invalid Response")


    #Always default index to last player since other are removed from play_order_round already
    #If player played card and not out of the game yet
    if last_main_deck != len(main_deck) and last_turn_len == len(play_order_round):
        last_player = play_order_round[play_idx]
        print("Last Player: " , last_player.name)
    if last_player != None and last_player in play_order_round:
        play_idx = play_order_round.index(last_player)
    elif last_player not in play_order and last_second_player != None:
        play_idx = play_order_round.index(last_second_player)

    #Make Index Not go out of order(Perfected)
    if dir and not game_end and not reset:
        if last_player == None:
            play_idx = 0
        else:
            play_idx += 1
    elif not dir and not game_end and not reset:
        if last_player == None:
            play_idex = len(play_order_round) - 1
        else:
            play_idx -= 1
    if play_idx > len(play_order_round) - 1:
        play_idx = 0
    elif play_idx < 0:
        play_idx = len(play_order_round) - 1
    reset = False

print("Game has ended")