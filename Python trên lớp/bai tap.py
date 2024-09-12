data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
trc = data.find('@')
print(trc)
sau = data.find(" ", trc)
print(sau)
giua =data[trc + 1 : sau]
print(giua)