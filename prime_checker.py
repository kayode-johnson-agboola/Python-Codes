# This python function test if a number is a prime number or not
# A prime number is a number that can only be divided by 1 and itself
# A prime number therefore has only 2 factors
def prime_checker(number):
    # set the initial value of the variable count to zero. Count check for the number of factors of a given number
    count = 0
    # 1 is not a prime number because it has just a factor. Prime numbers must have tw0(2)
    if number == 1:
        print(f"{number} is not a prime number")
    # For any other different from one
    else:
        # Divide the number to check for by numbers from 1 to itself
        for i in range(1, number+1):
            remainder_zero = number%i
            if remainder_zero == 0:
                #If the remainder is zero, i must be a factor of the number. Increment i by 1
                count += 1
        # If the total number of count is 2. It is then a prime number. Prime numbers have only 2 factors
        if count == 2:
            print(f"{number} is a prime number")
        else:
            print(f"{number} is not a prime number")

n = int(input("Enter number to check: "))
prime_checker(number=n)