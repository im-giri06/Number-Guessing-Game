import random
import math
# Initializing lower and upper bound
lower = int(input("Enter the Lower Bound : "))
upper = int(input("Enter the Upper Bound : "))

# Generating random number
x = random.randint(lower,upper)

# Initializing number of chances for guessing
y = round(math.log(upper-lower+1,2))

print("/n You have only",y,"chances")

# Initializing Game Logic 
count = 0
while count<y:

    count+=1

    guess = int(input("Enter your Guess :"))

    if x==guess:
        print("You Have Guessed it right in ",y,"chances.")
        break
    if x>guess:
        print("You have guessed too small")

    if x<guess:
        print("You have guessed too high")

if count>=y:
    print("You have Exceeded your chances")
    print("The Number is : ",x)
    print("Better Luck Next Time!!")


