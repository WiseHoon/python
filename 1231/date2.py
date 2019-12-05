

date = ["월","화","수"]
date2 = ["목","금","토"]


date3 = date + date2

print(date3)
#index = date3.index("일")
#print(index)

date3.remove("목")
print(date3)
date4 = ["일"]
date5 = date4 + date2 + date
index = date5.index("일")
print(index)
print(date5)

