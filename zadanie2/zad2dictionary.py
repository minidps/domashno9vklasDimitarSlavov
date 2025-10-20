dict = {
    "име": "Иван",
    "възраст": 25,
    "град": "София"
}

while dict:
    for key in list(dict.keys()):
        del dict[key]
        break

print("The dictionary is empty", dict)
