# List
#Create a list of cloud service providers that you are aware of, and print it out
cloud_providers = ["aws", "gcp", "azure", "oracle"]
print(cloud_providers)

#"""Print second element of the list ["a", "b", "c", "d", "e"] 
#Print the last element of this list #
cloud_providers = ["aws", "gpc", "azure", "oracle"]
print(cloud_providers[1])
print(cloud_providers[3])

"""Concatenate two lists ["a", "b", "c"] and ["c", "d", "e"] together, so each list element is a letter string
List methods .append() or .extend() will be useful here
"""
list1 = ["amazon", "google", "microst"]
list2 = ["aws", "gcp", "azure"]

list1.extend(list2)
print(list1)

# Tuple
"""Create a tuple of four world oceans (as strings) and print it out.
Some scientists claim that they discovered a new ocean! Try to call .append method on that tuple to add one extra element, e.g. "Antarctic". Why it won't work?
"""
oceans = ["Atlantic", "Pacific", "Indian", "Arctic"]
ocean1 = ["Southern"]

for ocean in oceans:
    print(oceans)

oceans.append(ocean1)
print(oceans)

# Dictionary
"""For the following employees dictionary add a new key:pair, where key is your region and values is a list of some names of your local colleagues
Print out a list of your local colleagues from this dictionary
"""
employees = {"US": ["Aurion", "Delores", "Kevin"]}
print(employees["US"])

# Set
"""Create two sets 1,2,3 and 3,4,5 and print them out
Create a set union of those sets 1,2,3 and 3,4,5 using .union method and print it out.
Create a new set out of this list ["a", "b", "b", "c"] using in-built set() function
"""
set_1 = {10, 20, 30}
set_2 = {3,6,9}

print(set_1)
print(set_2)

set_1.union(set_2)

print(set_1)

list = ["a", "b", "b", "c"]
my_set = set(list)

print(my_set)