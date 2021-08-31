#Defining Factorial Function
def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        n = n * fact(n - 1)
        return n

# Starting the main Program
print("Welcome to the program to find the factorial of a given number")

# Taking input from user
num = int(input("Enter the Number \n"))

#Calling the Factorial Function and printing the Answer
print(f"the factorial of {num} is {fact(num)}")
