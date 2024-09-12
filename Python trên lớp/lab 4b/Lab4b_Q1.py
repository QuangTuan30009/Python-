#   1.1	Write a function and display the content.
f = open("poem.txt","r")
print(f.read())

#   1.2 count the number of lines from a text file "story.txt," which is not starting with an alphabet "T." .
f = open("story.txt","r")
count = 0
for line in f:
    line = line.rstrip()
    # Have no idea
        count += 1
print("Number of lines starting with 'T' = ",count)