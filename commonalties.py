x = int(input("enter a number : "))
y = 0
for i in range(1,x+1) :
    if x % i == 0 :
        y += 1
print("the number of divisors is ", y ,"and they are : ")
for i in range(1,x+1) :
    if x % i == 0 :
        y += 1
        print (i)
