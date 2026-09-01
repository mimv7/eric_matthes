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
