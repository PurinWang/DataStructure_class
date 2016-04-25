from Module import *

#add(item), remove(item), search(item), isEmpty(), size(),
#append(item), index(item) , insert(pos,item), pop(), pop(pos)

mylist = UnorderedList()

print (mylist.isEmpty())
mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)
mylist.pop()
print(mylist.getdata())
print(mylist.search(93))
print(mylist.search(100))
mylist.add(100)
print(mylist.search(100))

print(mylist.size())

mylist.remove(54)
print(mylist.size())
mylist.remove(93)
print(mylist.size())
print (mylist.isEmpty())