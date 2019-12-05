import random
import turtle
id_user = input("ID를 입력하세요")
coin = int(input("시작코인은 얼마입니까?"))
t = turtle.Turtle()
t.penup()
t.goto(200,300)
t.write(id_user,font=(20))
t.penup()
t.goto(200,280)
t.write(coin,font=(20))
card=[["A클로버","2클로버","3클로버","4클로버","5클로버","6클로버","7클로버","8클로버","9클로버","10클로버","J클로버","Q클로버","K클로버"],
      ["A다이아","2다이아","3다이아","4다이아","5다이아","6다이아","7다이아","8다이아","9다이아","10다이아","J다이아","Q다이아","K다이아"]]

cardm=card #gamecard
ang = -90 #cardDraw
cl=80 #cardlen
dealer=[]
for i in range(4) :
    row = random.randrange(0,len(cardm))
    col = random.randrange(0,len(cardm[row]))
    cardrm = card[row][col]
    dealer.append(cardrm)
    print(cardrm)
    del cardm[row][col]
    
print(dealer)

user1=[dealer[0],dealer[1]]
user2=[dealer[2],dealer[3]]

cn= 0 #cardnum

for y in [300,-100] :    
    for x in [-200,-100] :
        t.penup()
        t.goto(x,y)
        t.pendown()
        t.setheading(0)
        t.forward(cl)
        t.setheading(ang*1)
        t.forward(cl*2)
        t.setheading(ang*2)
        t.forward(cl)
        t.setheading(ang*3)
        t.forward(cl*2)
        t.setheading(ang*4)
        t.penup()
        t.goto(x+70,y-20)
        if dealer[cn][0] =="1":
            t.goto(x+60,y-20)
            t.write(dealer[cn][0]+dealer[cn][1],font=(20))
            t.penup()
            t.goto( x+10 + cl/2 ,y-cl)
            t.pendown()
            if dealer[cn][2] =="다":
                   t.color("red")
                   t.pendown()
                   t.begin_fill()
                   for j in [120,-120,-60,60] :        
                       t.setheading(j)
                       t.forward(20)
                   t.end_fill()
                   t.color("black")
            else :
                t.penup()
                t.goto(x+10+cl/2,y-cl)
                t.pendown()
                t.begin_fill()
                t.circle(10)
                t.end_fill()
                t.penup()
                t.goto(x+cl/2,y+10-cl)
                t.pendown()
                t.begin_fill()
                t.circle(10)
                t.end_fill()
                t.penup()
                t.goto(x-10+cl/2,y-cl)
                t.pendown()
                t.begin_fill()
                t.circle(10)
                t.end_fill()
                t.penup()
                t.goto(x+cl/2,y+10-cl)
                t.pendown()
                t.begin_fill()
                t.goto(x+10+cl/2,y-5-cl)
                t.goto(x-10+cl/2,y-5-cl)
                t.goto(x+cl/2,y+10-cl)
                t.end_fill()
        else :
            t.write(dealer[cn][0],font=(20))
            t.penup()
            t.goto(x+10+cl//2,y-cl)
            if dealer[cn][1] =="다":
                   t.color("red")
                   t.pendown()
                   t.begin_fill()
                   for j in [120,-120,-60,60] :        
                       t.setheading(j)
                       t.forward(20)
                   t.end_fill()
                   t.color("black")
            else :
                t.penup()
                t.goto(x+10+cl/2,y-cl)
                t.pendown()
                t.begin_fill()
                t.circle(10)
                t.end_fill()
                t.penup()
                t.goto(x+cl/2,y+10-cl)
                t.pendown()
                t.begin_fill()
                t.circle(10)
                t.end_fill()
                t.penup()
                t.goto(x-10+cl/2,y-cl)
                t.pendown()
                t.begin_fill()
                t.circle(10)
                t.end_fill()
                t.penup()
                t.goto(x+cl/2,y+10-cl)
                t.pendown()
                t.begin_fill()
                t.goto(x+10+cl/2,y-5-cl)
                t.goto(x-10+cl/2,y-5-cl)
                t.goto(x+cl/2,y+10-cl)
                t.end_fill()
        cn=cn+1
        
        
            
