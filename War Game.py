#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random


# In[2]:


suits = ('Hearts','Diamonds','Spades','Clubs')
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':11,'Queen':12,'King':13,'Ace':14}


# In[3]:


class Card:
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    
    def __str__(self):
        return self.rank + ' of ' + self.suit
    


# In[20]:


class Deck:
    
    def __init__(self):
        self.allcards = []
        for suit in suits:
            for rank in ranks:
                self.allcards.append(Card(suit,rank))
    
    def shuffle(self):
        random.shuffle(self.allcards)
        
    def deal_one(self):
        return self.allcards.pop()
    


# In[21]:


class Player:
    
    def __init__(self,name):
        self.name = name
        self.allcards = []
        
    def removeone(self):
        return self.allcards.pop(0)
    
    def addcard(self,newcard):
        if type(newcard) == type([]):
            self.allcards.extend(newcard)
        else:
            self.allcards.append(newcard)
        
    def __str__(self):
        return f'player {self.name} has {len(allcards)} cards.'
    


# In[22]:


player_one = Player('one')
player_two = Player('two')


# In[23]:


new_deck = Deck()
new_deck.shuffle()


# In[24]:


for x in range(26):
    player_one.addcard(new_deck.deal_one())
    player_two.addcard(new_deck.deal_one())
    


# In[25]:


import pdb

game_on = True

round_num = 0

while game_on:
    
    round_num += 1
    print(f'round {round_num}')
    
    if len(player_one.allcards) == 0:
        print('Player one out of cards! Game over')
        print('Player two wins')
        game_on = False
        break
        
    if len(player_two.allcards) == 0:
        print('Player two out of cards! Game over')
        print('Player one wins')
        game_on = False
        break
        
        
    player_one_cards = []
    player_one_cards.append(player_one.removeone())
    
    player_two_cards = []
    player_two_cards.append(player_two.removeone())
    
    at_war = True
    
    while at_war:
        
        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.addcard(player_one_cards)
            player_one.addcard(player_two_cards)
            at_war = False
            
        elif player_one_cards[-1].value < player_two_cards[-1].value:
            player_two.addcard(player_one_cards)
            player_two.addcard(player_two_cards)
            at_war = False
            
        else:
            print('War!')
            
            if len(player_one.allcards) < 5:
                print('Player one unable to play war! Game over at war.')
                print('Player two wins! Player one loses!')
                game_on = False
                break
                
            if len(player_two.allcards) < 5:
                print('Player two unable to play war! Game over at war.')
                print('Player one wins! Player two loses!')
                game_on = False
                break
            
            else:
                for num in range(5):
                    player_one_cards.append(player_one.removeone())
                    player_two_cards.append(player_two.removeone())
            
        
        


# In[ ]:




