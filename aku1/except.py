try:
    print(10/0)
except ZeroDivisionError:
    print("Cant divide by zero")
except ArithmeticError:
    print("Error in calc")
except:
    print("something else wrong")
