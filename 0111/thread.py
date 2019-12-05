import threading

def add1(a,b) :
    total =0
    for i in range(a,b) :
        total = total + i
        print(total)
    return total
T1=threading.Thread(target = add1,args =(10,1000))
T1.start()
#add1(10,1000)

for i in range(0,1000):
    print("hello world")
