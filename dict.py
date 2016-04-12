# Key-Value
import copy

d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print d['Bob']

a = (1, 1)
a = list(a)
a[0] -= 1
a = tuple(a)
print a

l = [["Bob", "John", "Micheal"], ["Bob1", "John1", "Micheal1"]]


def modify():
    tl = copy.deepcopy(l)
    tl[0][0] = "Bobby"
    print tl


modify()
print l
