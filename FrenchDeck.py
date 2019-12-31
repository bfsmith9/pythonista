import collections
Card = collections.namedtuple('Card', ['rank', 'suit'])


# NOTE: the "range" function below takes a start and a stop. 
# So, this starts at 2, and ends at 11, and the 11 is not included in the result (so this is really only 
# "going up to" 10). See my test below. 
# https://thepythonguru.com/python-builtin-functions/range/


print(list(range(2,11)))

class FrenchDeck:
    """ This is the FrenchDeck class from Fluent Python"""
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()
    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
            for rank in self.ranks]
    def __len__(self):
        return len(self._cards)
    def __getitem__(self, position):
        return self._cards[position]


# Notice the single undercore before "cards" above. That's an agreed-upon convention in Python. The underscore prefix is meant as a hint to another programmer that a variable or method starting with a single underscore is intended for internal use. This convention is defined in PEP 8. See https://dbader.org/blog/meaning-of-underscores-in-python

beer_card = Card('8', 'hearts')
print(beer_card)

deck = FrenchDeck()
print(len(deck))

# To change the behavior of len(), you need to define 
# the __len__() special method in your class. Whenever you pass 
# an object of your class to len(), your custom definition 
# of __len__() will be used to obtain the result. Let’s implement 
# len() for the order class we talked about in the beginning:
	
(help(FrenchDeck))
