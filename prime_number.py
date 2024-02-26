x=int(input("enter a number: "))
for i in range (2,x):
    if(x%i==0):
        print("composite number")
        break
else:
    print("prime number")