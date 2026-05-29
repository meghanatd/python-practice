terms=int(input("How many terms? "))

#first 2 terms
n1, n2=0,1
count=0

#checking if number of terms is valid 
if terms <=0:
  print("Enter only positive integer ")
  
#if there's only one term
elif terms ==1:
  print ("Fibonacci sequence: ")
  print (n1)

else:
  print ("Fibonacci sequence: ")
  while count<terms: 
    print (n1)
    nth=n1+n2
    #updating values 
    n1=n2
    n2=nth
    count +=1
