# 5.3
player_1_points = 0
alien_color = 'green'
if alien_color.lower() == 'green':
    player_1_points += 5
elif alien_color.lower() == 'yellow' or alien_color == 'red':
    player_1_points = 0
else:
    print('wrong color')
print(player_1_points)
# 5.3
player_1_points = 0
alien_color = 'green'
if alien_color.lower() == 'green':
    player_1_points += 5
elif alien_color.lower() == 'yellow':
    player_1_points += 10
elif alien_color.lower() == 'red':
    player_1_points += 15
else:
    print('wrong color')
print(player_1_points)

# 5.6
age = int(input('input age - '))
if age < 2:
    print('baby')
elif 2 <= age < 4:
    print('big baby')
elif 4 <= age < 13:
    print('child')
elif 13 <= age < 20:
    print('teenager')
elif 20 <= age < 65:
    print('adult')
elif 65 <= age:
    print('elderly')
else:
    print('wrong age')