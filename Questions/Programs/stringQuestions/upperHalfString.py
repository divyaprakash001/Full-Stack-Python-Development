import math as m

# upper the half of later string
def upperHalfString(s):
    half = m.ceil(len(s)/2)
    s = s[:half]+s[half:].upper()
    print(s)

upperHalfString('string')