import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# #Easy Version:
# letter_part=""
# for l in range(1,nr_letters+1):
#     rnd_letter_pos=random.randint(1,len(letters))
#     letter_part+=letters[rnd_letter_pos]
#
# symbol_part=""
# for s in range(1,nr_symbols+1):
#     rnd_symbol_pos=random.randint(1,len(symbols))
#     symbol_part+=symbols[rnd_symbol_pos]
#
# number_part=""
# for l in range(1,nr_numbers+1):
#     rnd_number_pos=random.randint(1,len(numbers))
#     number_part+=numbers[rnd_number_pos]
#
# password=""
# password+=letter_part+symbol_part+number_part
# print(password)

#Hard version:
l=nr_letters
s=nr_symbols
n=nr_numbers
password=""
i=0
for i in range(0,nr_letters+nr_symbols+nr_numbers):
    rndChoice=random.randint(1,3)
    if rndChoice==1:
        if l>0:
            password += random.choice(letters)
            l -= 1
        else:
            rndChoice = random.randint(2, 3)
            if rndChoice == 2 and s>0:
                password += random.choice(symbols)
                s -= 1
            else:
                password += random.choice(numbers)
                n -= 1
    elif rndChoice==2:
        if s>0:
            password += random.choice(symbols)
            s -= 1
        else:
            rndChoice = random.randint(1, 3)
            if rndChoice == 1 and l>0:
                password += random.choice(letters)
                l -= 1
            else:
                password += random.choice(numbers)
                n -= 1
    elif rndChoice==3:
        if n>0:
            password += random.choice(numbers)
            n -= 1
        else:
            rndChoice = random.randint(1, 2)
            if rndChoice == 1 and l>0:
                password += random.choice(letters)
                l -= 1
            else:
                password += random.choice(symbols)
                s -= 1

print(password)