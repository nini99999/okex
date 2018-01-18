class A:
    var="1"
    def __init__(self):
        pass
    def prins(self):
        print(self.var)

a1=A()
a2=A()
a2.var='2'
print(a1.var)
print(a2.var)
a1.prins()
a2.prins()