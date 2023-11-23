a = int(input('Enter any number between 5 and 9 :: '))
if a < 5 or a > 9:
    raise ValueError('Value should be between 5 and 9')

user  = int(input('Enter any number between 5 and 9 :: '))
# if user enter quit as input but should not raise error