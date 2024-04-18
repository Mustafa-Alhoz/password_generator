import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+',',','.','/',']','[','-','_','=']

print('''
  __    _    __   __         __    __    __       __   ___        ___   __    _  ____   __    __  
 /__)  /_|  (    (   (   /  /  )  /__)  /  )     / _  (_    /| ) (_    /__)  /_|  /    /  )  /__) 
/     (  | __)  __)  |/|/  (__/  / (   /(_/     (__)  /__  / |/  /__  / (   (  | (    (__/  / (   
                                                                                               
''')

print("\nWelcome to the Password Generator!")
print("\nTHIS PROGRAMME WAS MADE BY THE BEST PROGRAMMER EVER ===> @mustafa_alhoz ")
nr_letters= int(input("\nHow many letters would you like in your password?\n")) 
nr_numbers = int(input("How many numbers would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like in your password?\n"))

random_letter=random.sample(letters,k=42)
random_number=random.sample(numbers,k=10)
random_symbol=random.sample(symbols,k=17)

the_password=random_letter+random_number+random_symbol

random.shuffle(the_password)

the_real_password=""
for x in the_password:
    the_real_password += x

print(f"\nYOUR NEW PASSWORD IS: {the_real_password}\n")    

