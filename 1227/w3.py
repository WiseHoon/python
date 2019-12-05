number = [1,2,4,6,8]
i =0
total = 0
while i<5 :
    total = total + number[i]
    i=i+1


print(total/5)

i=0
while i <5 :
    number[i] = (number[i] -(total/5))**2
    i=i+1


i=0
total = 0
while i<5 :
    total = total + number[i]
    i=i+1

print(total/5)
