# 4.1
pizzas = ['margarita', '"4" cheese', 'dodo']
for pizza in pizzas:
    print(f'I like {pizza.title()} pizza')
print('I love pizza')

# 4.3
for num in range(1,21):
    print(num)

# 4.4
numbers = list(range(1,101))
print(numbers)
print(min(numbers))
print(max(numbers))
print(sum(numbers))

# 4.6
numbers = list(range(1,21,2))
print(numbers)

# 4.7
numbers = list(range(3,31,3))
print(numbers)

# 4.8
cubes = []
for line in range(1,11):
    cube = line ** 3
    cubes.append(cube)
print(cubes)

# 4.9
cubes =[line ** 3 for line in range(1,11)]
print(cubes)

# 4.10
my_food = ['hamburger', 'glasses', 'chicken','beacon', 'milk' ]
print(my_food[:3])
print(my_food[1:3])
print(my_food[-3:])

# 4.11
my_pizzas = ['margarita', '"4" cheese', 'dodo']
wife_favorite_pizzas = my_pizzas[:]
wife_favorite_pizzas.append('tashir')
print('My favorite pizzas :')
for my_pizza in my_pizzas:
    print(f'\t{my_pizza}')
print('')
print('Wife favorite pizzas:')
for wife_pizza in wife_favorite_pizzas:
    print(f'\t{wife_pizza}')

# 4.13
buffet_in_adv = ('egg', 'sausage', 'cheese', 'yogurt', 'bread')
print('buffet in advert:')
for adv_menu in buffet_in_adv:
    print(adv_menu)
buffet_in_real = ('bread','water')
print('\nmenu in real life:')
for real_menu in buffet_in_real:
    print(real_menu, end='!\n')