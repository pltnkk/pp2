thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)
#2
thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)
#3
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)
#4
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)
#5
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)
#6
thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)
#7
thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)
#8
thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)
#9
thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset)
'''You can also use the pop() method to remove an item, but this method will remove a random item, so you cannot be sure what item that gets removed.

The return value of the pop() method is the removed item.'''