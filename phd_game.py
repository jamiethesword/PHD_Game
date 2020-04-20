# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 11:02:35 2020

@author: Jamie Dowie (jamie_d1@hotmail.co.uk)
"""

import random, time
from operator import itemgetter
interval = 0.5

############################## LIST OF FUNCTIONS ##############################

## build_deck(cards)
## deal(cards, deal_size)
## make_round_hand(hand1, hand2)
## high_card(cards)
## got_pair(cards)
## twopair(cards)
## got3(cards)
## straight(cards)
## flush(cards)
## got_house(cards)
## got4(cards)
## strfl(cards)
## royfl(cards)
## find_combos(cards)
## direct_swap(swap_cards, player_cards, common_cards, current_deck, burn_cards)
## select_swap(hand, player_cards, common_cards, current_deck, burn_cards)
## pause(seconds)
## player_turn()
## computer_turn()
## game(p1hp, p2hp, playercards, opponentcards, commoncards)

## GOOD ASCII FONTS ##
## DOOM
## Sub-Zero
## Elite
## AMC Razor
## Chunky
## Caligraphy


###################################  DATA  ####################################

## Libraries containing cards and their attributes

Ace_of_hearts = {'value': 'ace', 'suit': 'hearts', 'number': 1}
Two_of_hearts = {'value': 'two', 'suit': 'hearts', 'number': 2}
Three_of_hearts = {'value': 'three', 'suit': 'hearts', 'number': 3}
Four_of_hearts = {'value': 'four', 'suit': 'hearts', 'number': 4}
Five_of_hearts = {'value': 'five', 'suit': 'hearts', 'number': 5}
Six_of_hearts = {'value': 'six', 'suit': 'hearts', 'number': 6}
Seven_of_hearts = {'value': 'seven', 'suit': 'hearts', 'number': 7}
Eight_of_hearts = {'value': 'eight', 'suit': 'hearts', 'number': 8}
Nine_of_hearts = {'value': 'nine', 'suit': 'hearts', 'number': 9}
Ten_of_hearts = {'value': 'ten', 'suit': 'hearts', 'number': 10}
Jack_of_hearts = {'value': 'jack', 'suit': 'hearts', 'number': 11}
Queen_of_hearts = {'value': 'queen', 'suit': 'hearts', 'number': 12}
King_of_hearts = {'value': 'king', 'suit': 'hearts', 'number': 13}

Ace_of_diamonds = {'value': 'ace', 'suit': 'diamonds', 'number': 1}
Two_of_diamonds = {'value': 'two', 'suit': 'diamonds', 'number': 2}
Three_of_diamonds = {'value': 'three', 'suit': 'diamonds', 'number': 3}
Four_of_diamonds = {'value': 'four', 'suit': 'diamonds', 'number': 4}
Five_of_diamonds = {'value': 'five', 'suit': 'diamonds', 'number': 5}
Six_of_diamonds = {'value': 'six', 'suit': 'diamonds', 'number': 6}
Seven_of_diamonds = {'value': 'seven', 'suit': 'diamonds', 'number': 7}
Eight_of_diamonds = {'value': 'eight', 'suit': 'diamonds', 'number': 8}
Nine_of_diamonds = {'value': 'nine', 'suit': 'diamonds', 'number': 9}
Ten_of_diamonds = {'value': 'ten', 'suit': 'diamonds', 'number': 10}
Jack_of_diamonds = {'value': 'jack', 'suit': 'diamonds', 'number': 11}
Queen_of_diamonds = {'value': 'queen', 'suit': 'diamonds', 'number': 12}
King_of_diamonds = {'value': 'king', 'suit': 'diamonds', 'number': 13}

Ace_of_spades = {'value': 'ace', 'suit': 'spades', 'number': 1}
Two_of_spades = {'value': 'two', 'suit': 'spades', 'number': 2}
Three_of_spades = {'value': 'three', 'suit': 'spades', 'number': 3}
Four_of_spades = {'value': 'four', 'suit': 'spades', 'number': 4}
Five_of_spades = {'value': 'five', 'suit': 'spades', 'number': 5}
Six_of_spades = {'value': 'six', 'suit': 'spades', 'number': 6}
Seven_of_spades = {'value': 'seven', 'suit': 'spades', 'number': 7}
Eight_of_spades = {'value': 'eight', 'suit': 'spades', 'number': 8}
Nine_of_spades = {'value': 'nine', 'suit': 'spades', 'number': 9}
Ten_of_spades = {'value': 'ten', 'suit': 'spades', 'number': 10}
Jack_of_spades = {'value': 'jack', 'suit': 'spades', 'number': 11}
Queen_of_spades = {'value': 'queen', 'suit': 'spades', 'number': 12}
King_of_spades = {'value': 'king', 'suit': 'spades', 'number': 13}

Ace_of_clubs = {'value': 'ace', 'suit': 'clubs', 'number': 1}
Two_of_clubs = {'value': 'two', 'suit': 'clubs', 'number': 2}
Three_of_clubs = {'value': 'three', 'suit': 'clubs', 'number': 3}
Four_of_clubs = {'value': 'four', 'suit': 'clubs', 'number': 4}
Five_of_clubs = {'value': 'five', 'suit': 'clubs', 'number': 5}
Six_of_clubs = {'value': 'six', 'suit': 'clubs', 'number': 6}
Seven_of_clubs = {'value': 'seven', 'suit': 'clubs', 'number': 7}
Eight_of_clubs = {'value': 'eight', 'suit': 'clubs', 'number': 8}
Nine_of_clubs = {'value': 'nine', 'suit': 'clubs', 'number': 9}
Ten_of_clubs = {'value': 'ten', 'suit': 'clubs', 'number': 10}
Jack_of_clubs = {'value': 'jack', 'suit': 'clubs', 'number': 11}
Queen_of_clubs = {'value': 'queen', 'suit': 'clubs', 'number': 12}
King_of_clubs = {'value': 'king', 'suit': 'clubs', 'number': 13}

## list containing the full deck of cards which can be pulled into a game
deck = [Ace_of_hearts, Two_of_hearts, Three_of_hearts, Four_of_hearts,
        Five_of_hearts, Six_of_hearts, Seven_of_hearts, Eight_of_hearts,
        Nine_of_hearts, Ten_of_hearts, Jack_of_hearts, Queen_of_hearts,
        King_of_hearts,
        Ace_of_diamonds, Two_of_diamonds, Three_of_diamonds, Four_of_diamonds,
        Five_of_diamonds, Six_of_diamonds, Seven_of_diamonds,
        Eight_of_diamonds, Nine_of_diamonds, Ten_of_diamonds, Jack_of_diamonds,
        Queen_of_diamonds, King_of_diamonds,
        Ace_of_spades, Two_of_spades, Three_of_spades, Four_of_spades,
        Five_of_spades, Six_of_spades, Seven_of_spades, Eight_of_spades,
        Nine_of_spades, Ten_of_spades, Jack_of_spades, Queen_of_spades,
        King_of_spades,
        Ace_of_clubs, Two_of_clubs, Three_of_clubs, Four_of_clubs,
        Five_of_clubs, Six_of_clubs, Seven_of_clubs, Eight_of_clubs,
        Nine_of_clubs, Ten_of_clubs, Jack_of_clubs, Queen_of_clubs,
        King_of_clubs]

###############################################################################

################################## SORTING HANDS ##############################

## This function pulls a deck in and shuffles them for a game
def build_deck(cards):
    game_deck = list(cards)
    random.shuffle(game_deck)
    return game_deck

## This function takes a game deck in and deals a given number to a player or
## common cards NB: requires game_deck to be in play or will error out
def deal(cards, deal_size):
    dealt_cards = []
    for i in range(deal_size):
        pulled_card = random.choice(cards)
        cards.remove(pulled_card)
        dealt_cards.append(pulled_card)       
    return dealt_cards

## This function assembles and sorts a combined hand
    
def make_round_hand(hand1, hand2):
    sorted_hand = sorted(hand1 + hand2, key=itemgetter('number'))
    return sorted_hand

################################### CHECKING HANDS ############################

## This function identifies a player's high card
    
def high_card(cards):
    return cards[-1]

## This function identifies if the player has a pair & returns the highest pair

def got_pair(cards):
    pair = 0
    for i in range(len(cards) - 1):
        if cards[i]['number'] == cards[i + 1]['number']:
            pair = [cards[i], cards[i + 1]]
    if pair != 0:
        return pair
    else:
        return 0

## This function identifies if the player has 2 pair and returns the highest 2

def twopair(cards):
    two_pair = []
    for i in range(len(cards) - 1):
        if cards[i]['number'] == cards[i + 1]['number']:
            if two_pair == []:
                two_pair.extend([cards[i], cards[i + 1]])            
            elif cards[i] != two_pair[-1]:
                two_pair.extend([cards[i], cards[i + 1]])
    if len(two_pair) >= 4:
        return two_pair[-4:]
    else:
        return 0

## This function identifies if the player has 3oak and returns the highest 3
        
def got3(cards):
    trips = 0
    for i in range(len(cards) - 2):
        if cards[i]['number'] == cards[i + 1]['number'] == cards[i + 2]['number']:
            trips = [cards[i], cards[i + 1], cards[i + 2]]
    if trips != 0:
        return trips
    else:
        return 0

## This function identifies if the player has a straight & returns the highest
## straight
        
def straight(cards):
    cards_copy = list(cards)
    straight = 0
    for i in range(len(cards_copy) - 2):
        if cards_copy[i]['number'] == cards_copy[i + 1]['number']:
            cards_copy[i] = 'duplicate'
    while 'duplicate' in cards_copy:
        cards_copy.remove('duplicate')
    for i in range(len(cards_copy) - 4):
        if (cards_copy[i]['number']
            == cards_copy[i + 1]['number'] - 1
            == cards_copy[i + 2]['number'] - 2
            == cards_copy[i + 3]['number'] - 3
            == cards_copy[i + 4]['number'] - 4):
            straight = ([cards_copy[i], cards_copy[i + 1], cards_copy[i + 2],
                         cards_copy[i + 3], cards_copy[i + 4]])
    if straight != 0:
        return straight
    else:
        return 0
    
## This function identifies if the player has a flush and returns highest flush
        
def flush(cards):
    hearts_count = 0
    clubs_count = 0
    spades_count = 0
    diamonds_count = 0
    hearts_hand = []
    clubs_hand = []
    spades_hand = []
    diamonds_hand = []
    for i in range(len(cards)):
        if cards[i]['suit'] == 'hearts':
            hearts_count += 1
            hearts_hand.extend([cards[i]])
        elif cards[i]['suit'] == 'clubs':
            clubs_count += 1
            clubs_hand.extend([cards[i]])
        elif cards[i]['suit'] == 'spades':
            spades_count += 1
            spades_hand.extend([cards[i]])
        elif cards[i]['suit'] == 'diamonds':
            diamonds_count += 1
            diamonds_hand.extend([cards[i]])
    if hearts_count >= 5:
        return hearts_hand[-5:]
    elif clubs_count >= 5:
        return clubs_hand[-5:]
    elif spades_count >= 5:
        return spades_hand[-5:]
    elif diamonds_count >= 5:
        return diamonds_hand[-5:]
    else:
        return 0

## this function identifies if the player has a full house and returns it
def got_house(cards):
    house = []   #House is set to 0 by defualt and filled in as a list of cards
    test = 0    #Test is filled in with a 1 when a pair is found and 
    ## 2 when trips found, and if the function ends with test = 3 then the
    ## cards are returned as the output
    
    ## Below is the test for a pair, taking extra care to make sure it's *only* 
    ## a pair and not picking up 3 of a kind
    for i in range(len(cards) - 1):
        ## this is checking that the 2nd last card is part of a pair with the
        ## last card, and is seperated from the main ELSE argument so we don't
        ## go out of the range
        if cards[i] == cards[-2]:
            if (test != 1 and cards[i]['number'] == cards[i + 1]['number']
                != cards[i - 1]['number']):
                house = [cards[i], cards[i + 1]]
                test += 1
        ## this is checking that the third last card is part of a pair with the
        ## second last card and is seperated from the main ELSE argument so we 
        ## don't go out of the range
        elif cards[i] == cards[-3]:
            if (test != 1 and cards[i]['number'] == cards[i + 1]['number']
                != cards[i + 2]['number'] and cards[i]['number'] 
                != cards[i - 1]['number']):
                house = [cards[i], cards[i + 1]]
                test += 1
        ## this is checking the first card is part of a pair with the second
        ## card and is seperated from the main ELSE argument so we don't go out
        ## of the range
        elif cards[i] == cards[0]:
            if (test != 1 and cards[i]['number'] == cards[i + 1]['number']
            != cards[i + 2]['number']):
                house = [cards[i], cards[i + 1]]
                test += 1
        ## main test of a pair, making sure only a pair and not trips with the 
        ## card one before or two after
        else:
            if (test != 1 and cards[i]['number'] == cards[i + 1]['number']
                != cards[i + 2]['number'] and cards[i]['number']
                != cards[i - 1]['number']):
                house = [cards[i], cards[i + 1]]
                test += 1
    ## test for trips, range is -2 so that we don't fall out of range looking
    ## for cards after the last two cards
    for i in range(len(cards) - 2):
        if (cards[i]['number'] == cards[i + 1]['number']
            == cards[i + 2]['number']):
            house.extend([cards[i], cards[i + 1], cards[i + 2]])
            test += 2
    if test >= 3:
        return house[-5:]
    else:
        return 0
    
## this function identifies if the player has 4oak and returns this
def got4(cards):
    four = 0
    for i in range(len(cards) - 3):
        if (cards[i]['number'] == cards[i + 1]['number']
        == cards[i + 2]['number'] == cards[i + 3]['number']):
            four = [cards[i], cards[i + 1], cards[i + 2], cards[i + 3]]
    if four != 0:
        return four
    else:
        return 0

## this function identifies if the player has a straight flush
def strfl(cards):
    straight_flush = 0
    hearts_count = 0
    clubs_count = 0
    spades_count = 0
    diamonds_count = 0
    hearts_hand = []
    clubs_hand = []
    spades_hand = []
    diamonds_hand = []
    for i in range(len(cards)):
        if cards[i]['suit'] == 'hearts':
            hearts_count += 1
            hearts_hand.extend([cards[i]])
        elif cards[i]['suit'] == 'clubs':
            clubs_count += 1
            clubs_hand.extend([cards[i]])
        elif cards[i]['suit'] == 'spades':
            spades_count += 1
            spades_hand.extend([cards[i]])
        elif cards[i]['suit'] == 'diamonds':
            diamonds_count += 1
            diamonds_hand.extend([cards[i]])
    if hearts_count >= 5:
        for i in range(len(hearts_hand) - 4):
            if (hearts_hand[i]['number']
             == hearts_hand[i + 1]['number'] - 1
             == hearts_hand[i + 2]['number'] - 2
             == hearts_hand[i + 3]['number'] - 3
             == hearts_hand[i + 4]['number'] - 4):
                 straight_flush = ([hearts_hand[i], hearts_hand[i + 1],
                                     hearts_hand[i + 2], hearts_hand[i + 3],
                                     hearts_hand[i + 4]])
    elif clubs_count >= 5:
        for i in range(len(clubs_hand) - 4):
            if (clubs_hand[i]['number']
             == clubs_hand[i + 1]['number'] - 1
             == clubs_hand[i + 2]['number'] - 2
             == clubs_hand[i + 3]['number'] - 3
             == clubs_hand[i + 4]['number'] - 4):
                 straight_flush = ([clubs_hand[i], clubs_hand[i + 1],
                                     clubs_hand[i + 2], clubs_hand[i + 3],
                                     clubs_hand[i + 4]])
    elif spades_count >= 5:
        for i in range(len(spades_hand) - 4):
            if (spades_hand[i]['number']
             == spades_hand[i + 1]['number'] - 1
             == spades_hand[i + 2]['number'] - 2
             == spades_hand[i + 3]['number'] - 3
             == spades_hand[i + 4]['number'] - 4):
                 straight_flush = ([spades_hand[i], spades_hand[i + 1],
                                     spades_hand[i + 2], spades_hand[i + 3],
                                     spades_hand[i + 4]])
    elif diamonds_count >= 5:
        for i in range(len(diamonds_hand) - 4):
            if (diamonds_hand[i]['number']
             == diamonds_hand[i + 1]['number'] - 1
             == diamonds_hand[i + 2]['number'] - 2
             == diamonds_hand[i + 3]['number'] - 3
             == diamonds_hand[i + 4]['number'] - 4):
                 straight_flush = ([diamonds_hand[i], diamonds_hand[i + 1],
                                     diamonds_hand[i + 2], diamonds_hand[i + 3],
                                     diamonds_hand[i + 4]])    
    if straight_flush != 0:
        return straight_flush
    else:
        return 0

## this function identifies if the player has a straight flush
def royfl(cards):
    royal_flush = 0
    hearts_count = 0
    clubs_count = 0
    spades_count = 0
    diamonds_count = 0
    hearts_hand = []
    clubs_hand = []
    spades_hand = []
    diamonds_hand = []
    for i in range(len(cards)):
        if cards[i]['suit'] == 'hearts':
            hearts_count += 1
            hearts_hand.extend([cards[i]])
        elif cards[i]['suit'] == 'clubs':
            clubs_count += 1
            clubs_hand.extend([cards[i]])
        elif cards[i]['suit'] == 'spades':
            spades_count += 1
            spades_hand.extend([cards[i]])
        elif cards[i]['suit'] == 'diamonds':
            diamonds_count += 1
            diamonds_hand.extend([cards[i]])
    if hearts_count >= 5:
        for i in range(len(hearts_hand) - 4):
            if (hearts_hand[i]['number'] == 9 and
                hearts_hand[i]['number']
             == hearts_hand[i + 1]['number'] - 1
             == hearts_hand[i + 2]['number'] - 2
             == hearts_hand[i + 3]['number'] - 3
             == hearts_hand[i + 4]['number'] - 4):
                 royal_flush = ([hearts_hand[i], hearts_hand[i + 1],
                                     hearts_hand[i + 2], hearts_hand[i + 3],
                                     hearts_hand[i + 4]])
    if clubs_count >= 5:
        for i in range(len(clubs_hand) - 4):
            if (clubs_hand[i]['number'] == 9 and
                clubs_hand[i]['number']
             == clubs_hand[i + 1]['number'] - 1
             == clubs_hand[i + 2]['number'] - 2
             == clubs_hand[i + 3]['number'] - 3
             == clubs_hand[i + 4]['number'] - 4):
                 royal_flush = ([clubs_hand[i], clubs_hand[i + 1],
                                     clubs_hand[i + 2], clubs_hand[i + 3],
                                     clubs_hand[i + 4]])
    if spades_count >= 5:
        for i in range(len(spades_hand) - 4):
            if (spades_hand[i]['number'] == 9 and
                spades_hand[i]['number']
             == spades_hand[i + 1]['number'] - 1
             == spades_hand[i + 2]['number'] - 2
             == spades_hand[i + 3]['number'] - 3
             == spades_hand[i + 4]['number'] - 4):
                 royal_flush = ([spades_hand[i], spades_hand[i + 1],
                                     spades_hand[i + 2], spades_hand[i + 3],
                                     spades_hand[i + 4]])
    if diamonds_count >= 5:
        for i in range(len(diamonds_hand) - 4):
            if (diamonds_hand[i]['number'] == 9 and
                diamonds_hand[i]['number']
             == diamonds_hand[i + 1]['number'] - 1
             == diamonds_hand[i + 2]['number'] - 2
             == diamonds_hand[i + 3]['number'] - 3
             == diamonds_hand[i + 4]['number'] - 4):
                 royal_flush = ([diamonds_hand[i], diamonds_hand[i + 1],
                                     diamonds_hand[i + 2], diamonds_hand[i + 3],
                                     diamonds_hand[i + 4]])    
    if royal_flush != 0:
        return royal_flush
    else:
        return 0
    

################################### GAME RULES ################################

## The rules set out what happens when a particular hand is played, as well as 
## a description to be referenced towards the end of the game() function
        
play_high_card       = {'hp': 0,   'action': 'swap selected', 'end_turn': 'yes', 'description': 'High Card'}
play_pair            = {'hp': 0,   'action': 'swap played',   'end_turn': 'yes', 'description': 'Pair'}
play_two_pair        = {'hp': 3,   'action': 'swap played',   'end_turn': 'no', 'description': 'Two Pairs'}
play_three_of_a_kind = {'hp': 5,   'action': 'swap played',   'end_turn': 'no', 'description': 'Three of a Kind'}
play_straight        = {'hp': 10,  'action': 'swap played',   'end_turn': 'no', 'description': 'Straight'}
play_flush           = {'hp': 15,  'action': 'swap played',   'end_turn': 'no', 'description': 'Flush'}
play_full_house      = {'hp': 20,  'action': 'swap played',   'end_turn': 'no', 'description': 'Full House'}
play_four_of_a_kind  = {'hp': 30,  'action': 'swap played',   'end_turn': 'no', 'description': 'Four of a Kind'}
play_straight_flush  = {'hp': 50,  'action': 'swap played',   'end_turn': 'no', 'description': 'Straight Flush'}
play_royal_flush     = {'hp': 100, 'action': 'swap played',   'end_turn': 'no', 'description': 'Royal Flush'}

## Pulling the rules into a list which can be called by the game function

rules = [play_high_card, play_pair, play_two_pair, play_three_of_a_kind,
        play_straight, play_flush, play_full_house, play_four_of_a_kind,
        play_straight_flush, play_royal_flush]

#turn = []

##################################### GAME ####################################

## This function identifies all the combinations of winning hands and builds 2 
## lists, one of the combinations and another a description of the combinations
## These are then returned as a tuple of lists

def find_combos(cards):
    combos = [[high_card(cards)]]
    combos_desc = ['High Card']
    if got_pair(cards) != 0:
        combos.append(got_pair(cards))
        combos_desc.append('Pair')
    if twopair(cards) != 0:
        combos.append(twopair(cards))
        combos_desc.append('Two Pairs')
    if got3(cards) != 0:
        combos.append(got3(cards))
        combos_desc.append('Three of a Kind')
    if straight(cards) != 0:
        combos.append(straight(cards))
        combos_desc.append('Straight')    
    if flush(cards) != 0:
        combos.append(flush(cards))
        combos_desc.append('Flush')    
    if got_house(cards) != 0:
        combos.append(got_house(cards))
        combos_desc.append('Full House')
    if got4(cards) != 0:
        combos.append(got4(cards))
        combos_desc.append('Four of a Kind')
    if strfl(cards) != 0:
        combos.append(strfl(cards))
        combos_desc.append('Straight Flush')
    if royfl(cards) != 0:
        combos.append(royfl(cards))
        combos_desc.append('Royal Flush')

    return combos, combos_desc

## this function swaps out specific cards when a hand is played. The first
## nested for loop finds any cards to be swapped in the players' hand, removes
## them, replaces them with a random card from the deck and adds the removed
## cards to a burn deck. The second nested loop does the exact same for the
## common cards
    
def direct_swap(swap_cards, player_cards, common_cards, current_deck, burn_cards):
    for i in range(len(swap_cards)):
        for j in range(len(player_cards)):
            if swap_cards[i] == player_cards[j]:
                burn_cards.append(player_cards[j])
                player_cards.remove(player_cards[j])
                pulled_card = random.choice(current_deck)
                current_deck.remove(pulled_card)
                player_cards.append(pulled_card)
        for k in range(len(common_cards)):
            if swap_cards[i] == common_cards[k]:
                burn_cards.append(common_cards[k])
                common_cards.remove(common_cards[k])
                pulled_card = random.choice(current_deck)
                current_deck.remove(pulled_card)
                common_cards.append(pulled_card)

def select_swap(hand, player_cards, common_cards, current_deck, burn_cards):
    if turn != 'Player 2':
        print()
        for i in range(len(player_hand)):
            print('Type ' + str(i + 1) + ' to swap ' + str(hand[i]['value'] + ' of ' + hand[i]['suit']))
    if turn == 'Player 1':
        player_entry = 'invalid'
        while player_entry != 'valid':
            select = 'not a number'
            print()
            while select.isdigit() == False:
                select = input()
                if select.isdigit() == False:
                    print('Please type a number between 1 and ' + str(len(player_hand)))
            select = int(select)
            #if isinstance(select, int) == True:
            if select > 0 and select < len(player_hand) + 1:
                player_entry = 'valid'
            else:
                print('Please type a number between 1 and ' + str(len(player_hand)))
    elif turn == 'Player 2':
        select = random.randint(1, int(len(player_hand)))
    for j in range(len(player_cards)):
        if hand[select - 1] == player_cards[j]:
            burn_cards.append(player_cards[j])
            player_cards.remove(player_cards[j])
            pulled_card = random.choice(current_deck)
            current_deck.remove(pulled_card)
            player_cards.append(pulled_card)
    for k in range (len(common_cards)):
        if hand[select - 1] == common_cards[k]:
            burn_cards.append(common_cards[k])
            common_cards.remove(common_cards[k])
            pulled_card = random.choice(current_deck)
            current_deck.remove(pulled_card)
            common_cards.append(pulled_card)

def pause(seconds):
    time.sleep(seconds)

def player_turn():
    pause(interval * 2)   
    print()
    print('~~~Your turn~~~')
    print()
    ## hands are printed 
    pause(interval * 2)
    print('Communal Cards:')
    for i in range(len(communal_cards)):
        pause(interval)
        print(communal_cards[i - 1]['value'] + ' of ' + communal_cards[i - 1]['suit'])
    print()
    pause(interval * 4)
    print('Your Cards:')
    for i in range(len(player_1['cards'])):
        pause(interval)
        print(player_1['cards'][i - 1]['value'] + ' of ' + player_1['cards'][i - 1]['suit'])
    print()
    pause(interval * 4)
    print('Opponent Cards:')
    for i in range(len(player_2['cards'])):
        pause(interval)
        print('???')
    print()
    
    pause(interval * 2)
    ## Possible hand combinations which can be played are printed
    print('You have the following hands:')
    ## First for loop prints the type of combination
    for i in range(len(find_combos(player_hand)[1])):
        print(find_combos(player_hand)[1][i])
        pause(interval)
        print('***')
        ## NESTED FOR LOOPS SUUUUCK.
        ## Nested for loop prints the cards which make up that combination
        for j in range(len(find_combos(player_hand)[0][i])):
            print(find_combos(player_hand)[0][i][j]['value'] + ' of ' + find_combos(player_hand)[0][i][j]['suit'])
        print('***')
    pause(interval * 2)
    print('Your move:')
    ## For loop which shows the hands which can be played
    for i in range(len(find_combos(player_hand)[1])):
        print('Type ' + str(i + 1) + ' to play your ' + (find_combos(player_hand)[1][i]))
    
    ## Player responds with a number as directed
    player_response = 'invalid'
    while player_response != 'valid':
        response = 'not a number'
        print()
        while response.isdigit() == False:
            response = input()
            if response.isdigit() == False:
                print('Please type a number between 1 and ' + str(len(find_combos(player_hand)[1])))
        response = int(response)
        #if isinstance(select, int) == True:
        if response > 0 and response < len(find_combos(player_hand)[1]) + 1:
            player_response = 'valid'
        else:
            print('Please type a number between 1 and ' + str(len(find_combos(player_hand)[1])))
    
    ## Player responds with a number as directed
#    response = int(input())
    
    ## two variables are created off the back of this entry, the played
    ## combination and the individial cards in the combination
    played_combination = find_combos(player_hand)[1][response - 1]
    played_cards = find_combos(player_hand)[0][response - 1]
    
    ## looping through the rules to find the one relevant to the combination
    ## selected and assigning it to a variable played_action
    for i in range(len(rules)):
        if played_combination == rules[i]['description']:
            played_action = rules[i]
    
    ## if the combination generates a direct swap then this function is called 
    if played_action['action'] == 'swap played':
        direct_swap(played_cards, player['cards'], communal_cards, game_deck, burn_deck)
    elif played_action['action'] == 'swap selected':
        select_swap(player_hand, player['cards'], communal_cards, game_deck, burn_deck)
    ## the current player is identified and the opposing player is penalised
    ## the appropriate number of points
    pause(interval * 2)
    player_2['HP'] -= played_action['hp']
    print(str(played_action['hp']) + ' damage done, your opponent\'s HP is now ' + str(player_2['HP']))
    pause(interval * 2)
    ## if the turn should be ended then the player turns are swapped
    if played_action['end_turn'] == 'yes':
        return 'Player 2'
    else:
        return 'Player 1'
    
def computer_turn():
    pause(interval * 2)   
    print()
    print('~~~Opponent\'s turn~~~')
    print()
    ## hands are printed
    pause(interval)
    print('Communal Cards:')
    for i in range(len(communal_cards)):
        pause(interval)
        print(communal_cards[i - 1]['value'] + ' of ' + communal_cards[i - 1]['suit'])
    print()
    pause(interval * 3)
    print('Your Cards:')
    pause(interval)
    for i in range(len(player_1['cards'])):
        pause(interval)
        print(player_1['cards'][i - 1]['value'] + ' of ' + player_1['cards'][i - 1]['suit'])
    print()
    pause(interval * 3)
    print('Opponent Cards:')
    for i in range(len(player_2['cards'])):
        pause(interval)
        print('???')
    print()
    
    pause(interval * 3)
    ## Possible hand combinations which can be played are printed
    print('Your opponent has ' +  str(len(find_combos(player_hand)[0])) + ' hands available')
    ## First for loop prints the type of combination
    
    ## Player responds with a number as directed
    response = int(len(find_combos(player_hand)[0]))
    
    ## two variables are created off the back of this entry, the played
    ## combination and the individial cards in the combination
    played_combination = find_combos(player_hand)[1][response - 1]
    played_cards = find_combos(player_hand)[0][response - 1]
    pause(interval * 2)
    print('Your opponent played ' + played_combination)
    
    ## looping through the rules to find the one relevant to the combination
    ## selected and assigning it to a variable played_action
    for i in range(len(rules)):
        if played_combination == rules[i]['description']:
            played_action = rules[i]
    
    ## if the combination generates a direct swap then this function is called 
    if played_action['action'] == 'swap played':
        direct_swap(played_cards, player['cards'], communal_cards, game_deck, burn_deck)
    elif played_action['action'] == 'swap selected':
        select_swap(player_hand, player['cards'], communal_cards, game_deck, burn_deck)
    ## the current player is identified and the opposing player is penalised
    ## the appropriate number of points
    pause(interval * 2)
    player_1['HP'] -= played_action['hp']
    print(str(played_action['hp']) + ' damage done, Your HP is now ' + str(player_1['HP']))
    ## if the turn should be ended then the player turns are swapped
    if played_action['end_turn'] == 'yes':
        return 'Player 1'
    else:
        return 'Player 2'

## GETTING AN ERROR WHEN ONLY 1 CARD IS SELECTED (UNLESS MASKED AS A RANGE i.e. [0:2])
## NEED TO SEE HOW THIS IMPACTS WHEN ACTUALLY CALLED, BUT HOPEFULLY NO ISSUE 
## BECAUSE MINIMUM WITH THIS IS A PAIR

def game(p1hp, p2hp, playercards, opponentcards, commoncards):
## Players are assigned points and an empty set of cards in a dictionary, as
## well as an empty set of communal cards and burn deck
    global player_1
    global player_2
    global communal_cards
    global burn_deck
    global player_hand
    global game_deck
    global player
    global turn
    player_1 = {'HP' : p1hp, 'cards': 0}
    player_2 = {'HP' : p2hp, 'cards': 0}
    communal_cards = 0
    burn_deck = []
    
    ## Game deck is built and shuffled, players and communal are dealt random cards
    game_deck = build_deck(deck)
    player_1['cards'] = deal(game_deck, playercards)
    player_2['cards'] = deal(game_deck, opponentcards)
    communal_cards = deal(game_deck, commoncards)
    turn = 'Player 1'
    
    
    
    ## starts the for loop which remains until a player's HP is spent
    while player_1['HP'] > 0 and player_2['HP'] > 0:
        ## The players' hands are derived and sorted from low to high
        player_1_hand = make_round_hand(player_1['cards'], communal_cards)
        player_2_hand = make_round_hand(player_2['cards'], communal_cards)
        
        if len(game_deck) < 10:
            game_deck = game_deck + burn_deck
            burn_deck = []
            print('Game deck replenished with burn deck cards')
            
        ## player_hand allows actions to be taken on either players' hands
        ## independently
    
        if turn == 'Player 1':
            player_hand = player_1_hand
            player = player_1
            turn = player_turn()
            print(str(len(game_deck)) + ' cards left in the main deck')
            print(str(len(burn_deck)) + ' cards now in the burn deck')
        
        elif turn == 'Player 2' and player_2['HP'] > 0:
            player_hand = player_2_hand
            player = player_2
            turn = computer_turn()
            print(str(len(game_deck)) + ' cards left in the main deck')
            print(str(len(burn_deck)) + ' cards now in the burn deck')
      
    if player_1['HP'] < 1:
        print('You Lose!')
        return 'You Lose!'
    
    elif player_2['HP'] < 1:
        return 'You Win!'

#####TODO#####

complete = 'restart'
cheat_code = 'locked'


while complete.upper() != 'QUIT':

    print('          ██████╗ ██╗  ██╗   ██████╗               ')
    pause(0.05)
    print('          ██╔══██╗██║  ██║   ██╔══██╗              ')
    pause(0.05)
    print('          ██████╔╝███████║   ██║  ██║              ')
    pause(0.05)
    print('          ██╔═══╝ ██╔══██║   ██║  ██║              ')
    pause(0.05)
    print('          ██║██╗  ██║  ██║██╗██████╔╝              ')
    pause(0.05)
    print('          ╚═╝╚═╝  ╚═╝  ╚═╝╚═╝╚═════╝               ')
    pause(2)
    print(' ')
    print('          ______     _                 ')
    pause(0.05)
    print('          | ___ \   | |                ')
    pause(0.05)
    print('          | |_/ /__ | | _____ _ __     ')
    pause(0.05)
    print('          |  __/ _ \| |/ / _ \ \'__|   ')
    pause(0.05)
    print('          | | | (_) |   <  __/ |       ')
    pause(0.05)
    print('          \_|  \___/|_|\_\___|_|       ') 
    pause(1)
    print('           _   _                 _      ')
    pause(0.05)
    print('          | | | |               | |    ')
    pause(0.05)
    print('          | |_| | __ _ _ __   __| |    ')
    pause(0.05)
    print('          |  _  |/ _` | \'_ \ / _` |    ')
    pause(0.05)
    print('          | | | | (_| | | | | (_| |    ')
    pause(0.05)
    print('          \_| |_/\__,_|_| |_|\__,_|    ') 
    pause(1)
    print('          ______            _       ')
    pause(0.05)
    print('          |  _  \          | |      ')
    pause(0.05)
    print('          | | | |_   _  ___| |      ')
    pause(0.05)
    print('          | | | | | | |/ _ \ |      ')
    pause(0.05)
    print('          | |/ /| |_| |  __/ |      ')
    pause(0.05)
    print('          |___/  \__,_|\___|_|      ')
    print(' ')
    pause(1)
    print('          Copyright Jamie Dowie 2020')
    pause(0.05)
    print(' ')
    pause(3)
    print(' ')
    pause(0.05)
    print(' ')
    pause(0.05)
    print(' ')
    pause(0.05)
    print('For best resolution expand window to full screen')
    pause(1)
    print('          Press Enter to Continue   ')
    cont = input()
        
    pause(1)
    player_HP = 40
    hand_size = 3
    game_1 = 'not won'
    game_2 = 'not won'
    game_3 = 'not won'
    game_4 = 'not won'
    game_5 = 'not won'
    game_6 = 'not won'
    skip = 'no'
    menu_exit = 'no'
    
    for i in range(40):
        pause(0.05)
        print(' ')
       
    
    print(' ___ ___   ____  ____  ____       ___ ___    ___  ____   __ __ ')
    pause(0.05)
    print('|   |   | /    ||    ||    \     |   |   |  /  _]|    \ |  |  |')
    pause(0.05)
    print('| _   _ ||  o  | |  | |  _  |    | _   _ | /  [_ |  _  ||  |  |')
    pause(0.05)
    print('|  \_/  ||     | |  | |  |  |    |  \_/  ||    _]|  |  ||  |  |')
    pause(0.05)
    print('|   |   ||  _  | |  | |  |  |    |   |   ||   [_ |  |  ||  :  |')
    pause(0.05)
    print('|   |   ||  |  | |  | |  |  |    |   |   ||     ||  |  ||     |')
    pause(0.05)
    print('|___|___||__|__||____||__|__|    |___|___||_____||__|__| \__,_|')
    pause(0.05)
    print(' ')
    pause(0.05)
    print(' ')
    pause(0.05)
    print(' ')                                                                  
    pause(1)

    while menu_exit == 'no':        
        print(' ')
        pause(0.05)
        print(' ')
        pause(0.05)
        print(' ')
        print('Type one of the following options and press enter')
        pause(1)
        print('1. Start Story Mode')
        pause(0.05)
        print('2. How to Play')
        pause(0.05)
        print('3. Enter Cheat Code.')
        if cheat_code.upper() == 'GORDON':
            pause(0.05)
            print('4. Free Play Mode')
        print(' ')
        menu_response = input()
        
        if menu_response == '1':
            menu_exit = 'yes'
        
        elif menu_response == '2':
            pause(1)
            print('How to Play:')
            pause(1)
            print('Each player is dealt a set of cards from a reglar, shuffled deck of 52 cards.')
            pause(8)
            print('The player\'s cards must be combined with a set of communal cards to create a poker hand.')
            pause(8)
            print('This is similar to many variants of poker, such as Texas Hold\'em.')            
            pause(8)
            print('Players can select from any available hand, for example if a player\'s strongest...')
            print('...hand is three of a kind the player can select the three of a kind, or a pair, or the high card.')
            pause(8)
            print('Playing a high card lets you select any card to burn, whereas playing a combination hand burns those specific cards,...')
            print('...in both cases to be replenished by a new card from the main deck.')
            pause(8)
            print('Burned cards are collected in a seperate burn deck until the main deck has less than 10 cards,...')
            print('...at which point the burn cards will be added to the main deck and this replenished main deck shuffled.')
            pause(12)            
            print('Each player has a hit point (HP) score. The points scored by a player in their turn...')
            print('...will be deducted from their opponent\'s HP score.')
            pause(8)
            print('Playing anything higher than a pair lets you take another turn, playing a pair or high card moves the turn on to your opponent.')
            pause(8)
            print('The first player to get their opponent\'s HP score to 0 or lower wins.')
            pause(8)
            print('Aces are always low. A royal flush is therefore Nine to King.')
            pause(8)
            print('The full list of hand scores and actions is as follows:')
            pause(2)
            for i in range(len(rules)):
                print('Playing ' + rules[i]['description'] + ' earns you ' + str(rules[i]['hp']) + ' points and you ' + rules[i]['action'] + ' card(s)')
                pause(1)
            pause(10)
            print(' ')
            print('The whole game will make more sense when you start I promise.')
        
        elif menu_response == '3':
            print('Type Cheat Code:')
            cheat_code = input()
            if cheat_code.upper() == 'GORDON':
                pause(1)
                print('Free Play Mode Unlocked')
                pause(1)
            elif cheat_code.upper() == 'CLEARING HOUSE':
                skip = 'yes'
                print('Skip the first two rounds!')
                menu_exit = 'yes'
            elif cheat_code.upper() == 'BOLT':
                interval = 0.05
                print('Fast mode enabled, duels will now be much faster')
            else:
                pause(1)
                print('Code not recognised')
                pause(2)
        
        elif menu_response == '4' and cheat_code.upper() == 'GORDON':
            pause(1)
            
            for i in range(40):
                pause(0.05)
                print(' ')
            
            print(' _______                        ______ __                   _______           __        ')
            pause(0.05)
            print('|    ___|.----.-----.-----.    |   __ \  |.---.-.--.--.    |   |   |.-----.--|  |.-----.')
            pause(0.05)
            print('|    ___||   _|  -__|  -__|    |    __/  ||  _  |  |  |    |       ||  _  |  _  ||  -__|')
            pause(0.05)
            print('|___|    |__| |_____|_____|    |___|  |__||___._|___  |    |__|_|__||_____|_____||_____|')
            pause(0.05)
            print('                                                |_____|                                 ')
            pause(0.05)
            print(' ')
            pause(0.05)
            print(' ')
            pause(0.05)
            print(' ')
            pause(2)            
            print('In Free Play Mode you can set up your own game against the computer.')
            pause(2)
            print('Keep the number of cards you deal somewhat sensible or the game will crash.')
            pause(2)
            print('Did you know there are only 52 cards in a deck?')
            pause(3)
            print('What do you want your HP to be?')
            free_p_hp = int(input())
            pause(1)
            print('What do you want your opponent\'s HP to be?')
            free_o_hp = int(input())
            pause(1)
            print('How many cards do you want to be dealt?')
            free_p_cards = int(input())
            pause(1)
            print('How many cards do you want your opponent to be dealt?')
            free_o_cards = int(input())
            pause(1)
            print('How many communal cards should there be?')
            free_c_cards = int(input())
            pause(2)
            print('Game on:')            
            if game(free_p_hp, free_o_hp, free_p_cards, free_o_cards, free_c_cards) == 'You Win!':
                pause(4)
                print('You Win!!!')
                pause(4)
            else:
                pause(4)
                print('You Lose!!!')
                pause(4)
        
        else:
            pause(1)
            if cheat_code.upper() == 'GORDON':
                print('Please enter a number between 1 and 4')
                pause(1)
            else:
                print('Please enter a number between 1 and 3')
                pause(1)
    
    if skip == 'no':
        
        for i in range(40):
            pause(0.05)
            print(' ')
            
        
        print(' _____                       _    ____             ')
        pause(0.05)
        print('|  __ \                     | |  / __ \            ')
        pause(0.05)
        print('| |__) |___  _   _ _ __   __| | | |  | |_ __   ___ ')
        pause(0.05)    
        print('|  _  // _ \| | | | \'_ \ / _` | | |  | | \'_ \ / _ \ ')
        pause(0.05)
        print('| | \ \ (_) | |_| | | | | (_| | | |__| | | | |  __/')
        pause(0.05)
        print('|_|  \_\___/ \__,_|_| |_|\__,_|  \____/|_| |_|\___|')
        pause(0.05)
        print(' ')
        pause(0.05)
        print(' ')
        pause(2)

        
        print('      ___           ___                                    ___           ___           ___                                         ')
        pause(0.05)
        print('     /__/\         /__/\        ___           ___         /  /\         /  /\         /  /\        ___           ___         ___   ')
        pause(0.05)
        print('     \  \:\        \  \:\      /  /\         /__/\       /  /:/_       /  /::\       /  /:/_      /  /\         /  /\       /__/|  ')
        pause(0.05)
        print('      \  \:\        \  \:\    /  /:/         \  \:\     /  /:/ /\     /  /:/\:\     /  /:/ /\    /  /:/        /  /:/      |  |:|  ')
        pause(0.05)
        print('  ___  \  \:\   _____\__\:\  /__/::\          \  \:\   /  /:/ /:/_   /  /:/~/:/    /  /:/ /::\  /__/::\       /  /:/       |  |:|  ')
        pause(0.05)
        print(' /__/\  \__\:\ /__/::::::::\ \__\/\:\__   ___  \__\:\ /__/:/ /:/ /\ /__/:/ /:/___ /__/:/ /:/\:\ \__\/\:\__   /  /::\     __|__|:|  ')
        pause(0.05)
        print(' \  \:\ /  /:/ \  \:\~~\~~\/    \  \:\/\ /__/\ |  |:| \  \:\/:/ /:/ \  \:\/:::::/ \  \:\/:/~/:/    \  \:\/\ /__/:/\:\   /__/::::\  ')
        pause(0.05)
        print('  \  \:\  /:/   \  \:\  ~~~      \__\::/ \  \:\|  |:|  \  \::/ /:/   \  \::/~~~~   \  \::/ /:/      \__\::/ \__\/  \:\     ~\~~\:\ ')
        pause(0.05)
        print('   \  \:\/:/     \  \:\          /__/:/   \  \:\__|:|   \  \:\/:/     \  \:\        \__\/ /:/       /__/:/       \  \:\      \  \:\ ')
        pause(0.05)
        print('    \  \::/       \  \:\         \__\/     \__\::::/     \  \::/       \  \:\         /__/:/        \__\/         \__\/       \__\/')
        pause(0.05)
        print('     \__\/         \__\/                       ~~~~       \__\/         \__\/         \__\/                                        ')
        
        pause(0.05)
        print(' ')
        pause(0.05)
        print(' ')
        pause(4)
        print(' ')
        
        while game_1 == 'not won':
            pause(0.5)
            print('You are ready to graduate from University, Master of Science in Psychology')
            pause(2)
            print('All you need to do is study for your exams')
            pause(2)
            print('Do you study? Y/N')
            response1 = input()
            pause(1)
            if response1.upper() == 'Y':
                print('Well done, your HP goes up by 5')
                player_HP += 5    
            else:
                print('Uh oh.')
            pause(1)
            print('Good luck in your exam!')
            pause(2)
            
            print('You have ' + str(player_HP) + ' HP, your opponent has 30 HP')
            pause(3)
            if game(player_HP, 30, hand_size, 3, 5) == 'You Win!':
                game_1 = 'won'
            else:
                pause(2)
                print('looks like you didn\'t graduate, better luck next time')
                pause(4)
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                pause(4)
                print('You get the chance to re-sit your exams')
        
        pause(4)
        print('You Win!')
        pause(2)
        print('You graduated from University.')
        
    
        pause(2)
        print('Do you want to apply for a PHD?')
        pause(1)
        print('If you want to apply type \'apply\', otherwise press enter to continue')
        response1 = input()
        if response1.upper() == 'APPLY':
            print('Your application is being reviewed.')
            pause(3.5)
            print('...')
            pause(3.5)
            print('...')
            pause(3.5)
            print('They said they would get back in touch soon')
            pause(3.5)
            print('...')
            pause(3.5)
            print('It\'s a no.')
            pause(3.5)
            print('Well that was a waste of time')
        else:
            print('That seems sensible, best to get some experience under your belt')
        pause(4)
    
        for i in range(40):
            pause(0.05)
            print(' ')
        
    
        
        print(' _____                       _   _______            ')
        pause(0.05)
        print('|  __ \                     | | |__   __|           ')
        pause(0.05)
        print('| |__) |___  _   _ _ __   __| |    | |_      _____  ')
        pause(0.05)
        print('|  _  // _ \| | | | \'_ \ / _` |    | \ \ /\ / / _ \ ') 
        pause(0.05)
        print('| | \ \ (_) | |_| | | | | (_| |    | |\ V  V / (_) |')
        pause(0.05)
        print('|_|  \_\___/ \__,_|_| |_|\__,_|    |_| \_/\_/ \___/ ')
        
        pause(0.05)
        print(' ')
        pause(0.05)
        print(' ')
        pause(2)
            
        
        print(' ______    _______  _______  _______  _______  ______    _______  __   __         ')
        pause(0.05)
        print('|    _ |  |       ||       ||       ||   _   ||    _ |  |       ||  | |  |        ')
        pause(0.05)
        print('|   | ||  |    ___||  _____||    ___||  |_|  ||   | ||  |       ||  |_|  |        ')
        pause(0.05)
        print('|   |_||_ |   |___ | |_____ |   |___ |       ||   |_||_ |       ||       |        ')
        pause(0.05)
        print('|    __  ||    ___||_____  ||    ___||       ||    __  ||      _||       |        ')
        pause(0.05)
        print('|   |  | ||   |___  _____| ||   |___ |   _   ||   |  | ||     |_ |   _   |        ')
        pause(0.05)
        print('|___|  |_||_______||_______||_______||__| |__||___|  |_||_______||__| |__|        ')
        pause(0.05)
        print('     _______  _______  _______  ___   _______  _______  _______  __    _  _______ ')
        pause(0.05)
        print('    |   _   ||       ||       ||   | |       ||       ||   _   ||  |  | ||       |')
        pause(0.05)
        print('    |  |_|  ||  _____||  _____||   | |  _____||_     _||  |_|  ||   |_| ||_     _|')
        pause(0.05)
        print('    |       || |_____ | |_____ |   | | |_____   |   |  |       ||       |  |   |  ')
        pause(0.05)
        print('    |       ||_____  ||_____  ||   | |_____  |  |   |  |       ||  _    |  |   |  ')
        pause(0.05)
        print('    |   _   | _____| | _____| ||   |  _____| |  |   |  |   _   || | |   |  |   |  ')
        pause(0.05)
        print('    |__| |__||_______||_______||___| |_______|  |___|  |__| |__||_|  |__|  |___|  ')
  
        pause(0.05)
        print(' ')
        pause(0.05)
        print(' ')
        pause(4)
        print(' ')
    
        print('You become a reseach assistant.')
        pause(2)
        print('Some people don\'t know what a research assistant is.')
        pause(3)
        print('They think it must be holding books open for researchers while they reseach.')
        pause(4)
        print('Turning the pages and so on.')
        pause(2)
        print('Not me though.')
        pause(3)
        print('I know what a research assistant is. I just can\'t be bothered explaining it.')
        pause(3)
        
        while game_2 == 'not won':
            print('Do some great research assistance and you can take a step closer to getting a PHD')
            pause(3)
            
            print('You have ' + str(player_HP) + ' HP, your opponent has 40 HP')
            pause(3)
            if game(player_HP, 40, hand_size, 3, 5) == 'You Win!':
                game_2 = 'won'
            else:
                pause(2)
                print('your research assistance was lacklustre, better luck next time')
                pause(4)
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                pause(4)
                print('Do some more research assisting, better this time, to prove your prowess with psychology.')
        
        pause(4)
        print('You Win!')
        
        
        pause(2)
        print('Do you want to reapply for your PHD?')
        pause(2)
        print('If you want to apply type \'apply\', otherwise press enter to continue.')
        response1 = input()
        pause(1)
        if response1.upper() == 'APPLY':
            print('Your application is being reviewed.')
            pause(3.5)
            print('...')
            pause(3.5)
            print('...')
            pause(3.5)
            print('I\'ve got a good feeling this time.')
            pause(3.5)
            print('...')
            pause(3.5)
            print('Honestly I think this is it.')
            pause(3.5)
            print('...')
            pause(3.5)
            print('I calculate you at a 1.8% chance of being accepted this time.')
            pause(3.5)
            print('...')
            pause(3.5)
            print('...')
            pause(3.5)
            print('...')
            pause(3.5)
            print('It\'s a no')
        else:
            pause(1)
            print('Go on give it a go, you probably have enough experience by now')
            pause(2)
            print('just type \'apply\' if you want to apply')
            response1 = input()
            pause(1)
            if response1.upper() == 'APPLY':
                print('Your application is being reviewed.')
                pause(3.5)
                print('...')
                pause(3.5)
                print('...')
                pause(3.5)
                print('I\'ve got a good feeling this time.')
                pause(3.5)
                print('...')
                pause(3.5)
                print('Honestly I think this is it.')
                pause(3.5)
                print('...')
                print('I calculate you at a 0.8% chance of being accepted this time.')
                print('...')
                pause(3.5)
                print('...')
                pause(3.5)
                print('...')
                pause(3.5)
                print('...')
                pause(3.5)
                print('It\'s a no')
            else:
                print('OK, fair enough, I think you could have got it this time though.')
        
        pause(2)
        print('From now on if you want to skip the first two rounds.')
        pause(2)
        print('Enter the cheat code \'Clearing House\' in the main menu.')
        pause(4)
        print('but be warned you will skip to here with your starting HP only')
        pause(5)
        
    
    print(' ____                          _____                       _ ')
    pause(0.05)
    print('|  _ \                        |  __ \                     | |')
    pause(0.05)
    print('| |_) | ___  _ __  _   _ ___  | |__) |___  _   _ _ __   __| |')
    pause(0.05)
    print('|  _ < / _ \| \'_ \| | | / __| |  _  // _ \| | | | \'_ \ / _` |')
    pause(0.05)
    print('| |_) | (_) | | | | |_| \__ \ | | \ \ (_) | |_| | | | | (_| |')
    pause(0.05)
    print('|____/ \___/|_| |_|\__,_|___/ |_|  \_\___/ \__,_|_| |_|\__,_|')
                                                                  
    pause(0.05)
    print(' ')
    pause(0.05)
    print(' ')
    pause(2)                                                          
    

    print('oooooo     oooo           oooo                              .                                      ')
    pause(0.05)
    print(' `888.     .8\'            `888                            .o8                                     ') 
    pause(0.05)
    print('  `888.   .8\'    .ooooo.   888  oooo  oooo  ooo. .oo.   .o888oo  .oooo.   oooo d8b oooo    ooo    ') 
    pause(0.05)
    print('   `888. .8\'    d88\' `88b  888  `888  `888  `888P\"Y88b    888   `P  )88b  `888\"\"8P  `88.  .8\'')      
    pause(0.05)
    print('    `888.8\'     888   888  888   888   888   888   888    888    .oP\"888   888       `88..8\'    ')   
    pause(0.05)
    print('     `888\'      888   888  888   888   888   888   888    888 . d8(  888   888        `888\'      ')  
    pause(0.05)
    print('      `8\'       `Y8bod8P\' o888o  `V88V\"V8P\' o888o o888o   \"888\" `Y888\"\"8o d888b        .8\'')         
    pause(0.05)
    print('                                                                                   .o..P\'         ') 
    pause(0.05)
    print('                                                                                   `Y8P\'          ') 
    pause(0.05)
    print('                                                                                                   ')
    pause(0.05)
    print('                     oooooo   oooooo     oooo                    oooo                          ')
    pause(0.05)
    print('                      `888.    `888.     .8\'                     `888                         ') 
    pause(0.05)
    print('                       `888.   .8888.   .8\'    .ooooo.  oooo d8b  888  oooo                   ') 
    pause(0.05)
    print('                        `888  .8\'`888. .8\'    d88\' `88b `888\"\"8P  888 .8P\'               ')      
    pause(0.05)
    print('                         `888.8\'  `888.8\'     888   888  888      888888.                    ')  
    pause(0.05)
    print('                          `888\'    `888\'      888   888  888      888 `88b.                  ')  
    pause(0.05)
    print('                           `8\'      `8\'       `Y8bod8P\' d888b    o888o o888o                ')   
     
    pause(0.05)
    print(' ')
    pause(0.05)
    print(' ')
    pause(5)                                                              
    
    print('Welcome to the voluntary work bonus round.')
    pause(3)
    print('Just like voluntary work...')
    pause(2)
    print('...this round is for fun')
    pause(3)
    print('Volunteer an answer to the following questions in under 10 seconds.')
    pause(4)
    print('No more')
    pause(2)
    print('Than 10 seconds.')
    pause(3)
    print('Or this poorly built game will crash.')
    pause(2)
    print('Ready?')
    pause(3)
    print(' ')
    print('Q1: What\'s your favourite TV show of all time?')
    answer1 = input()
    pause(2)
    print('Q2: What is your favourite film franchise?')
    answer2 = input()
    pause(2)
    print('Q3: If you were a biscuit what kind of biscuit would you be?')
    answer3 = input()
    pause(5)
    print('Great, wasn\'t that fun? OK back to the game.')
    pause(3)
    print('I should let you know, I haven\'t used that personal information...')
    pause(2)
    print('...to hack into all your online accounts.')
    pause(5)
    print('I could.')
    pause(4)
    print('But I won\'t.')
    pause(3)
    print('You\'re welcome.')
    
    
    
    pause(4)
    print('You could reapply for your PHD but I think we both know...')
    pause(0.5)
    print('..it\'s unlikely to be accepted just now.')
    pause(1)
    print('If you really want to you can apply by typing \'apply\'. Otherwise press enter')
    response1 = input()
    if response1.upper() == 'APPLY':
        pause(5)
        print('You didn\'t get accepted, but you\'re building resiliance')
        pause(2)
        print('Your HP goes up by 5')
        player_HP += 5    
    else:
        pause(2)
        print('Yeah I wouldn\'t have either')
    pause(3)
    for i in range(4):
        pause(0.5)
        print(' ')
    
    print('I\'ll level with you.')
    pause(2)
    print('The road ahead is looking more and more difficult.')
    pause(4)
    print('If you want you can give up.')
    pause(3)    
    print('Do you want to give up on getting your PHD? Y/N')
    response1 = input()
    if response1.upper() == 'N':
        pause(2)
        print('Good for you, your determination now will give you more options in future.')
        pause(2)
        print('And for that you will get more options in the game now.')
        pause(2)
        print('You will be dealt an additional card into your hand')
        hand_size += 1
    else:
        pause(2)
        print('Come on don\'t be so down, you can\'t quit.')
        pause(2)
        print('This is a game about a journey to getting a PHD.')
        pause(2)
        print('Not quitting and getting a job at Sainsbury\'s')
        pause(2)
        print('Somehow you find the will to carry on.')
    
    pause(3)
    
    for i in range(40):
        pause(0.05)
        print(' ')
        
        
    print(' _____                       _   _______ _                   ')
    pause(0.05)
    print('|  __ \                     | | |__   __| |                  ')
    pause(0.05)
    print('| |__) |___  _   _ _ __   __| |    | |  | |__  _ __ ___  ___ ')
    pause(0.05)
    print('|  _  // _ \| | | | \'_ \ / _` |    | |  | \'_ \| \'__/ _ \/ _ \ ')
    pause(0.05)
    print('| | \ \ (_) | |_| | | | | (_| |    | |  | | | | | |  __/  __/')
    pause(0.05)
    print('|_|  \_\___/ \__,_|_| |_|\__,_|    |_|  |_| |_|_|  \___|\___|')                                                      

    pause(0.05)
    print(' ')
    pause(0.05)
    print(' ')
    pause(2)
                                                                                                       
    print('                   .,                                  ,;                                      ')
    pause(0.05)
    print('                  ,Wt               j.               f#i                                       ')
    pause(0.05)
    print('                 i#D.            .. EW,            .E#t                                        ')
    pause(0.05)
    print('                f#f             ;W, E##j          i#W,                                         ')
    pause(0.05)
    print('              .D#i             j##, E###D.       L#D.                                          ')
    pause(0.05)
    print('             :KW,             G###, E#jG#W;    :K#Wfff;                                        ')
    pause(0.05)
    print('             t#f            :E####, E#t t##f   i##WLLLLt                                       ')
    pause(0.05)
    print('              ;#G          ;W#DG##, E#t  :K#E:  .E#L                                           ')
    pause(0.05)
    print('               :KE.       j###DW##, E#KDDDD###i   f#E:                                         ')
    pause(0.05)
    print('                .DW:     G##i,,G##, E#f,t#Wi,,,    ,WW;                                        ')
    pause(0.05)
    print('                  L#,  :K#K:   L##, E#t  ;#W:       .D#;                                       ')
    pause(0.05)
    print('                   jt ;##D.    L##, DWi   ,KK:        tt                                       ')
    pause(0.05)
    print('                      ,,,      .,,                                                             ')
    pause(0.05)
    print('                                                                                               ')
    pause(0.05)
    print('                                                                                               ')
    pause(0.05)
    print('                                                                                               ')
    pause(0.05)
    print('                         .        .              .                      L.                     ') 
    pause(0.05)
    print('                        ;W       ;W t           ;W                      EW:        ,ft         ') 
    pause(0.05)
    print('             ..        f#E      f#E Ej         f#E GEEEEEEEL         .. E##;       t#E GEEEEEEEL')
    pause(0.05)
    print('            ;W,      .E#f     .E#f  E#,      .E#f  ,;;L#K;;.        ;W, E###t      t#E ,;;L#K;;.')
    pause(0.05)
    print('           j##,     iWW;     iWW;   E#t     iWW;      t#E          j##, E#fE#f     t#E    t#E   ')
    pause(0.05)
    print('          G###,    L##Lffi  L##Lffi E#t    L##Lffi    t#E         G###, E#t D#G    t#E    t#E   ')
    pause(0.05)
    print('        :E####,   tLLG##L  tLLG##L  E#t   tLLG##L     t#E       :E####, E#t  f#E.  t#E    t#E   ')
    pause(0.05)
    print('       ;W#DG##,     ,W#i     ,W#i   E#t     ,W#i      t#E      ;W#DG##, E#t   t#K: t#E    t#E   ')
    pause(0.05)
    print('      j###DW##,    j#E.     j#E.    E#t    j#E.       t#E     j###DW##, E#t    ;#W,t#E    t#E   ')
    pause(0.05)
    print('     G##i,,G##,  .D#j     .D#j      E#t  .D#j         t#E    G##i,,G##, E#t     :K#D#E    t#E   ')
    pause(0.05)
    print('   :K#K:   L##, ,WK,     ,WK,       E#t ,WK,          t#E  :K#K:   L##, E#t      .E##E    t#E   ')
    pause(0.05)
    print('  ;##D.    L##, EG.      EG.        E#t EG.            fE ;##D.    L##, ..         G#E     fE   ')
    pause(0.05)
    print('  ,,,      .,,  ,        ,          ,;. ,               : ,,,      .,,              fE      :   ')
    pause(0.05)
    print('                                                                                    ,          ')
  
    pause(0.05)
    print(' ')
    pause(0.05)
    print(' ')
    pause(4)
    print(' ')
    
    while game_3 == 'not won':
        print('You\'re now a care assistant.')
        pause(2)
        print('Do a good enough job and you\'ll be able to move a step closer to your doctorate postgrad.')
        pause(2)
            
        print('You have ' + str(player_HP) + ' HP, your opponent has 50 HP')
        pause(1)
        if game(player_HP, 50, hand_size, 3, 5) == 'You Win!':
            game_3 = 'won'
        else:
            pause(2)
            print('Looks like you didn\'t care hard enough')
            pause(4)
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            pause(4)
            print('Try and care just a little bit more.')

    pause(3)
    
    for i in range(40):
        pause(0.05)
        print(' ')
        
    print(' _____                       _   ______               ')
    pause(0.05)
    print('|  __ \                     | | |  ____|              ')
    pause(0.05)
    print('| |__) |___  _   _ _ __   __| | | |__ ___  _   _ _ __ ')
    pause(0.05)
    print('|  _  // _ \| | | | \'_ \ / _` | |  __/ _ \| | | | \'__|')
    pause(0.05)
    print('| | \ \ (_) | |_| | | | | (_| | | | | (_) | |_| | |   ')
    pause(0.05)
    print('|_|  \_\___/ \__,_|_| |_|\__,_| |_|  \___/ \__,_|_|   ')
                                                           
    pause(0.05)
    print(' ')
    pause(0.05)
    print(' ')
    pause(2)
                                                           
    
    print('   _____    _________ _______________    __________________                                ')
    pause(0.05)
    print('  /  _  \  /   _____//   _____/|   |/   _____/\__    ___/  _  \   \      \__    ___/                                ')
    pause(0.05)
    print(' /  /_\  \ \_____  \ \_____  \ |   |\_____  \   |    | /  /_\  \  /   |   \|    |                                   ')
    pause(0.05)
    print('/    |    \/        \/        \|   |/        \  |    |/    |    \/    |    \    |                                   ')
    pause(0.05)
    print('\____|__  /_______  /_______  /|___/_______  /  |____|\____|__  /\____|__  /____|                                   ')
    pause(0.05)
    print('        \/        \/        \/             \/                 \/         \/                                         ')
    pause(0.05)
    print('__________  ______________.___._________   ___ ___ ________  .____    ________    ________.___  ____________________')
    pause(0.05)
    print('\______   \/   _____/\__  |   |\_   ___ \ /   |   \\______  \ |    |   \_____  \  /  _____/|   |/   _____/\__    ___/')
    pause(0.05)
    print(' |     ___/\_____  \  /   |   |/    \  \//    ~    \/   |   \|    |    /   |   \/   \  ___|   |\_____  \   |    |   ')
    pause(0.05)
    print(' |    |    /        \ \____   |\     \___\    Y    /    |    \    |___/    |    \    \_\  \   |/        \  |    |   ')
    pause(0.05)
    print(' |____|   /_______  / / ______| \______  /\___|_  /\_______  /_______ \_______  /\______  /___/_______  /  |____|   ')
    pause(0.05)
    print('                  \/  \/               \/       \/         \/        \/       \/        \/            \/            ')
    
    pause(6)
    print('Congratulations, they looked at your application again, the one they kept on file...')
    pause(2)
    print('...and they love the voluntary stuff, they\'ve fast-tracked your application.')
    pause(3.5)
    print('...')
    pause(3.5)
    print('I\'m just fucking with you, they don\'t have your application on file.')
    pause(2)
    print('I\'m afraid your application went in the other file.')
    pause(4)
    print('The bin')
    pause(2)
    
    print(' ')
    print(' ')
    
    print('Anyhoo.')
    pause(1)
    print('You\'re now an Assistant Psychologist.')
    pause(3)
    print('That\'s awesome!')
    pause(2)
    print('All you have to do now is assist, assist assist, until you can\'t assist any more.')
    pause(3)
    print('These are three speed rounds, through three jobs, and you have 1 spare life.')
    pause(4)
    print('Meaning you can only half-arse one of the three Psychology Assistant jobs without getting fired.')
    pause(3)
    
    round_1 = 'incomplete'
    round_2 = 'incomplete'
    round_3 = 'incomplete'
    lives = 1
        
    
    
    while game_4 == 'not won':
        
        if round_1 == 'incomplete' and lives >= 0:
            pause(1)
            print('Assistant Psychology Job number one.')
            pause(3)
            print('In this round you both have 20 HP and will be dealt two cards')
            if game(20, 20, 2, 2, 5) == 'You Win!':
                round_1 = 'complete'
                print('You win!')
            else:
                lives -= 1
                if lives == 0:
                    print('You get another chance, don\'t blow it!')
                else:
                    print('You\'re done, you have to start over.')
        
        pause(3)
        
        if round_1 == 'complete' and round_2 == 'incomplete' and lives >= 0:
            pause(2)
            print('Assistant Psychology Job number two.')
            pause(2)
            print('In this round you both have 50 HP, you both get 3 cards, and straights and flushes are worth 45 HP')
            play_straight['hp'] = 45
            play_flush['hp'] = 45
            pause(5)
            
            if game(50, 50, 3, 3, 5) == 'You Win!':
                round_2 = 'complete'
                print('You win!')
            else:
                lives -= 1
                if lives == 0:
                    print('You get another chance, don\'t blow it!')
                    pause(2)
                else:
                    print('You\'re done, you have to start over.')
                    pause(2)
        play_straight['hp'] = 10
        play_flush['hp'] = 15
        
        pause(3)
    
        if round_2 == 'complete' and round_3 == 'incomplete' and lives >= 0:
            pause(2)
            print('Assistant Psychology Job number three.')
            pause(2)
            print('In this round you each get 6 cards, there are 2 communal cards and you have 50 HP each.')
            pause(5)
            if game(player_HP, 50, 6, 6, 2) == 'You Win!':
                round_3 = 'complete'
                game_4 = 'won'        
                print('You Win!')
            else:
                lives -= 1
                if lives == 0:
                    print('You get another chance, don\'t blow it!')
                    pause(2)
                else:
                    print('You\'re done, you have to start over.')
                    pause(2)
    pause(4)
    
    if lives == 1:
        player_HP += 10
        pause(2)
        print('Well done you completed three in a row without losing a life.')
        pause(3)
        print('Your HP goes up by 10')
        pause(3)
        print('And I\'ll let you in on a secret.')
        pause(3)
        print('Type \'Bolt\' in as a cheat code in the main menu to enable Fast Mode.')
        pause(4)
    
    
    print('Wow you\'ve been working as an Assistant Psychologist for a long time now.')
    pause(2)
    print('They say you\'re one of the best there\'s ever been.')
    pause(3)
    print('Maybe it\'s time you reapply for the PHD you\'re working towards.')
    pause(3)
    print('Type \'apply\' to re-apply for your PHD again, and hopefully your application won\'t find the bin this time.')
    response1 = 'not apply'
    while response1.upper() != 'APPLY':
        response1 = input()
        if response1.upper() != 'APPLY':
            pause(1)
            print('I don\'t think you heard me. Type \'apply\'')
    
    pause(2)
    print('OK your application has ben submitted.')
    pause(3.5)
    print('...')
    pause(3.5)
    print('...')
    pause(3.5)
    print('...')
    pause(3.5)
    print('...')
    pause(3.5)
    print('You\'re in! Well done!')
    pause(3)
    print('Your hard work has paid off.')
    pause(3)
    print('now it\'s time to sit back, relax and...')
    pause(1)
    print('...')
    pause(3)
    print('Hang on. It says here this is when the hard work STARTS.')
    pause(3)
    print('Christ.')
    pause(2)
    print('Oh well, time to get to work I guess.')
    
    pause(3)
    
    for i in range(40):
        pause(0.05)
        print(' ')
        
    
    print(' _____                       _   ______ _           ')
    print('|  __ \                     | | |  ____(_)          ')
    print('| |__) |___  _   _ _ __   __| | | |__   ___   _____ ')
    print('|  _  // _ \| | | | \'_ \ / _` | |  __| | \ \ / / _ \ ')
    print('| | \ \ (_) | |_| | | | | (_| | | |    | |\ V /  __/')
    print('|_|  \_\___/ \__,_|_| |_|\__,_| |_|    |_| \_/ \___|')
                                                     
    pause(0.05)
    print(' ')
    pause(0.05)
    print(' ')
    pause(2)
                                                           
    print('    ███        ▄█    █▄       ▄████████                                                                    ')
    pause(0.05)
    print('▀█████████▄   ███    ███     ███    ███                                                                    ')
    pause(0.05)
    print('   ▀███▀▀██   ███    ███     ███    █▀                                                                     ')
    pause(0.05)
    print('    ███   ▀  ▄███▄▄▄▄███▄▄  ▄███▄▄▄                                                                        ')
    pause(0.05)
    print('    ███     ▀▀███▀▀▀▀███▀  ▀▀███▀▀▀                                                                        ')
    pause(0.05)
    print('    ███       ███    ███     ███    █▄                                                                     ')
    pause(0.05)
    print('    ███       ███    ███     ███    ███                                                                    ')
    pause(0.05)
    print('   ▄████▀     ███    █▀      ██████████                                                                    ')
    pause(0.05)
    print(' ')                                                                                                          
    pause(0.05)
    print('████████▄   ▄██████▄   ▄████████     ███      ▄██████▄     ▄████████    ▄████████     ███        ▄████████ ')
    pause(0.05)
    print('███   ▀███ ███    ███ ███    ███ ▀█████████▄ ███    ███   ███    ███   ███    ███ ▀█████████▄   ███    ███ ')
    pause(0.05)
    print('███    ███ ███    ███ ███    █▀     ▀███▀▀██ ███    ███   ███    ███   ███    ███    ▀███▀▀██   ███    █▀  ')
    pause(0.05)
    print('███    ███ ███    ███ ███            ███   ▀ ███    ███  ▄███▄▄▄▄██▀   ███    ███     ███   ▀  ▄███▄▄▄     ')
    pause(0.05)
    print('███    ███ ███    ███ ███            ███     ███    ███ ▀▀███▀▀▀▀▀   ▀███████████     ███     ▀▀███▀▀▀     ')
    pause(0.05)
    print('███    ███ ███    ███ ███    █▄      ███     ███    ███ ▀███████████   ███    ███     ███       ███    █▄  ')
    pause(0.05)
    print('███   ▄███ ███    ███ ███    ███     ███     ███    ███   ███    ███   ███    ███     ███       ███    ███ ')
    pause(0.05)
    print('████████▀   ▀██████▀  ████████▀     ▄████▀    ▀██████▀    ███    ███   ███    █▀     ▄████▀     ██████████ ')
    pause(0.05)
    print('                                                          ███    ███                                       ')
        
    pause(5)
    print('OK, this is it: coursework, research, placements and your thesis.')
    pause(4)
    print('Complete this and you will get your PHD.')
    pause(3)
    print('It wont\'t be easy, the opponent is a bit tougher, and a bit smarter')
    
    pause(3)
            
    print('You have ' + str(player_HP) + ' HP, your opponent has 65 HP')
    pause(1)
    while game_5 != 'won':
        if game(player_HP, 65, hand_size, 3, 5) == 'You Win!':
            game_5 = 'won'
        else:
            pause(3)
            consequence = random.randint(1, 3)
            if consequence == 1:
                print('You fell asleep during most of your classes, you\'ll need to restart')
            elif consequence == 2:
                print('You got lost on your way to your placement, start again.')
            elif consequence == 3:
                print('You researched entirely the wrong subject, start over.')
            pause(4)
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            pause(4)
            print('Doctorate courses aren\'t easy, keep going!')
    
    pause(5)
    
    print('Holy shit you made it to the end of your doctorate course!')
    pause(2)
    print('It\'s party time!')
    pause(1)
    
    for i in range(9):
        pause(0.04)
        print(' ')
    
    print(' .----------------. ')
    pause(0.04)
    print('| .--------------. |')
    pause(0.04)
    print('| |   ______     | |')
    pause(0.04)
    print('| |  |_   __ \   | |')
    pause(0.04)
    print('| |    | |__) |  | |')
    pause(0.04)
    print('| |    |  ___/   | |')
    pause(0.04)
    print('| |   _| |_      | |')
    pause(0.04)
    print('| |  |_____|     | |')
    pause(0.04)
    print('| |              | |')
    pause(0.04)
    print('| \'--------------\' |')
    pause(0.04)
    print(' \'----------------\' ')
    pause(0.04)
    print(' .----------------. ')
    pause(0.04)
    print('| .--------------. |')
    pause(0.04)
    print('| |      __      | |')
    pause(0.04)
    print('| |     /  \     | |')
    pause(0.04)
    print('| |    / /\ \    | |')
    pause(0.04)
    print('| |   / ____ \   | |')
    pause(0.04)
    print('| | _/ /    \ \_ | |')
    pause(0.04)
    print('| ||____|  |____|| |')
    pause(0.04)
    print('| |              | |')
    pause(0.04)
    print('| \'--------------\' |')
    pause(0.04)
    print(' \'----------------\' ')
    pause(0.04)
    print(' .----------------. ')
    pause(0.04)
    print('| .--------------. |')
    pause(0.04)
    print('| |  _______     | |')
    pause(0.04)
    print('| | |_   __ \    | |')
    pause(0.04)
    print('| |   | |__) |   | |')
    pause(0.04)
    print('| |   |  __ /    | |')
    pause(0.04)
    print('| |  _| |  \ \_  | |')
    pause(0.04)
    print('| | |____| |___| | |')
    pause(0.04)
    print('| |              | |')
    pause(0.04)
    print('| \'--------------\' |')
    pause(0.04)
    print(' \'----------------\' ')
    pause(0.04)
    print(' .----------------. ')
    pause(0.04)
    print('| .--------------. |')
    pause(0.04)
    print('| |  _________   | |')
    pause(0.04)
    print('| | |  _   _  |  | |')
    pause(0.04)
    print('| | |_/ | | \_|  | |')
    pause(0.04)
    print('| |     | |      | |')
    pause(0.04)
    print('| |    _| |_     | |')
    pause(0.04)
    print('| |   |_____|    | |')
    pause(0.04)
    print('| |              | |')
    pause(0.04)
    print('| \'--------------\' |')
    pause(0.04)
    print(' \'----------------\' ')
    pause(0.04)
    print(' .----------------. ')
    pause(0.04)
    print('| .--------------. |')
    pause(0.04)
    print('| |  ____  ____  | |')
    pause(0.04)
    print('| | |_  _||_  _| | |')
    pause(0.04)
    print('| |   \ \  / /   | |')
    pause(0.04)
    print('| |    \ \/ /    | |')
    pause(0.04)
    print('| |    _|  |_    | |')
    pause(0.04)
    print('| |   |______|   | |')
    pause(0.04)
    print('| |              | |')
    pause(0.04)
    print('| \'--------------\' |')
    pause(0.04)
    print(' \'----------------\' ')
    
    for i in range(9):
        pause(0.02)
        print(' ')    
    
    print(' .----------------. ')
    pause(0.04)
    print('| .--------------. |')
    pause(0.04)
    print('| |  _________   | |')
    pause(0.04)
    print('| | |  _   _  |  | |')
    pause(0.04)
    print('| | |_/ | | \_|  | |')
    pause(0.04)
    print('| |     | |      | |')
    pause(0.04)
    print('| |    _| |_     | |')
    pause(0.04)
    print('| |   |_____|    | |')
    pause(0.04)
    print('| |              | |')
    pause(0.04)
    print('| \'--------------\' |')
    pause(0.04)
    print(' \'----------------\' ')
    pause(0.04)
    print(' .----------------. ')
    pause(0.04)
    print('| .--------------. |')
    pause(0.04)
    print('| |     _____    | |')
    pause(0.04)
    print('| |    |_   _|   | |')
    pause(0.04)
    print('| |      | |     | |')
    pause(0.04)
    print('| |      | |     | |')
    pause(0.04)
    print('| |     _| |_    | |')
    pause(0.04)
    print('| |    |_____|   | |')
    pause(0.04)
    print('| |              | |')
    pause(0.04)
    print('| \'--------------\' |')
    pause(0.04)
    print(' \'----------------\' ')
    pause(0.04)
    print(' .----------------. ')
    pause(0.04)
    print('| .--------------. |')
    pause(0.04)
    print('| | ____    ____ | |')
    pause(0.04)
    print('| ||_   \  /   _|| |')
    pause(0.04)
    print('| |  |   \/   |  | |')
    pause(0.04)
    print('| |  | |\  /| |  | |')
    pause(0.04)
    print('| | _| |_\/_| |_ | |')
    pause(0.04)
    print('| ||_____||_____|| |')
    pause(0.04)
    print('| |              | |')
    pause(0.04)
    print('| \'--------------\' |')
    pause(0.04)
    print(' \'----------------\' ')
    pause(0.04)
    print(' .----------------. ')
    pause(0.04)
    print('| .--------------. |')
    pause(0.04)
    print('| |  _________   | |')
    pause(0.04)
    print('| | |_   ___  |  | |')
    pause(0.04)
    print('| |   | |_  \_|  | |')
    pause(0.04)
    print('| |   |  _|  _   | |')
    pause(0.04)
    print('| |  _| |___/ |  | |')
    pause(0.04)
    print('| | |_________|  | |')
    pause(0.04)
    print('| |              | |')
    pause(0.04)
    print('| \'--------------\' |')
    pause(0.04)
    print(' \'----------------\' ')




    
    
    pause(2)
    print('Wait.')
    pause(2)
    print('You got to the end of your course but your thesis isn\'t done yet.')
    pause(4)
    print('Party time canceled.')
    pause(4)
    
    for i in range(10):
        pause(0.05)
        print(' ')
    
    print(' .----------------. ')
    pause(0.02)
    print('| .--------------. |')
    pause(0.02)
    print('| |   ______     | |')
    pause(0.02)
    print('| |  |_   __ \   | |')
    pause(0.02)
    print('| |    | |__) |  | |')
    pause(0.02)
    print('| |    |  ___/   | |')
    pause(0.02)
    print('| |   _| |_      | |')
    pause(0.02)
    print('| |  |_____|     | |')
    pause(0.02)
    print('| |              | |')
    pause(0.02)
    print('| \'--------------\' |')
    pause(0.02)
    print(' \'----------------\' ')
    pause(0.02)
    print(' .----------------. ')
    pause(0.02)
    print('| .--------------. |')
    pause(0.02)
    print('| |      __      | |')
    pause(0.02)
    print('| |     /  \     | |')
    pause(0.02)
    print('| |    / /\ \    | |')
    pause(0.02)
    print('| |   / ____ \   | |')
    pause(0.02)
    print('| | _/ /    \ \_ | |')
    pause(0.02)
    print('| ||____|  |____|| |')
    pause(0.02)
    print('| |              | |')
    pause(0.02)
    print('| \'--------------\' |')
    pause(0.02)
    print(' \'----------------\' ')
    pause(0.02)
    print(' .----------------. ')
    pause(0.02)
    print('| .--------------. |')
    pause(0.02)
    print('| |  _______     | |')
    pause(0.02)
    print('| | |_   __ \    | |')
    pause(0.02)
    print('| |   | |__) |   | |')
    pause(0.02)
    print('| |   |  __ /    | |')
    pause(0.02)
    print('| |  _| |  \ \_  | |')
    pause(0.02)
    print('| | |____| |___| | |')
    pause(0.02)
    print('| |              | |')
    pause(0.02)
    print('| \'--------------\' |')
    pause(0.02)
    print(' \'----------------\' ')
    pause(0.02)
    print(' .----------------. ')
    pause(0.02)
    print('| .--------------. |')
    pause(0.02)
    print('| |  _________   | |')
    pause(0.02)
    print('| | |  _   _  |  | |')
    pause(0.02)
    print('| | |_/ | | \_|  | |')
    pause(0.02)
    print('| |     | |      | |')
    pause(0.02)
    print('| |    _| |_     | |')
    pause(0.02)
    print('| |   |_____|    | |')
    pause(0.02)
    print('| |              | |')
    pause(0.02)
    print('| \'--------------\' |')
    pause(0.02)
    print(' \'----------------\' ')
    pause(0.02)
    print(' .----------------. ')
    pause(0.02)
    print('| .--------------. |')
    pause(0.02)
    print('| |  ____  ____  | |')
    pause(0.02)
    print('| | |_  _||_  _| | |')
    pause(0.02)
    print('| |   \ \  / /   | |')
    pause(0.02)
    print('| |    \ \/ /    | |')
    pause(0.02)
    print('| |    _|  |_    | |')
    pause(0.02)
    print('| |   |______|   | |')
    pause(0.02)
    print('| |              | |')
    pause(0.02)
    print('| \'--------------\' |')
    pause(0.02)
    print(' \'----------------\' ')
    
    for i in range(9):
        pause(0.02)
        print(' ')
    
    print(' .----------------. ')
    pause(0.02)
    print('| .--------------. |')
    pause(0.02)
    print('| |  _________   | |')
    pause(0.02)
    print('| | |  _   _  |  | |')
    pause(0.02)
    print('| | |_/ | | \_|  | |')
    pause(0.02)
    print('| |     | |      | |')
    pause(0.02)
    print('| |    _| |_     | |')
    pause(0.02)
    print('| |   |_____|    | |')
    pause(0.02)
    print('| |              | |')
    pause(0.02)
    print('| \'--------------\' |')
    pause(0.02)
    print(' \'----------------\' ')
    pause(0.02)
    print(' .----------------. ')
    pause(0.02)
    print('| .--------------. |')
    pause(0.02)
    print('| |     _____    | |')
    pause(0.02)
    print('| |    |_   _|   | |')
    pause(0.02)
    print('| |      | |     | |')
    pause(0.02)
    print('| |      | |     | |')
    pause(0.02)
    print('| |     _| |_    | |')
    pause(0.02)
    print('| |    |_____|   | |')
    pause(0.02)
    print('| |              | |')
    pause(0.02)
    print('| \'--------------\' |')
    pause(0.02)
    print(' \'----------------\' ')
    pause(0.02)
    print(' .----------------. ')
    pause(0.02)
    print('| .--------------. |')
    pause(0.02)
    print('| | ____    ____ | |')
    pause(0.02)
    print('| ||_   \  /   _|| |')
    pause(0.02)
    print('| |  |   \/   |  | |')
    pause(0.02)
    print('| |  | |\  /| |  | |')
    pause(0.02)
    print('| | _| |_\/_| |_ | |')
    pause(0.02)
    print('| ||_____||_____|| |')
    pause(0.02)
    print('| |              | |')
    pause(0.02)
    print('| \'--------------\' |')
    pause(0.02)
    print(' \'----------------\' ')
    pause(0.02)
    print(' .----------------. ')
    pause(0.02)
    print('| .--------------. |')
    pause(0.02)
    print('| |  _________   | |')
    pause(0.02)
    print('| | |_   ___  |  | |')
    pause(0.02)
    print('| |   | |_  \_|  | |')
    pause(0.02)
    print('| |   |  _|  _   | |')
    pause(0.02)
    print('| |  _| |___/ |  | |')
    pause(0.02)
    print('| | |_________|  | |')
    pause(0.02)
    print('| |              | |')
    pause(0.02)
    print('| \'--------------\' |')
    pause(0.02)
    print(' \'----------------\' ')
    
    for i in range(9):
        pause(0.02)
        print(' ')
    
    print(' .----------------. ')
    pause(0.02)
    print('| .--------------. |')
    pause(0.02)
    print('| |     ______   | |')
    pause(0.02)
    print('| |   .\' ___  |  | |')
    pause(0.02)
    print('| |  / .\'   \_|  | |')
    pause(0.02)
    print('| |  | |         | |')
    pause(0.02)
    print('| |  \ `.___.\'\  | |')
    pause(0.02)
    print('| |   `._____.\'  | |')
    pause(0.02)
    print('| |              | |')
    pause(0.02)
    print('| \'--------------\' |')
    pause(0.02)
    print(' \'----------------\' ')
    pause(0.02)
    print(' .----------------. ')
    pause(0.02)
    print('| .--------------. |')
    pause(0.02)
    print('| |      __      | |')
    pause(0.02)
    print('| |     /  \     | |')
    pause(0.02)
    print('| |    / /\ \    | |')
    pause(0.02)
    print('| |   / ____ \   | |')
    pause(0.02)
    print('| | _/ /    \ \_ | |')
    pause(0.02)
    print('| ||____|  |____|| |')
    pause(0.02)
    print('| |              | |')
    pause(0.02)
    print('| \'--------------\' |')
    pause(0.02)
    print(' \'----------------\' ')
    pause(0.02)
    print(' .-----------------.')
    pause(0.02)
    print('| .--------------. |')
    pause(0.02)
    print('| | ____  _____  | |')
    pause(0.02)
    print('| ||_   \|_   _| | |')
    pause(0.02)
    print('| |  |   \ | |   | |')
    pause(0.02)
    print('| |  | |\ \| |   | |')
    pause(0.02)
    print('| | _| |_\   |_  | |')
    pause(0.02)
    print('| ||_____|\____| | |')
    pause(0.02)
    print('| |              | |')
    pause(0.02)
    print('| \'--------------\' |')
    pause(0.02)
    print(' \'----------------\' ')
    pause(0.02)
    print(' .----------------. ')
    pause(0.02)
    print('| .--------------. |')
    pause(0.02)
    print('| |     ______   | |')
    pause(0.02)
    print('| |   .\' ___  |  | |')
    pause(0.02)
    print('| |  / .\'   \_|  | |')
    pause(0.02)
    print('| |  | |         | |')
    pause(0.02)
    print('| |  \ `.___.\'\  | |')
    pause(0.02)
    print('| |   `._____.\'  | |')
    pause(0.02)
    print('| |              | |')
    pause(0.02)
    print('| \'--------------\' |')
    pause(0.02)
    print(' \'----------------\' ')
    pause(0.02)
    print(' .----------------. ')
    pause(0.02)
    print('| .--------------. |')
    pause(0.02)
    print('| |  _________   | |')
    pause(0.02)
    print('| | |_   ___  |  | |')
    pause(0.02)
    print('| |   | |_  \_|  | |')
    pause(0.02)
    print('| |   |  _|  _   | |')
    pause(0.02)
    print('| |  _| |___/ |  | |')
    pause(0.02)
    print('| | |_________|  | |')
    pause(0.02)
    print('| |              | |')
    pause(0.02)
    print('| \'--------------\' |')
    pause(0.02)
    print(' \'----------------\' ')
    pause(0.02)
    print(' .----------------. ')
    pause(0.02)
    print('| .--------------. |')
    pause(0.02)
    print('| |   _____      | |')
    pause(0.02)
    print('| |  |_   _|     | |')
    pause(0.02)
    print('| |    | |       | |')
    pause(0.02)
    print('| |    | |   _   | |')
    pause(0.02)
    print('| |   _| |__/ |  | |')
    pause(0.02)
    print('| |  |________|  | |')
    pause(0.02)
    print('| |              | |')
    pause(0.02)
    print('| \'--------------\' |')
    pause(0.02)
    print(' \'----------------\' ')
    pause(0.02)
    print(' .----------------. ')
    pause(0.02)
    print('| .--------------. |')
    pause(0.02)
    print('| |   _____      | |')
    pause(0.02)
    print('| |  |_   _|     | |')
    pause(0.02)
    print('| |    | |       | |')
    pause(0.02)
    print('| |    | |   _   | |')
    pause(0.02)
    print('| |   _| |__/ |  | |')
    pause(0.02)
    print('| |  |________|  | |')
    pause(0.02)
    print('| |              | |')
    pause(0.02)
    print('| \'--------------\' |')
    pause(0.02)
    print(' \'----------------\' ')
    pause(0.02)
    print(' .----------------. ')
    pause(0.02)
    print('| .--------------. |')
    pause(0.02)
    print('| |  _________   | |')
    pause(0.02)
    print('| | |_   ___  |  | |')
    pause(0.02)
    print('| |   | |_  \_|  | |')
    pause(0.02)
    print('| |   |  _|  _   | |')
    pause(0.02)
    print('| |  _| |___/ |  | |')
    pause(0.02)
    print('| | |_________|  | |')
    pause(0.02)
    print('| |              | |')
    pause(0.02)
    print('| \'--------------\' |')
    pause(0.02)
    print(' \'----------------\' ')
    pause(0.02)
    print(' .----------------. ')
    pause(0.02)
    print('| .--------------. |')
    pause(0.02)
    print('| |  ________    | |')
    pause(0.02)
    print('| | |_   ___ `.  | |')
    pause(0.02)
    print('| |   | |   `. \ | |')
    pause(0.02)
    print('| |   | |    | | | |')
    pause(0.02)
    print('| |  _| |___.\' / | |')
    pause(0.02)
    print('| | |________.\'  | |')
    pause(0.02)
    print('| |              | |')
    pause(0.02)
    print('| \'--------------\' |')
    pause(0.02)
    print(' \'----------------\' ')


    
    pause(4)
    print('Well this sucks.')
    pause(2)
    print('This is the hardest thing you\'ve ever had to do.')
    pause(2)
    print('And it\'s not as if everything else is rosy in the world.')
    pause(2)
    print('The last ever episode of ' + answer1 + ' was a dissappointment.')
    pause(4)
    print('They handed the ' + answer2 + ' franchise over to a bunch of clowns who don\'t know what they\'re doing')
    pause(5)
    print('And worst of all ' + answer3 + 's have suffered from shrinkflation.')
    pause(5)
    print('I understand if you want to give up.')
    pause(5)
    print('Not many would have the resolve to dust themselves off and see this through.')
    pause(5)
    print('No one will blame you, it\'s OK to admit that it\'s too much.')
    pause(5)
    print('Just type \'quit\' and you don\'t need to do your thesis.')
    response1 = input()
    if response1.upper() == 'QUIT':
        print(' ')
        pause(3)
        print('███╗   ██╗ ██████╗ ██╗██╗')
        pause(0.05)
        print('████╗  ██║██╔═══██╗██║██║')
        pause(0.05)
        print('██║╚██╗██║██║   ██║╚═╝╚═╝')
        pause(0.05)
        print('██║ ╚████║╚██████╔╝██╗██╗')
        pause(0.05)
        print('╚═╝  ╚═══╝ ╚═════╝ ╚═╝╚═╝')
        pause(3)
        print(' ')
        print('You don\'t quit, you don\'t know the meaning of the word quit.')
        pause(3)
        print('I\'m going to assume your finger slipped')
    
    pause(3)
    print('Of course you don\'t quit!')
    pause(1)
    player_HP = player_HP * 3
    print('Your resiliance is rewarded, your HP is multiplied by 3')
    pause(1)
    print('Your HP is now ' + str(player_HP))
    
    pause(4)
    
    print('You will now face your toughest enemy yet.')
    pause(4)
    print('The opponent is much tougher and is dealt the same number of cards as you.')
    pause(4)
    print('There\'s an extra communal card.')
    pause(4)
    print('Flushes, Straights and Full Houses are worth double.')
    pause(4)
    print('And Playing Two Pairs no longer grants you another turn.')
    print(' ')
    pause(8)
     
    play_two_pair['end_turn'] = 'yes'
    play_straight['hp'] = 20
    play_flush['hp'] = 30
    play_full_house['hp'] = 40 
          
    for i in range(40):
        pause(0.05)
        print(' ')


    print(' ______ _             _   _____                       _ ')
    pause(0.05)
    print('|  ____(_)           | | |  __ \                     | |')
    pause(0.05)
    print('| |__   _ _ __   __ _| | | |__) |___  _   _ _ __   __| |')
    pause(0.05)
    print('|  __| | | \'_ \ / _` | | |  _  // _ \| | | | \'_ \ / _` |')
    pause(0.05)
    print('| |    | | | | | (_| | | | | \ \ (_) | |_| | | | | (_| |')
    pause(0.05)
    print('|_|    |_|_| |_|\__,_|_| |_|  \_\___/ \__,_|_| |_|\__,_|')
    
    for i in range(20):
        pause(0.05)
        print(' ')
    
    pause(3)
                                                       
    for i in range(40):
        pause(0.05)
        print(' ')
    
    pause(3)
                                                                                                                                                   
    print('   /###           /  /                         ##### ##                                                          ##                                ') 
    pause(0.05)
    print('  /  ############/ #/                       ######  /##                                                           ##    #                          ') 
    pause(0.05)
    print(' /     #########   ##                      /#   /  / ##                            #                              ##   ###                         ') 
    pause(0.05)
    print(' #     /  #        ##                     /    /  /  ##                           ##                              ##    #                          ') 
    pause(0.05)
    print('  ##  /  ##        ##                         /  /   /                            ##                              ##                               ') 
    pause(0.05)
    print('     /  ###        ##  /##      /##          ## ##  /        /###      /###     ######## /###   ###  /###     ### ##  ###   ###  /###     /###     ') 
    pause(0.05)
    print('    ##   ##        ## / ###    / ###         ## ## /        / ###  /  / #### / ######## / ###  / ###/ #### / ######### ###   ###/ #### / /  ###  / ') 
    pause(0.05)
    print('    ##   ##        ##/   ###  /   ###        ## ##/        /   ###/  ##  ###/     ##   /   ###/   ##   ###/ ##   ####   ##    ##   ###/ /    ###/  ') 
    pause(0.05)
    print('    ##   ##        ##     ## ##    ###       ## ## ###    ##    ##  ####          ##  ##    ##    ##        ##    ##    ##    ##    ## ##     ##   ') 
    pause(0.05)
    print('    ##   ##        ##     ## ########        ## ##   ###  ##    ##    ###         ##  ##    ##    ##        ##    ##    ##    ##    ## ##     ##   ') 
    pause(0.05)
    print('     ##  ##        ##     ## #######         #  ##     ## ##    ##      ###       ##  ##    ##    ##        ##    ##    ##    ##    ## ##     ##   ') 
    pause(0.05)
    print('      ## #      /  ##     ## ##                 /      ## ##    ##        ###     ##  ##    ##    ##        ##    ##    ##    ##    ## ##     ##   ') 
    pause(0.05)
    print('       ###     /   ##     ## ####    /      /##/     ###  ##    /#   /###  ##     ##  ##    /#    ##        ##    /#    ##    ##    ## ##     ##   ') 
    pause(0.05)
    print('        ######/    ##     ##  ######/      /  ########     ####/ ## / #### /      ##   ####/ ##   ###        ####/      ### / ###   ### ########   ') 
    pause(0.05)
    print('          ###       ##    ##   #####      /     ####        ###   ##   ###/        ##   ###   ##   ###        ###        ##/   ###   ###  ### ###  ') 
    pause(0.05)
    print('                          /               #                                                                                                    ### ') 
    pause(0.05)
    print('                         /                 ##                                                                                            ####   ###') 
    pause(0.05)
    print('                        /                                                                                                              /######  /# ') 
    pause(0.05)
    print('                       /                                                                                                              /     ###/   ') 
    pause(0.05)
    print('                                                                                                                                                   ') 
    pause(0.05)
    print('  /###           /                                                        /##                                                                      ')
    pause(0.05)
    print(' /  ############/                                                       #/ ###                                                                     ')
    pause(0.05)
    print('/     #########                                    #                   ##   ###                                                                    ')
    pause(0.05)
    print('#     /  #     ##                                 ##                   ##                                                                          ')
    pause(0.05)
    print(' ##  /  ##     ##                                 ##                   ##                                                                          ')
    pause(0.05)
    print('    /  ###      ##    ###    ####      /###     ########       /###    ######         /###                                                         ')
    pause(0.05)
    print('   ##   ##       ##    ###     ###  / / ###  / ########       / ###  / #####         / ###  /                                                      ')
    pause(0.05)
    print('   ##   ##       ##     ###     ###/ /   ###/     ##         /   ###/  ##           /   ###/                                                       ')
    pause(0.05)
    print('   ##   ##       ##      ##      ## ##    ##      ##        ##    ##   ##          ##    ##                                                        ')
    pause(0.05)
    print('   ##   ##       ##      ##      ## ##    ##      ##        ##    ##   ##          ##    ##                                                        ')
    pause(0.05)
    print('    ##  ##       ##      ##      ## ##    ##      ##        ##    ##   ##          ##    ##                                                        ')
    pause(0.05)
    print('     ## #      / ##      ##      ## ##    ##      ##        ##    ##   ##          ##    ##                                                        ')
    pause(0.05)
    print('      ###     /  ##      /#      /  ##    /#      ##        ##    ##   ##          ##    /#                                                        ')
    pause(0.05)
    print('       ######/    ######/ ######/    ####/ ##     ##         ######    ##           ####/ ##                                                       ')
    pause(0.05)
    print('         ###       #####   #####      ###   ##     ##         ####      ##           ###   ##                                                      ')                                                                                                                                                   
    pause(0.05)
    print('                                                                                                                                                   ')  
    pause(0.05)
    print('                                                                                                                                                   ')                                                                                                                                                    
    pause(0.05)
    print('  /###           /  /                                                                                                                              ')
    pause(0.05)
    print(' /  ############/ #/                              #                                                                                                ')
    pause(0.05)
    print('/     #########   ##                             ###                                                                                               ')
    pause(0.05)
    print('#     /  #        ##                              #                                                                                                ')
    pause(0.05)
    print(' ##  /  ##        ##                                                                                                                               ')
    pause(0.05)
    print('    /  ###        ##  /##      /##       /###   ###        /###                                                                                    ')
    pause(0.05)
    print('   ##   ##        ## / ###    / ###     / #### / ###      / #### /                                                                                 ')
    pause(0.05)
    print('   ##   ##        ##/   ###  /   ###   ##  ###/   ##     ##  ###/                                                                                  ')
    pause(0.05)
    print('   ##   ##        ##     ## ##    ### ####        ##    ####                                                                                       ')
    pause(0.05)
    print('   ##   ##        ##     ## ########    ###       ##      ###                                                                                      ')
    pause(0.05)
    print('    ##  ##        ##     ## #######       ###     ##        ###                                                                                    ')
    pause(0.05)
    print('     ## #      /  ##     ## ##              ###   ##          ###                                                                                  ')
    pause(0.05)
    print('      ###     /   ##     ## ####    /  /###  ##   ##     /###  ##                                                                                  ')
    pause(0.05)
    print('       ######/    ##     ##  ######/  / #### /    ### / / #### /                                                                                   ')
    pause(0.05)
    print('         ###       ##    ##   #####      ###/      ##/     ###/                                                                                    ')
    pause(0.05)
    print('                         /                                                                                                                         ')
    pause(0.05)
    print('                        /                                                                                                                          ')
    pause(0.05)
    print('                       /                                                                                                                           ')
    pause(0.05)
    print('                      /                                                                                                                            ')
          
    pause(6)      

    print('You have ' + str(player_HP) + ' HP, your opponent has 300 HP')
    while game_6 != 'won':
        if game(player_HP, 300, hand_size, hand_size, 6) == 'You Win!':
            game_6 = 'won'
        else:
            pause(2)
            consequence = random.randint(1, 3)
            if consequence == 1:
                print('You mixed up their, there and they\'re throughout the entire Thesis, you need to start from scratch.')
            elif consequence == 2:
                print('You would have had written the thing in the wrong tense, better start over.')
            elif consequence == 3:
                print('You wrote the Thesis as a Dickensian comedy, which the examinors didn\'t appreciate, rewrite it!.')
            pause(4)
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            pause(4)
            print('Come on, dig deep, get this son of a bitch finished!!')
    
    pause(6)
    
    play_two_pair['end_turn'] = 'no'
    play_straight['hp'] = 10
    play_flush['hp'] = 15
    play_full_house['hp'] = 20 
    print(' ')
    pause(1)
    print('YOU DID IT')
    print(' ')
    pause(1)
    print(' ')
    pause(1)
    print('YOUR HARD WORK PAYED OFF')
    print(' ')
    pause(1)
    print('YOU\'RE NOW A DOCTOR')
    print(' ')
    pause(1)
    print('YOU REALLY DID IT')
    pause(3)
    
    for i in range(40):
        pause(0.05)
        print(' ')
    
    print('          ,_')
    pause(0.05)
    print('          | `""---..._____')
    pause(0.05)
    print('          \'-...______    _````"""""""\'`|')
    pause(0.05)
    print('                 \   ```` ``"---...__  |')
    pause(0.05)
    print('                 |`              |   ``!')
    pause(0.05)
    print('                 |               |     A')
    pause(0.05)
    print('                 |               /\   /#\ ')
    pause(0.05)
    print('                 /`--..______..-\'  |  ###')
    pause(0.05)
    print('                |   /  `\    /`--. |  ###')
    pause(0.05)
    print('               _|  |  .-;`-./;-.  ||  ###')
    pause(0.05)
    print('              / \  \ /\#|    |#/\/ /\ ##\'')
    pause(0.05)
    print('              |  `-\' \__/ _  \__/ |  |`#')
    pause(0.05)
    print('              \_,                 /_/')
    pause(0.05)
    print('                 `\              /')
    pause(0.05)
    print('                   \'.  \'.__.\'  .\'')
    pause(0.05)
    print('                     `-,____,-\'')
    pause(0.05)
    print('                      /"""I""\ ')
    pause(0.05)
    print('                     /`---\'--\'\ ')
    
    for i in range(40):
        print(' ')
        pause(0.05)
        
    pause(3)
        
    print('                           Design & Code')
    pause(0.5)
    print('                            Jamie Dowie')
    print(' ')
    print(' ')
    print(' ')
    pause(2)
    print('                       ASCII Text Genered through')
    pause(0.5)
    print('                          Patrick Gillespie')
    print('                             patorjk.com')
    print(' ')
    pause(0.5)      
    print('                            Joan G. Stark')
    print('https://asciiart.website/joan/www.geocities.com/SoHo/7373/index-3.html')
    print(' ')
    pause(0.5)
    print('                            Jamie Dowie')
    print('                         via asciiart.club')
    print(' ')
    pause(3)
    print(' ')
    print('ASCII fonts designed by:')
    print('DOOM by Frans P. de Vries <fpv@xymph.iaf.nl>')
    pause(0.5)
    print('Square by Chris Gill, 30-JUN-94 -- based on .sig of Jeb Hagan.')
    pause(0.5)
    print('Big by Glenn Chappell 4/93')
    pause(0.5)
    print('isometric3 by Lennert Stock <stock@fwi.uva.nl>')
    pause(0.5)
    print('Modular by \'myflix\' Apr-2006')
    pause(0.5)
    print('Roman by Nick Miners N.M.Miners@durham.ac.uk June 1994')
    pause(0.5)
    print('Def Leppard by Hanspeter Niederstrasser 2003-06-29')
    pause(0.5)
    print('Graffiti by Leigh Purdie (purdie@zeus.usq.edu.au) 5 Mar 1994')
    pause(0.5)
    print('Delta Corps Prist 1 by \'CoSMiC cHiLD\'')
    pause(0.5)
    print('Blocks by \'myflix\' June-2004')
    pause(0.5)
    print('Caligraphy by by Vinney Thai October 94, modified by Paul Burton September 96')
    pause(0.5)
    print('')
    pause(0.5)
    print('')
    pause(5)
    
    
    
    for i in range(20):
        print(' ')
        pause(0.05)
    pause(6)
    
          
          
    print('                                           ,.⌐═^"`     ]        `ⁿ═⌐,')
    pause(0.05)
    print('                                     ,⌐^`  t ,.⌐⌐⌐═r^^""""""""" ═¬,   "═,')
    pause(0.05)
    print('                                  ,^   ,⌐^`        `                ▀^.   *,')
    pause(0.05)
    print('                                ¿▀  ,^      ▌     ,      , ``````  ╛     ,  \'∞')
    pause(0.05)
    print('                              ,`  .╚   `` ` ┤ ,.⌐═▀^^""\'``"\"ⁿ^═¬.,"       \'¬   V')
    pause(0.05)
    print('                             /\'-,`   \'   ⌐^`     Γ                  "═,      ┐⌐ ╙')
    pause(0.05)
    print('                            ╛  r  \'¬.═\'Y    .,. ,  ,⌐╓    ▌             *,  ╓')
    pause(0.05)
    print('                           ╛  `    `     - ╓⌐ ▄ [        ƒ                ▐"^¬,')
    pause(0.05)
    print('                          ▐  `   /      ▌      ,▌,....,        "                ▐  ▐')
    pause(0.05)
    print('                          " ▐" ╗,       ▄.═"   ▐        ]  "═.            ▐         ▌')
    pause(0.05)
    print('                         ▐  [  ╚  `"``  [      ║        ▌       "═.      ,       ▌  ▐')
    pause(0.05)
    print('                         [  [.Ç    r    [      ▌ " ⁿ²"    ╙""\'^^\'\'   ⁿ,═` "╕     [  ▐')
    pause(0.05)
    print('                         ║.\'▐     "▌¬,  ╟      ▌             `"═.    ¿      \    ▌  ▐')
    pause(0.05)
    print('                         ▐, ▐███▄▄▄▄  ▌ "^.       ,,,             `-▄        L      ▌')
    pause(0.05)
    print('                              ██▀▄████▄      ``J       \'▐f` ▄ "∞        .       ƒ')
    pause(0.05)
    print('                        ,` `",██,,▄███B▀       ╚        ▌ █▌ `▀ ▀  ▐        ╛  ┌   █')
    pause(0.05)
    print('                       ¿      ▀▀▀▀              *       ▌ █╓▄  █ ▌.▐      ¿`  ;   ▐')
    pause(0.05)
    print('                      Æ                            ^═══^▀N █µL ▌,▌  ,   ⌐`   ¿   ,▀')
    pause(0.05)
    print('                     ╛                                   ▐█▌▀ █ █    "▄     ƒ   ╓')
    pause(0.05)
    print('                   ,                                   ,▄█▀\'▄▀,█▌ ,⌐^    """███▀')
    pause(0.05)
    print('                  ,      `▀▀█▄                       ,  ╨ ^,▄██F            ▐█')
    pause(0.05)
    print('                   ▀██████▄▄▌▐█                      ▐▄  ,██▓▓r           ╓"')
    pause(0.05)
    print('                        █     ▀█                       ▀██╣╚`    "^══─^█▀')
    pause(0.05)
    print('                        █                               ▓             ▀')
    pause(0.05)
    print('                         ████▄▄█                       ;▌            ▌')
    pause(0.05)
    print('                         ▀██▀   ▀W                    @▓r           ▐')
    pause(0.05)
    print('                          ▐█▌                      ,g╣▓▀            ▐')
    pause(0.05)
    print('                          █▀                    ,╓@█▓▓╛              r')
    pause(0.05)
    print('                          ⌐                  ,¿√M╬╢█▀                █')
    pause(0.05)
    print('                          ▀             ~╒K\'M╛╬║▌╜                   ▐')
    pause(0.05)
    print('                            ▀▀P██████▄▄y├V∩kQM"                       █')
    pause(0.05)
    print('                                     ▀▀█▓ÑtM                           █')
    pause(0.05)
    print('                                        █▌                              ▀')

    
    print(' ')  
    print(' ')    
   
    
    print(' _______ _                 _     __     __           ______           _____  _             _             ')
    pause(0.05)
    print('|__   __| |               | |    \ \   / /          |  ____|         |  __ \| |           (_)            ')
    pause(0.05)
    print('   | |  | |__   __ _ _ __ | | __  \ \_/ /__  _   _  | |__ ___  _ __  | |__) | | __ _ _   _ _ _ __   __ _ ')
    pause(0.05)
    print('   | |  | \'_ \ / _` | \'_ \| |/ /   \   / _ \| | | | |  __/ _ \| \'__| |  ___/| |/ _` | | | | | \'_ \ / _` |')
    pause(0.05)
    print('   | |  | | | | (_| | | | |   <     | | (_) | |_| | | | | (_) | |    | |    | | (_| | |_| | | | | | (_| |')
    pause(0.05)
    print('   |_|  |_| |_|\__,_|_| |_|_|\_\    |_|\___/ \__,_| |_|  \___/|_|    |_|    |_|\__,_|\__, |_|_| |_|\__, |')
    pause(0.05)
    print('                                                                                      __/ |         __/ |')
    pause(0.05)
    print('                                                                                     |___/         |___/ ')

    pause(5)
    
    for i in range(40):
        print(' ')
        pause(0.05)
        
    
    
    print('You\'ve now unlocked \'Free Play\' mode')
    pause(1)
    print('Enter cheat code \'Gordon\' to unlock Free Play mode from now on')
    cheat_code = 'Gordon'
    pause(1)
    print('to quit type \'quit\', otherwise press enter to to back to the main menu')
  
    for i in range(20):
        print(' ')
        pause(0.05)
    
    complete = input()
          