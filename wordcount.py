# put your code here.
def count_words(file_name):
    word_dict = {}

    file = open(file_name)
    for line in file:

        words = line.split()

        for word in words:
            word = word.rstrip(",.-!?")
            word_dict[word] = word_dict.get(word, 0) + 1

    for word, count in word_dict.items():
        print(word, count)



count_words('test.txt')
#count_words('twain.txt')