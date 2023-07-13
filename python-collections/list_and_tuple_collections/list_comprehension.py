from timeit import default_timer as timer

idades = [24,14,61,52,53]

print(idades)

# list comprehension
new_ages = [idade+1 for idade in idades]
print(new_ages)


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [(x if x != 'banana' else 'laranja') for x in fruits]

print(newlist)


list2 = [1, 2, 3, 4, 5]
[x for x in list2 if x != 3]
print(id(list2))

print(list2)
