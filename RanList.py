import random

pets = ['cats', 'dogs', 'snakes']
people = ['Sara', 'Doug', 'John', 'Michelle']

print(random.choice(pets))
random.shuffle(people)
print(people)
print(pets.index('cats'))
pets.append('mouse')
print(pets)
print(pets.index('mouse'))
pets.insert(2, 'tigers')
print(pets)
# pets.remove('tigers')
pets.sort()
# print(pets)
# pets.sort(reverse=True)
pets.reverse()
print(pets)