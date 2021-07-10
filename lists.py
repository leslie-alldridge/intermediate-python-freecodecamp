# Lists, ordered, mutable, allows duplicates
mylist = ["banana", "cherry", "apple"]
print(mylist)

mylist2 = [3, True, "apple", "apple"]
print(mylist2)

item = mylist[0]
print(item)

# negative index from last item onwards
item2 = mylist[-2]
print(item2)

for i in mylist:
    print(i)

if "banana" in mylist:
    print("yes it is here")
else:
    print("no")

print(len(mylist))

mylist.append("lemon")

mylist.insert(1, "blueberry")
print(mylist)

popitem = mylist.pop()
print(popitem)
print(mylist)

mylist.remove("cherry")
print(mylist)

print(mylist2)
mylist2.reverse()
print(mylist2)

mylist2.clear()
print(mylist2)

newlist = [1, 2, 0, 7, 3]
newlist.sort()
print(newlist)
