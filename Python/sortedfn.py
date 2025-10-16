coffee=['Espresso','Latte','Capuccino','Machiatto','Americano','Decaf']

def reverse(str):
    return str[::-1]

reversed_coffees = map(reverse,coffee)

for x in reversed_coffees:
    print(sorted(x))