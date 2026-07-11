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
    if number < 0:break
