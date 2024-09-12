# 1. Seek the Beginning of the File
f = open("text_2.txt", "r")
f.seek(0)
print(f.read())

# 2. Seeking The End of File
f.write("\nThis content is added to the end of the file")
f.close()
