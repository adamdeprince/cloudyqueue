

from cloudyqueue.queue import Queue 


a = Queue('a')
for x in range(10):
    a.put(x)

del(a)

tries = 10

while True:
    for element in Queue('a'):
        try:
            with element as x:
                if x == 3 and tries:
                    raise TypeError()
                print x
        except TypeError:
            print "Okay, we're scared of the #3"
            print "Lets try again"
            tries -= 1
