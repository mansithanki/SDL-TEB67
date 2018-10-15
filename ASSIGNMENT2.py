#TE B 67
set1=set()
set2=set()

for i in range(1,8):
    set1.add(i);

for i in range(5,9):
    set2.add(i);

print("\n Set 1 : ")
print(set1)

print("\n Set 2 : ")
print(set2)


print ("\n Set union : ")
c = set1|set2
print (c)

print("\n Using function : ")
print(set1.union(set2))

print ("\n Set intersection : ")
d = set1 & set2

print (d)

print("\n Using function : ")
print(set1.intersection(set2))

print("\n Set difference : ")
c = set1-set2

print(c)

print("\n Using function : ")
print(set1.difference(set2))

print("\n Set symmetric difference : ")
d = set1^set2

print(d)

print("\n Checking wheteher A is subset : ")
d = set1<=set2

print(d)

print("\n Using function : ")
print(set1.issubset(set2))

print("\n Checking whether A is superset : ")
d = set1>=set2

print(d)

print("\n Using function : ")
print(set1.issuperset(set2))


