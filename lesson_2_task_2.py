def is_year_leap(year):
    """
    Проверяет, является ли год високосным.

    Год считается високосным, если он делится на 4 без остатка.

    Args:
        year (int): номер года

    Returns:
        bool: True, если год високосный, False — если нет
    """
    if year % 4 == 0:
        return True
    else:
        return False

# Вызов функции с передачей года (выбран 2024 — високосный год)
test_year = 2024
result = is_year_leap(test_year)

# Вывод результата в требуемом формате
print(f"год {test_year}: {result}")