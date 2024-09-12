#   2.1 Count and display the total number of words in a text file.
def count_words():
    f = open('story.txt',"r")
    count = 0
    for line in f:
        word = line.split()
        count += len(word)
    return count
count = count_words()
print("Total words are ",count)

#   2.2 read lines and display those words less than 4 characters.
def display_words():
    f = open("poem.txt", "r")
    for line in f:
        words = line.split()
        for word in words:
            if len(word) < 4:
                print (word)
    f.close()
display_words()

