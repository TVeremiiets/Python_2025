from unicodedata import digit

#home_field = int(input("7498"))
#home_field2=1000
#digit=home_field
#left,right=divmod(digit,home_field2)
#print(left)

home_field=int(input(7498))
res1=home_field//1000
res2=(home_field//100)%10
res3=(home_field%100)//10
res4=home_field%10
print(res1)
print(res2)
print(res3)
print(res4)



