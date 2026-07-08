def  is_int(Age):
    try:
        Age = int(Age)
        return Age
            
    except ValueError:
        while True:
            print("The entered age is not a number.")
            Age =(input("Re-enter the Age's life:"))
            try:
                Age = int(Age)
                return Age
            except ValueError:
                continue


number = input("number:")
number = is_int(number)

while True:
    print(number)
    number = number -1
    if number < 0:break