import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
#option 1
#print(random.choice(friends))# This is one way of looping through to get random names printed.
names_to_pay = random.randint(0,5)
print(friends[names_to_pay]) # Option 2