class myclass :
    def __init__(self) :
        self.cnt =3
    def restart(self) :
        self.cnt = 0
    def view(self) : #restart 이전에 view 부터 실행하면?
        return self.cnt
    def increase(self):
        self.cnt = self.cnt +1

class_object1= myclass()
class_object2= myclass()

class_object1.restart()
class_object2.restart()

class_object1.increase()


a=class_object1.view()
b=class_object2.view()

print(a,b)

class_object = myclass()
tmp = class_object.view()
class_object.restart()


print(tmp)
