# dictionaries
people = {
    'htanaka' : 'Haru Tanaka',
    'ppatel' : 'Pooja Patel',
    'bagarcia' : 'Benjamin Alberto Garcia',
    'zmin' : 'Zhang Min',
    'afarooqi' : 'Ayesha Farooqi',
    'hajackson' : 'Hanna Jackson',
    'papatel' : 'Pratyush Aarav Patel',
    'hrjackson' : 'Henry Jackson'
}
print(people)
print(people['ppatel'])     # particular value is printed associated to the key

person = 'zmin'
print(people[person])

print(len(people))      # length is printed

print('zmin' in people)     # checks whether the key is present in the dictionary ot not

# changing the value associated to the key
people['hajackson'] = 'Hanna Adam Jackson'
print(people)

# updating the value using update() function
people.update({'htanaka':'Harry Tanaka'})
print(people)

# printing the key of the value
for person in people:
    print(person + " " + "is the key value of " + people[person])
    
    
people1 = {
    'van' : 'vanshraj',
    'lak' : 'lakshya',
    'may' : 'mayank'
}
peoplecp = people1.copy()
print(peoplecp)
people1.update({'van':'vsg'})
print(people1)
print(peoplecp)

# deleting the key from the dictionary
del people1['van']
print(people1)

people1.pop('lak')
print(people1)

# clearup the dictionary
people1.clear()
print(people1)

# nested dictionary
people2 = {
    'man' : 'manas',
    'hit' : 'hiten',
    'nd' : peoplecp
}
print(people2)
print(people2['nd'])