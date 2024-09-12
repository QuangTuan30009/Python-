#   3.1 Count uppercase characters in a text file.
def dis_chars_uppercase():
    f = open("poem.txt","r")
    uppercase_count = 0
    for line in f:
        for char in line:
            if char.isupper():
                uppercase_count += 1
    return uppercase_count
uppercase_count  = dis_chars_uppercase()
print(uppercase_count)

#   3.2 Count the words "this" and "these"
def count_word():
    f = open("article.txt", "r")
    count = 0
    for line in f:
        words = line.split()
        for word in words:
            if word.startswith("this") or word.startswith("these"):
                count +=1
        return(count)
count = count_word()
print(count)