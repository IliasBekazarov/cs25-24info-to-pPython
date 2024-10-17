persons = {
    "person": {
        "name": "Ilias",
        "age": 18,
        "city": "Bishkek",
        "email": "iliasbeknazarov4@gmail.com",
        "phone": "0704459561"
    },
    "person1": {
        "name": "Bilal",
        "age": 17,
        "city": "Bishkek",
        "email": "Bilal@gmail.com",
        "phone": "0704 ** ** **"
    }
}

print(persons)

if persons["person"]["age"] >= 18:
    print(f'{persons["person"]["name"]}  тебя  можно.')
else:
    print(f'{persons["person"]["name"]}  тебя  нельзя.')

if persons["person1"]["age"] >= 18:
    print(f'{persons["person1"]["name"]}  тебя можно.')
else:
    print(f'{persons["person1"]["name"]} тебя нельзя.')
