"""
Instructions: Implement Python programs to accomplish the following task

Task

You are tasked with creating a Python program that serves as an interactive tool for a friend who 
enjoys exploring numbers. The program should begin by prompting the user to enter their name and then 
ask them for three of their favorite numbers. After gathering this information, the program should 
greet the user with a personalized message that includes their name. The three numbers provided by 
the user should be stored in a list. The program should then check if any of the numbers are even or 
odd, and store this information in a separate list of tuples, where each tuple contains the number and
a string indicating whether it is "even" or "odd". Following this, the program should use a for loop
to iterate over the list of numbers, and for each number, it should create a tuple containing the number
and its square. These tuples should be printed in a creative and engaging format. Additionally, the program
should calculate the sum of the three numbers and print the result, accompanied by an encouraging message. 
Finally, the program should determine if the sum is a prime number and notify the user with an appropriate 
message. The goal is to make the tool both enjoyable and informative, allowing the user to explore their
favorite numbers in a fun and interactive way, while also introducing some interesting logical checks.
"""
def is_prime(num):
    if num <= 1:
        return False
    for i in range(3, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True    
    
# Ask the User to enter their favorite numbers
def User():
    
    # prompting the user to enter their name

    name = input("Hello! What's your name? ")
    
    # Ask the User to enter their favorite numbers
    print(f"Nice to meet you, {name}! I'd love to know three of your favorite numbers.")

    numbers = []
    for i in range(3):
        fav_num = int(input(f"Enter Your Favourite Number {i + 1}: "))
        numbers.append(fav_num)
    print(f"Thanks {name}!. These are your favorite numbers: {numbers}")
    
    # check if any of the numbers are even or odd
    parity = [(num, "even" if num % 2 == 0 else "odd") for num in numbers]
    
    # Create tuples of numbers and their squares
    squares = [(num, num**2) for num in numbers]
    
    for num, p in parity:
        print(f"{num} is {p}")
        
    for num, square in squares:
        print(f"The square of {num} is {square}")    
    
    # Calculate the sum of the numbers
    total_sum = sum (numbers)
    print(f"The sum of your favorite numbers is : {total_sum}")    
    
    # Provide an encouraging message based on the sum
    if   total_sum >100:
        print("Wow! That's a big number! You are thinking Big!")
    elif total_sum < 10:   
        print("Small and mighty! Every number counts") 
    else:
        print("Nice that's a solid sum!")
    
    if is_prime(total_sum):
        print(f"Great! {total_sum} is a prime number!")
    else:
        print(f"{total_sum} is not a prime number, but it's a great number")        
User()
