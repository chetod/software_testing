def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    
# print(fizzbuzz(15))  # FizzBuzz
# print(fizzbuzz(3))  # Fizz
# print(fizzbuzz(5))  # Buzz
# print(fizzbuzz(7))  # 7
