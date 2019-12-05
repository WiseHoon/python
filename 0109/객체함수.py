class Rectangle:
    name = "d"
    def __init__(self, side=0):
        self.side = side
    def set_name(self , str) :
        Rectangle.name=str #각자의 클래스가 공유하는 네임
                           #정적변수는 모든 클래스가 공유
                            #파이썬프로그래밍이 이래서 멀티프로세스,멀티쓰레드에 좋
a = Rectangle(3)
b = Rectangle(3)

print(a.name)
b.name = "TEL"
print(b.name)
print(a.name)
