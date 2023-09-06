num=int(input("\nEnter the number:"))

def factorial(num):
 if num==0 or ==1:
   return1
 else:
   return num*factorial(num-1)

result=factorial(num)
print("the factorial of given number",num,"is",result)