from Module import *

print "Q2A(Normal Queue)"
lqueue = Queue()
print "enqueue left"

for i in range(0,5):
    lqueue.enqueue(i)
    print lqueue.items

print "dequeue right"

for i in range(0,3):
    lqueue.dequeue()
    print lqueue.items


print lqueue.isEmpty()
lqueue.dequeue()
print lqueue.items
lqueue.enqueue("a")
print lqueue.items

print "\nQ2B"
rqueue = rQueue();
print "enqueue right"

for i in range(0,5):
    rqueue.enqueue(i)
    print rqueue.items

print "dequeue left"

for i in range(0,3):
    rqueue.dequeue()
    print rqueue.items


print rqueue.isEmpty()
rqueue.dequeue()
print rqueue.items
rqueue.enqueue("a")
print rqueue.items