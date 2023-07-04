print("*" * 30)
print("Hello! This is the FizzBuzzer!")
print("*" * 30)
print("""How this works: """)

for num in range(1,101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)