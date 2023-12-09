'''
def locate_cards(cards,query):
    position=0
    print('cards',cards)
    print('query',query)
    while True:
        print('position',position)
        if cards[position]==query:
            return position
        position += 1
        if position == len(cards):
          return -1
        
    
print(locate_cards([1,2,4,3,6,4,8],2))
print(locate_cards([1,2,4,3,2,6,4,8],2))
print(locate_cards([1,2,4,3,6,4,8],-2))
# print(locate_cards([],-2))  #encounter error with this solution when the cards are empty
'''

def locate_cards(cards,query):
    position=0
    while position<len(cards):
        if cards[position]==query:
            return position
        position += 1
    return -1
        
print(locate_cards([1,2,4,3,6,4,8],2))
print(locate_cards([1,2,4,3,2,6,4,8],2))
print(locate_cards([1,2,4,3,6,4,8],-2))
print(locate_cards([],-2))