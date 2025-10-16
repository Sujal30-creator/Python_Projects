class P:
    def __init__(self) -> None:
        self.a=12
    
class C(P):
    pass

c=C()   #Instance of child class
print(c.a)