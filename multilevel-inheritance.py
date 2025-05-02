class A:
    def sayA(self):
        print("A")

class B(A):
    def sayB(self):
        print("B")

class C(B):
    def sayC(self):
        print("C")

element1 = A()
element2 = B()
element3 = C()

element1.sayA()

element2.sayA()
element2.sayB()

element3.sayA()
element3.sayB()
element3.sayC()

#Method Resolution Order
class Superclass1:
    def info(self):
        print("Infos1")

class Superclass2:
    def info(self):
        print("Infos2")

class Subclass(Superclass2, Superclass1):
    pass

object = Subclass()
object.info()