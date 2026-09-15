# 6.1
im ={
    'name': 'roman',
    'soname': 'meleshin',
    'age': 41,
    'city': 'saint-petersburg',
}
for k in im:
    print(im[k])

# 6.2
favorite_num = {
    'roma':7,
    'sveta': 5,
    'mama': 8,
    'papa': 2,
    'andrey':3,
}

# 6.3
glossary ={
    "string": "Серия символов, которая обрабатывается как текст.",
    "comment": "Заметка в коде, которую интерпретатор Python полностью игнорирует.",
    "list": "Коллекция элементов, расположенных в определенном порядке.",
    "loop": "Конструкция, которая позволяет циклически выполнять блок кода.",
    "dictionary": "Коллекция пар 'ключ-значение', связывающая слова с их определениями.",
}
for i in glossary:
    print(f'{i.title()} : \n\t{glossary[i]}')

# 6.4
for k,v in glossary.items():
    print(f'{k} : {v}')

# 6.5
rivers = {
    'nile':'egypt',
    'neva':'russia',
    'mississippi':'usa',
    'oka':'russia'
}
for k,v in rivers.items():
    print(f'the {k.title()} runs through {v.title()}')
for rive in rivers.keys():
    print(rive)

for country in set(rivers.values()):
    print(f'\t{country}')

# 6.6
favorite_lang ={
    'jen':'python',
    'sarah': 'c',
    'edward':'ruby',
    'phil':'python',
}
poll_participants = ['jen', 'alex', 'phil', 'elena', 'sarah', 'dylan']
for name in poll_participants:
    if name in favorite_lang.keys():
        print(f'{name.title()}, спасибо за участие в опросе!"')
    else:
        print(f'{name.title()}, примите участие в опросе')