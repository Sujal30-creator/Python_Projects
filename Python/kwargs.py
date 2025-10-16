def sum_of(**kwargs):
    sum = 0
    for k,v in kwargs.items():
        sum += v
    return round(sum,2)

print(sum_of( Coffee=2.99, Cake=4.55, Juice=2.99 ))