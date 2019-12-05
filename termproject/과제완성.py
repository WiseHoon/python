def sum_card(card) :
    sum_n=0
    for i in card :
        if i =="A" and sum_n <=10 :
            sum_n = sum_n +11
        elif i =="A" and sum_n >10 :
            sum_n = sum_n +1
        else :
            sum_n = sum_n + int(i)
        
    return sum_n


def DrawCard(cardtext,x,y):
        cl=80
        ang=-90
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
        if cardtext[0] =="1":
            t.goto(x+60,y-20)
            t.write(cardtext[0]+cardtext[1],font=(20))
            t.penup()
            t.goto( x+10 + cl/2 ,y-cl)
            t.pendown()
            if cardtext[2] =="다":
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
            if t.ycor() >0 :
                return "10" , "dealer"
            else :
                return "10" , "user"
  
        else :
            t.write(cardtext[0],font=(20))
            t.penup()
            t.goto(x+10+cl//2,y-cl)
            if cardtext[1] =="다":
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
            if t.ycor() >0 :
                if cardtext[0].isalpha():
                    if cardtext[0] =="A" :
                        return "A", "dealer"
                    else :
                        return "10" , "dealer"
                return cardtext[0], "dealer"
            else :
                if cardtext[0].isalpha():
                    if cardtext[0] =="A" :
                        return "A", "user"
                    else :
                        return "10" , "user"
                return cardtext[0], "user"
                    
import random
import turtle
class Player_Account :
    def __init__(self):
        self.Player_ID ="user"
        self.Player_Coin ="0"
    def start(self) :
        self.Player_ID = input("ID를 입력하세요")
        self.Player_Coin = int(input("시작코인은 얼마입니까?"))
    def view(self) :
        return self.Player_ID,self.Player_Coin
    def start_coin(self,coin):
        self.Player_Coin = coin - 10
        return self.Player_Coin
    def hit_coin(self,i) :
        self.Player_Coin = self.Player_Coin-20*(2**i)
        return self.Player_Coin

    
class Dealer_a(Player_Account) :
    def __init__(self):
        self.Player_Coin = 500
        self.Player_ID = "dealer"
    def hit_coin(self) :
        self.Player_Coin -=50
        return self.Player_Coin
        
Player1 =Player_Account()

Player1.start()

id_user,coin=Player1.view()

Dealer = Dealer_a()

dealer_n,D_coin = Dealer.view()

t = turtle.Turtle()
while(1 and coin >= 10 and D_coin >0):
    t.speed(10)
    print("coin=",coin)
    start_coin = coin
    Dealer_Card = []
    Player_Card = []
    t.penup()
    t.goto(200,300)
    t.write(id_user,font=(20))
    t.penup()
    t.goto(200,280)
    t.write(coin,font=(20))
    t.penup()
    t.goto(-250,300)
    t.write(dealer_n,font=(20))
    t.penup()
    t.goto(-250,280)
    t.write(D_coin,font=(20))
    
    card=[["A클로버","2클로버","3클로버","4클로버","5클로버","6클로버","7클로버","8클로버","9클로버","10클로버","J클로버","Q클로버","K클로버"],
          ["A다이아","2다이아","3다이아","4다이아","5다이아","6다이아","7다이아","8다이아","9다이아","10다이아","J다이아","Q다이아","K다이아"]]
    cardm=card #gamecard
    ang = -90 #cardDraw
    cl=80 #cardlen
    game_card=[]
    for i in range(4) :
        row = random.randrange(0,len(cardm))
        col = random.randrange(0,len(cardm[row]))
        cardrm = card[row][col]
        game_card.append(cardrm)
        del cardm[row][col]
        
    dealer=[game_card[0],game_card[1]]
    user=[game_card[2],game_card[3]]
    #[-200,300][-100,300][-200,-100][-100,-100]
    number,who=DrawCard(dealer[0],-200,300)
    if who == "dealer":
        Dealer_Card.append(number)
    else :
        Player_Card.append(number)
    number,who=DrawCard(dealer[1],-100,300)
    if who == "dealer":
        Dealer_Card.append(number)
    else :
        Player_Card.append(number)
    number,who=DrawCard(user[0],-200,-100)
    if who == "dealer":
        Dealer_Card.append(number)
    else :
        Player_Card.append(number)
    number,who=DrawCard(user[1],-100,-100)
    if who == "dealer":
        Dealer_Card.append(number)
    else :
        Player_Card.append(number)
    coin = Player1.start_coin(coin)
    print("coin = ",coin)
    DC=sorted(Dealer_Card)
    PC=sorted(Player_Card)
    sum_dealer = sum_card(DC)
    sum_player = sum_card(PC)
    print(sum_dealer , sum_player)
    i=2
    j=2
    xx1=0
    xx=0
    if coin >= 20:
        pluscard = input("카드를 한장 더 받으시겠습니까?")
    while(1) :
        print("dealer coin =",D_coin)
        if(coin>=20 and pluscard.lower() =="hit" ):
            coin = Player1.hit_coin(i-2)
            print("coin=",coin)
            row = random.randrange(0,len(cardm))
            col = random.randrange(0,len(cardm[row]))
            cardrm = card[row][col]
            game_card.append(cardrm)
            print(cardrm)
            del cardm[row][col]
            user.append(game_card[i+2])
            number,who=DrawCard(user[i],xx,-100)  
            if who == "dealer":
                Dealer_Card.append(number)
            else :
                Player_Card.append(number)
                PC=sorted(Player_Card)
                print(DC,PC)
                sum_player = sum_card(PC)
                print(sum_dealer , sum_player)
            if sum_player > 21 :
                if coin >0 :
                    print("패배")
                    break
                else :
                    print("파산")
                    break
            pluscard = input("카드를 한장 더 받으시겠습니까?")
            xx=xx+100
            i+=1
        elif (coin<20 or pluscard.lower() == "stand" ) :
            if D_coin > 0 and (sum_dealer < sum_player or sum_dealer<12  ) and sum_player < 19 and sum_dealer+sum_player < 35 :
                D_coin = Dealer.hit_coin()
                row = random.randrange(0,len(cardm))
                col = random.randrange(0,len(cardm[row]))
                cardrm = card[row][col]
                game_card.append(cardrm)
                print(cardrm)
                del cardm[row][col]
                dealer.append(game_card[i+2])
                number,who=DrawCard(dealer[j],xx1,300)  
                xx1=xx1+100
                i+=1
                j+=1
                if who == "dealer":
                    Dealer_Card.append(number)
                    DC=sorted(Dealer_Card)
                    print(DC,PC)
                    sum_dealer = sum_card(DC)
                    print(sum_dealer , sum_player)
                else :
                    Player_Card.append(number)
                    PC=sorted(Player_Card)
                    print(DC,PC)
                    sum_player = sum_card(PC)
                    print(sum_dealer , sum_player)
            else :
                if sum_dealer > sum_player :
                    if coin >0 and sum_dealer<=21:
                        print("패배")
                        break
                    elif sum_dealer >21 :
                        print("승리")
                        coin = coin+(start_coin - coin)*2
                        break
                    else :
                        print("파산")
                        break
                elif sum_player > sum_dealer or sum_dealer>21 :
                    print("승리")
                    coin = coin+(start_coin - coin)*2
                    break
                else :
                    if sum_dealer > 21 and sum_player >21 or sum_dealer ==sum_player:
                        print("무승부")
                        coin = start_coin
                        break
                    
                    elif sum_dealer >21 and sum_player <=21 :
                        print("승리")
                        coin = coin+(start_coin - coin)*2
                        break
        else:
            pluscard = input("카드를 한장 더 받으시겠습니까?")
            
            
    t.reset()
    if D_coin ==0 :
        print("게임종료")
