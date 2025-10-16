menu = ["espresso","mocha","latte","capuccino","cortado","americano"]

def find_coffee(coffee):
    if coffee[0] == 'c' :
        return coffee

# using map function:->
#  
map_coffee = map(find_coffee, menu)
print(map_coffee)

for x in map_coffee:
    print(x)

# using filter function:->

# filter_coffee = filter(find_coffee, menu)
# print(filter_coffee)

# for x in filter_coffee:
#     print(x)

        