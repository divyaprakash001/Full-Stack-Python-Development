# first way
def reverseWords(s):
    st = s.split()[::-1]
    l=[]
    for i in st:
        l.append(i)
    print(' '.join(l))

reverseWords('ram is a good boy')

# 2nd way
def reverse_words(string):
	# split the string into a list of words
	words = string.split()

	# initialize an empty string to store the reversed words
	reversed_string = ''

	# loop through the words in reverse order and append them to the reversed string
	for i in range(len(words)-1, -1, -1):
		reversed_string =  reversed_string + words[i] + ' '

	# remove the extra space at the end of the reversed string and return it
	return reversed_string.strip()

string = "i am a good programmer"
print(reverse_words(string))
