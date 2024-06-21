def fb(n):
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return ""

for i in range(1, 21):
    result = fb(i)
    if result:
        print(f"{i} {result}")
    else:
        print(i)
