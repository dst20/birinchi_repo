# KALKULYATOR 
a = int(input("sonni kiriting: "))
b = int(input("sonni kiriting: "))
amal = input("amalni kiriting: (+,-,*,/) ")
if amal == '+' : 
   javob = a + b
   print(f"{a} + {b} = {javob}")
elif amal == '-'  :
   javob = a - b
   print(f"{a} - {b} = {javob}")
elif amal ==  '/' :
   javob = a / b
   print(f"{a} : {b} = {javob}")
elif amal == '*' :
   javob = a*b
   print(f"{a} x {b} = {javob}")
