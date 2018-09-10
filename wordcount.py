# put your code here.
import sys 

#def count_words():

word_dict = {}

file_name = sys.argv[1]

file = open(file_name)
for line in file:

    words = line.split()

    # within the line, go through each word one at a time and add to dictionary
    # or update its count
    for word in words:
        word = word.rstrip(",.-!?")
        word = word.lower()
        word_dict[word] = word_dict.get(word, 0) + 1


# after we've gone through all lines in the input file, we print out the 
# total counts for each word, where the words are sorted in alphabetic order
for word, count in sorted(word_dict.items()):
    print(word, count)



#count_words('test.txt')
#count_words('twain.txt')