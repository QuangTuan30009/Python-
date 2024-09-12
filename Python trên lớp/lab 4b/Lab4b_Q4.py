#   4.1
def hash_display():
    f = open("matter.txt","r")
    text = f.read()
    for i in range(len(text)):
        print(text[i], end="")
        if i < len(text) - 1:
            print("#", end="")
hash_display()
#   4.2
def JTOI():
    f = open("words.txt", 'r')
    text = f.read()
    corrected_text = text.replace('J', 'I')
    print(corrected_text)

JTOI()