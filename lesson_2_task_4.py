def fizz_buzz(n):
    """
    Печатает числа от 1 до n с заменой по правилам FizzBuzz:
    - делится на 3 → 'Fizz'
    - делится на 5 → 'Buzz'
    - делится на 3 и 5 → 'FizzBuzz'
    - иначе → само число

    Args:
        n (int): верхнее граничное число (включительно)
    """
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

# Пример вызова функции
fizz_buzz(15)