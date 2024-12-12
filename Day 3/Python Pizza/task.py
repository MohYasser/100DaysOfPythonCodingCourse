print("Welcome to Python Pizza Deliveries!")

size = input("What size pizza do you want? S, M or L: ")
while (not(size=="S" or size=="M" or size=="L")):
    size = input("please re-enter what size pizza you want? S, M or L: ")

pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
while(not(pepperoni=="Y" or pepperoni=="N")):
    pepperoni = input("Please re-enter if you want pepperoni on your pizza or not: Y or N: ")

extra_cheese = input("Do you want extra cheese? Y or N: ")
while(not(extra_cheese=="Y" or extra_cheese=="N")):
    extra_cheese = input("Please re-enter if you want extra cheese: Y or N: ")

total=0
#Size:
if(size=="S"):
    total=15
elif(size=="M"):
    total = 20
elif(size=="L"):
    total=25

#pepperoni:
if(pepperoni=="Y"):
    if(size=="S"):
        total+=2
    else: total+=3

#extra_cheese:
if(extra_cheese=="Y"):
    total+=1

print(f"Your final bill is: ${total}")