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
# total counts for each word, where the order is in descending order by count

#sort first by the word in asscending order
ordered_pairs = sorted(word_dict.items())
#then resort by the count in descending order.  Assuming? that the alphabeetic 
# order for keys is preserved if the count is the same
ordered_pairs2 = sorted(ordered_pairs, 
                       key = lambda pair: pair[1], 
                       reverse = True)

#ordered_pairs = sorted(word_dict.items())

for (word, count) in ordered_pairs2:
    print(word, count)



#count_words('test.txt')
#count_words('twain.txt')