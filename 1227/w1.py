from math import *



num1 = int(input("1정수 :"))
num2 = int(input("2정수 :"))
num3 = int(input("3정수 :"))
num4 = int(input("4정수 :"))

m= (num1 +num2+num3+num4) /4
sum =(num1-m)**2+(num2-m)**2+(num3-m)**2+(num4-m)**2
sum = sum/4
std= sqrt(sum)

print(std)
