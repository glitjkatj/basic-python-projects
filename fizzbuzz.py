print("\n" + "*" * 30)
print("Hello! This is the FizzBuzzer!")
print("*" * 30 + "\n")
print("""How this works:
You enter a starting number and an ending number.
The multiples of 3 are Fizzed,
And the multiples of 5 are Buzzed.
Multiples of both are FizzBuzzed.\n""")

start_num = int(input("Enter an integer for the starting number: >> "))
end_num = int(input("Enter an integer for the ending number: >> "))

# for loop goes through the range of numbers
# range() does not include the stop number, which is why there is a + 1
for num in range(start_num, end_num + 1):
    # conditional statements using modulus to check for multiples
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)