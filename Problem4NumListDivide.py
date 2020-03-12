#Casandra Villagran
#3/12/2020

#Create a while loop that initializes a counter at 0 and will run until the counter reaches 50.
#If the value of the counter is divisible by 10, append the value to the list, tens.

x=0

myList = []

while x<=50:
    print(x)

    if x%10==0:
        myList.append(x)
    x += 1
print(myList)
