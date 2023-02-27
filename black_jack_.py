class Card(object):

    RANKS=[
        'A','2','3','4','5','6','7','8','10','J','Q','K'
    ]
    
    SUITS=[
        'c','d','h','s'
    ]

    def _init_(self,rank,suit): #there is a syntax error on this line: always use double underscore for all constructors i.e, __init__ and not _init_
        self.rank=rank
        self.suit=suit

    def _str_(self): #there is a syntax error on this line: always use double underscore for all constructors
        rep=self.rank + self.suit
        return rep

class Unprintable_Card(Card):

     def _str_(self): #there is a syntax error on this line: always use double underscore for all constructors
        return'<Unprintable>'


class Positionable_Card(Card):
        
    def _init_(self,rank,suit,face_up=True): #there is a syntax error on this line: always use double underscore for all constructors
            super(Positionable_Card,self)._init_(rank,suit) #there is a syntax error on this line: always use double underscore for all constructors
            self.is_face_up=face_up

    def _str_(self): #there is a syntax error on this line: always use double underscore for all constructors
            if self.is_face_up:
                rep=super(Posionable_Card,self)._str_() #there are two syntax errors on this line
            else:
                rep='XX'

            return rep
        
    def flip(self):
            self.is_face_up= not self.is_face_up

Card1=Card('A', 'c')
card2=Unprintable_Card('A', 'd')
card3=Positionable_Card('A', 'h')

print('Print a Card object:')
print(card1) #there is a syntax error on this line: Card1 was initialized with uppercase C but called with lowercase c


print('Print an Unprinatable card object: ')
print(Card2) #there is a syntax error on this line: Card2 was initialized with lowercase c but called with uppercase C

print('Print a Positionable Card object:  ')
print(Card3) #there is a syntax error on this line: Card3 was initialized with lowercase c but called with uppercase C

print('Flipping the Positionable Card object:  ')
Card3.flip() #there is a syntax error on this line: Card3 was initialized with lowercase c but called with uppercase C

print('Printimg the Positiuinable card object: ')
print(card3)
        
    
