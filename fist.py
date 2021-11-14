print("Enter a number")
num1=int(input("\nEnter the first number:-"))
num2=int(input("\nEnter the second number:-"))
add_res=num1+num2
sub_res=num1-num2
mul_res=num1*num2
idiv_res=num1/num2       #Will show quotient as output
mdiv_res=num1%num2       #will show remainder as output
print('\n**********Results***************')
print(str(num1)+"+"+str(num2)+"="+str(add_res))
print(str(num1)+"-"+str(num2)+"="+str(sub_res))
print(str(num1)+"*"+str(num2)+"="+str(mul_res))
print(str(num1)+"/"+str(num2)+"="+str(idiv_res))
print(str(num1)+"%"+str(num2)+"="+str(mdiv_res))