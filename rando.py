import random

# print(random.randrange(23, 99, 4))

mylist = ['Gilbert', 'is', 'a', 'son', 'of', 'God']

random.shuffle(mylist)

print(mylist)
# print(random.random()*10)
print(random.choice(mylist))