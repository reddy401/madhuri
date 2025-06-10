
x=int(input('enter a total prize:'))
y=int(input('enter the discount:'))

# percentage=(y/100)*100

# print(percentage)
dis_prize=(y/100)*x
print(dis_prize)
current_value=x-dis_prize
print(current_value)
