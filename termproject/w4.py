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
for i in [-180,-60,60,180] :
    t.penup()
    t.goto(i+20,0)
    t.pendown()
    t.begin_fill()
    t.circle(20)
    t.end_fill()
    t.penup()
    t.goto(i+0,20)
    t.pendown()
    t.begin_fill()
    t.circle(20)
    t.end_fill()
    t.penup()
    t.goto(i+ -20,0)
    t.pendown()
    t.begin_fill()
    t.circle(20)
    t.end_fill()
    t.penup()
    t.goto(i+0,20)
    t.pendown()
    t.begin_fill()
    t.goto(i+20,-10)
    t.goto(i-20,-10)
    t.goto(i+0,20)
    t.end_fill()
for i in [-180,-60,60,180] :
    t.penup()
    t.goto(i+30,-100)
    t.color("red")
    t.pendown()
    t.begin_fill()
    for j in [120,-120,-60,60] :        
        t.setheading(j)
        t.forward(60)
    t.end_fill()
        
