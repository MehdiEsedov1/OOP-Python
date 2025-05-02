class A:
    def sayA(self):
        print("A")

class B:
    def sayB(self):
        print("B")

class C(A,B):
    pass

element = C()

element.sayA()
element.sayB()