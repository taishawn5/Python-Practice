def fizz_buzz(input):
    if input % 3 == 0 and input % 5 == 0:
        return print("fizzbuzz")
    elif input % 3 == 0:
        return print("fizz")
    elif input % 5 == 0:
        return print("buzz")
    return print(input)

fizz_buzz(17)