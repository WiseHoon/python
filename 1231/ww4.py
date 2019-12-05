import random

card=[["A클로버","2클로버","3클로버","4클로버","5클로버","6클로버","7클로버","8클로버","9클로버","10클로버","J클로버","Q클로버","K클로버"],
      ["A다이아","2다이아","3다이아","4다이아","5다이아","6다이아","7다이아","8다이아","9다이아","10다이아","J다이아","Q다이아","K다이아"]]

cardm=card


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

user1c1=user1[0]
user1c2=user1[1]
user2c1=user2[0]
user2c2=user2[1]

user1c1[0]
user1c2[0]
user2c1[0]
user2c2[0]
