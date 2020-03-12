#Casandra Villagran
#3/12/2020

#Using a while loop, create a list called L that contains the numbers 0 to 10.
#On each iteration, the loop should append the current value of a counter variable to L and then increase the counter by 1.
#The while loop should stop once the counter variable is greater than 10

#for L in range(0,11):
#print(L)
    
x=0

myList = []
while x<=10:
    print(x)
    myList.append(x)
    #x=x+1
    x += 1
print(myList)
    
