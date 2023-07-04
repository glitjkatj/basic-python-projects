print("\n" + "*" * 30)
print("Hello! This is the FizzBuzzer!")
print("*" * 30 + "\n")
print("""How this works:
You enter a starting number and an ending number.
The multiples of 3 are Fizzed,
And the multiples of 5 are Buzzed.
Multiples of both are FizzBuzzed.\n""")

for num in range(1,101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)