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
#age = int(input('input age - '))
age = 12
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

# 5.7
fruits = ['qiwi','jerry', 'strawberry', 'melon', ' watermelon']
favorite_fruits = 'jerry'
if favorite_fruits in fruits:
    print('True')
else:
    print('False')

# 5.8
user_login = ['arnold', 'meleshinrv','shi7ik','admin','login']
for login in user_login:
    if login.lower() == 'admin':
        print('HELLO GOD OF COMPUTER')

    else:
        new_login = input('new login - ')
        print(f'Hello, {new_login}!')
        user_login.append(new_login)
        break
print(user_login)

# 5.9
user_login = []
if user_login:
    print(user_login)
else:
    new_login_user = input('input you login - ')
    user_login.append(new_login_user)

print(user_login)

# 5.10
current_users = ['arnold', 'meleshinrv', 'shi7ik', 'admin', 'login']
new_users = ['Arnold', 'Dmitry', 'SHI7IK', 'olga', 'guest']
current_users_lower = [user.lower() for user in current_users]
for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Имя '{new_user}' уже занято. Пожалуйста, выберите другое имя.")
    else:
        print(f"Имя '{new_user}' свободно. Добро пожаловать!")
