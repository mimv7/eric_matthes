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