import random
import turtle
card=[["A클로버","2클로버","3클로버","4클로버","5클로버","6클로버","7클로버","8클로버","9클로버","10클로버","J클로버","Q클로버","K클로버"],
      ["A다이아","2다이아","3다이아","4다이아","5다이아","6다이아","7다이아","8다이아","9다이아","10다이아","J다이아","Q다이아","K다이아"]]

cardm=card #gamecard
ang = -90 #cardDraw
cl=80 #cardlen
dealer=[]
for i in range(4) :
    row = random.randrange(0,len(cardm))
    col = random.randrange(0,len(cardm[0]))
    cardrm = card[row][col]
    dealer.append(cardrm)
    print(cardrm)
    del cardm[row][col]
    
print(dealer)

user1=[dealer[0],dealer[1]]
user2=[dealer[2],dealer[3]]

cn= 0 #cardnum
t= turtle.Turtle()

for y in [300,-100] :    
    for x in [-200,-100] :
        t.penup()
        t.goto(x,y)
        t.pendown()
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
            t.write(dealer[cn][0],font=(20))
        else :
            t.write(dealer[cn][0],font=(20))
        cn=cn+1
        
        
            
