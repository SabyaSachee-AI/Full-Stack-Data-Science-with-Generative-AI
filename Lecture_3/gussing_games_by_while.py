# print("Creat a random number(1-100)using random internal pakage of python.")
# print("take a number from user input--->as guess number")
# print("compare/math the number")
# print("if guess>generate number----->>guess a lower number")
# print("if guess<generate num--->>guess a higher number")
# print("if number correct show the number")


import random
jackpot =random.randint(1,100)
print(jackpot)

guess_number = int(input("Guess a number:"))

counter = 1
while guess_number != jackpot:
    if guess_number< jackpot:
        print("Wrong...please guess higher")
    
    else:
        print("Wrong!..Please guess lower")

    guess_number = int(input("Guess a number:"))
    counter +=1
else:
    print("Correct Guess")
    print("print your attempt:" ,counter)