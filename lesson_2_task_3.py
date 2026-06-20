def square(side):
    """
    Рассчитывает площадь квадрата по длине его стороны.

    Args:
        side (int or float): длина стороны квадрата (должна быть положительным числом)


    Returns:
        int or float: площадь квадрата (side ** 2)

    Raises:
        ValueError: если сторона отрицательная или равна нулю
        TypeError: если сторона не является числом
    """
    # Проверка типа данных
    if not isinstance(side, (int, float)):
        raise TypeError("Сторона квадрата должна быть числом")

    # Проверка на положительность
    if side <= 0:
        raise ValueError("Сторона квадрата должна быть положительным числом")

    return side ** 2


# Примеры использования функции
print(square(5))  # 25
print(square(3.5))  # 12.25
print(square(10))  # 100