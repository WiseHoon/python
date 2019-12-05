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
t.penup()
t.goto(20,0)
t.pendown()
t.circle(20)
t.penup()
t.goto(0,20)
t.pendown()
t.circle(20)
t.penup()
t.goto(-20,0)
t.pendown()
t.circle(20)
t.penup()
t.goto(0,20)
t.pendown()
t.goto(20,-10)
t.goto(-20,-10)
t.goto(0,20)


