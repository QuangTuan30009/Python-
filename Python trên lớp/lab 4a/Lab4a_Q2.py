# 1. Write to a new file
f = open("Text.txt", "w")
f.write("This is new content\n")

# 2. Writing To An Existing File
f.write("This is new content\n")
f.write("This is overwritten content\n")

# 3. Write a list of lines to a file
f.write("Name: Emma\n")
f.write("Address: 221 Baker Street\n")
f.write("City: London")
f.close()