def add(x,y):
  return x + y
def subtract(x,y):
  return x - y
def multiply(x,y):
  return x * y
def divide(x,y):
  if y==0:
    return "Cannot divide by 0"
  return x / y
#menu
print("Select operation: ")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
choice=input("Enter a choice (1 to 4)")
n1=float(input("Enter first number: ")
n2=float(input("Enter second number: ")
 if choice =='1':
   print(n1,"+",n2,"=",add(n1,n2))
 elif choice =='2':
   print(n1,"-",n2,"=",subtract(n1,n2))
 elif choice =='3':
   print(n1,"×",n2,"=",multiply(n1,n2))
 elif choice =='4':
   print(n1,"÷",n2,"=",divide(n1,n2))
 else: 
   print("Invalid! Enter choice between 1 to 4")
