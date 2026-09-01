#3.1-2
names = ['andrey','slava','sasha']
print(f'Hello, {names[0].title()}!')
print(f'Hello, {names[1].title()}!')
print(f'Hello, {names[2].title()}!')

#3.3
guitars = ['cort','martin','jet','fender']
print(f'I want to buy "{guitars[0].title()}" guitars')
print(f'I want to buy "{guitars[1].title()}" guitars')
print(f'I want to buy "{guitars[2].title()}" guitars')
print(f'I want to buy "{guitars[3].title()}" guitars')

# 3.4
guest = ['mama','papa','andrey']
print(f'I invite you, {guest[0].title()}, to lunch!')
print(f'I invite you, {guest[1].title()}, to lunch!')
print(f'I invite you, {guest[2].title()}, to lunch!')

# 3.5
guest_cannot_come = guest.pop(2)
print(f'The guest {guest_cannot_come.title()} cannot come')
guest.append('sveta')
print(f'\nI invite you, {guest[2].title()}, to lunch!')

# 3.6
guest.insert(0,'tanya')
guest.insert(2,'kamila')
guest.append('ivan')
print(f'\n \tI invite you, {guest[0].title()}, to lunch!')
print(f'\tI invite you, {guest[1].title()}, to lunch!')
print(f'\tI invite you, {guest[2].title()}, to lunch!')
print(f'\tI invite you, {guest[3].title()}, to lunch!')
print(f'\tI invite you, {guest[4].title()}, to lunch!')
print(f'\tI invite you, {guest[5].title()}, to lunch!')

# 3.7
guest_cannot_come = guest.pop(0)
print(f'{guest_cannot_come.title()}- you cannot come')
guest_cannot_come = guest.pop(1)
print(f'{guest_cannot_come.title()}- you cannot come')
del guest[-1]
del guest[-1]
for i in guest:
    print(f'\n\tI invite you, {i.title()}, to lunch!')

# 3.8
country = ['usa', 'russia', 'china', 'italia', 'spanish']
print(country)
print(sorted(country))
print(country)
country.sort()
print(country)
country.reverse()
print(country)
print(len(country))