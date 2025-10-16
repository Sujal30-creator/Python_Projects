country = "USA"
print("Country name" + country)
print(globals())
print("-----------")

def b():
    country="Germany"
    print("Country name" + country)
    print(locals())

b()
print("Country name" + country)