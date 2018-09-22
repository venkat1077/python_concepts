x = int(raw_input("Enter the number : "))


def factorial(x):
    if not x == 0:
        return x * factorial(x-1)
    else:
        return 1

print(func_factorial(5))

        
                  
