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
        
    
print(locate_cards([8,7,4,3,2,1],2))
print(locate_cards([8,7,4,3,2,1],2))
print(locate_cards([8,7,4,3,2,1],2))
# print(locate_cards([],-2))  #encounter error with this solution when the cards are empty
'''


'''
# brute force solution
def locate_cards(cards,query):
    position=0
    while position<len(cards):
        if cards[position]==query:
            return position
        position += 1
    return -1
        

print(locate_cards([8,7,4,3,2,1],2))
print(locate_cards([8,7,4,3,2,1],1))
print(locate_cards([8,7,4,3,2,1],-2))
print(locate_cards([],-2))  
'''
'''
# applying bineary search algorithm for efficiency

def locate_cards(cards,query):
    lo,hi = 0,len(cards)-1

    while lo<=hi:
        mid = (lo+hi)//2
        mid_number = cards[mid]

        print('lo',lo,'hi',hi,'mid',mid,'mid_number',mid_number)

        if mid_number ==  query:
            return mid
        elif mid_number < query:
            hi = mid-1
        elif mid_number > query:
            lo = mid+1
        
    return -1

# print(locate_cards([199,45,76,58,35,24,12,10,8,7,4,3,2,1],2))
# print(locate_cards([8,7,4,3,2,1],1))
# print(locate_cards([8,7,4,3,2,1],-2))
# print(locate_cards([],-2))  
print(locate_cards([8,8,8,6,6,6,6,6,6,6,6,6,5,5,5,2,2,2,1,1,1,],6))  #test cases failed here as we have to get the first occurence of the queries element
'''

def test_location(cards,query,mid):
    mid_number = cards[mid]
    print('mid',mid,'mid_number',mid_number)

    if mid_number == query:
        if mid-1>0 and cards[mid-1]==query:
            return 'left'
        else:
            return 'found'
    elif mid_number<query:
        return 'left'
    else:
        return 'right'
    
def locate_cards(cards,query):
    lo, hi = 0, len(cards)-1
    while lo < hi:
        print('lo',lo,'hi',hi)
        mid = (lo+hi)//2
        result = test_location(cards,query,mid)

        if result == 'found':
            return mid
        elif result == 'left':
             hi = mid-1
        elif result == 'right':
            lo = mid+1
    return -1


print(locate_cards([8,8,8,6,6,6,6,6,6,6,6,6,5,5,5,2,2,2,1,1,1,],6))  #test cases failed here as we have to get the first occurence of the queries element