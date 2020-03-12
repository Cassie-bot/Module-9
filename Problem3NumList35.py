#Casandra Villagran
#3/12/2020


#Using a while loop, create a list numbers that contains the numbers 0 through 35.
#On each iteration, the loop should append the current value of the counter to the list and the counter should increase by 1.
#The while loop should stop when the counter is greater than 35.

x=0

myList = []
while x<=35:
    print(x)
    myList.append(x)
    #x=x+1
    x += 1
print(myList)
