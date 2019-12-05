#import turtle
#id_user = input("ID를 입력하세요")
#coin = int(input("시작코인은 얼마입니까?"))
#t = turtle.Turtle()
#t.penup()
#t.goto(200,300)
#t.write(id_user,font=(20))
#t.penup()
#t.goto(200,280)
#t.write(coin,font=(20))

cd=["클로버","다이아"]
num=["A","2","3","4","5","6","7","8","9","10","J","Q","K"]

card =[]

for i in range(len(cd)) :
    for j in range(len(card)) :
        card[i][j]=(num[j]+cd[i])
print(cd)
print(num)
print(card)
