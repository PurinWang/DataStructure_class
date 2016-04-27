from Module import *

#add(item), remove(item), search(item), isEmpty(), size(),
#append(item), index(item) , insert(pos,item), pop(), pop(pos)

mylist =  UnorderedList()

mylist.add(10)
print (mylist.isEmpty())
mylist.remove(10)
print (mylist.isEmpty())
mylist.add(35)
mylist.add(20)
mylist.add(10)
mylist.add(5)
mylist.append(59)
print(mylist.pop())
print (mylist.pop(1))
print(mylist.search(20))
print(mylist.size())
print(mylist.index(35))
print(mylist.index(59))