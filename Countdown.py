<<<<<<< HEAD
def  is_int(number):
    """
    This function checks whether the input is a number
    or not and if it is not a number,
    it receives the input again from the user.
    """
    try:
        number = int(number)
        return number
            
    except ValueError:
        while True:
            print("The entered number is not a number.")
            number =(input("Re-enter the number's life:"))
            try:
                number = int(number)
                return number
            except ValueError:
                continue


number = input("number:")
number = is_int(number)

while True:
    print(number)
    number = number -1
=======
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
>>>>>>> 8cf8a70ca7526f9ab8fe5b397acb3a0d0993a3d7
    if number < 0:break