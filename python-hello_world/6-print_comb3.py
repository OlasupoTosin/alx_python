for number in range(10):
    for numbers in range(10):
        if(number == 8 and numbers == 9):
            print("{}" .format(str(number) + str(numbers)))
        elif(numbers > number):
            print("{}" .format(str(number) + str(numbers)) + ", ", end="")