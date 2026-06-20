#Nigerian_states = ["Abia", "Adamawa", "Akwaibom", "Anambra"]
#print(Nigerian_states[-4  ])
# In python, creation of simple collection of ordered items is called list.
# e.g. fruits = ["Cherry", "Apple", "Pear"]
# list always starts with open square bracket - []

states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]
# states_of_america[0] = "Osun" #this is how we change things in a list
#states_of_america.append("osun state")# We append things using .append(). It adds an item to the end of a list.
states_of_america.extend(["osun state", "Abia", "Rivers"])# Unlike .append, we use,
# .extend to add a list of other things we want to see in our list.
length = len(states_of_america)
print(states_of_america)
