def add(a,b):
    return a+b;

def sub(a,b):
    return a-b;

def mult(a,b):
    return a*b;

def div(a,b):
    return a/b;

print("Simple Calculator(Made by suhail):\n1.Addition\n2.Subtraction\n3.Multipliction\n4.Division\n5.Exit")


i = int(input("select operator:"))

if i in [1, 2, 3, 4]:
     num1= int(input("Enter the First number:"))
     num2= int(input("Enter the Second number:"))

else:
    print("Invalid choice")

if i == 1:
    print(num1,"+",num2,"=",add(num1,num2))
    
elif i == 2:
    print(num1,"-",num2,"=",sub(num1,num2))

elif i == 3:
    print(num1,"*",num2,"=",mult(num1,num2))
    
elif i == 4:
    print(num1,"/",num2,"=",div(num1,num2))






   

    
    

    

