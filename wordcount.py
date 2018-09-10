# put your code here.
import sys 

#def count_words():

word_dict = {}

file_name = sys.argv[1]

file = open(file_name)
for line in file:

    words = line.split()

    for word in words:
        word = word.rstrip(",.-!?")
        word = word.lower()
        word_dict[word] = word_dict.get(word, 0) + 1


for word, count in word_dict.items():
    print(word, count)



#count_words('test.txt')
#count_words('twain.txt')