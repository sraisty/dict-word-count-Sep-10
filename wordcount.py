# put your code here.
def count_words(file_name):
    word_list = {}
    file = open(file_name)
    for line in file:
        line.rstrip()
        words = line.split()

        for word in words:
            word_list[word]= word_list.get(word, 0) +1

    for word, count in word_list.items():
        print(word, count)



#count_words('test.txt')
count_words('twain.txt')