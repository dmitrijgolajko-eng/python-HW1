def month_to_season(month):
    """
    Возвращает название сезона по номеру месяца.

    Args:
        month (int): номер месяца (от 1 до 12)

    Returns:
        str: название сезона («Зима», «Весна», «Лето» или «Осень»)
    Raises:
        ValueError: если номер месяца не в диапазоне 1–12
    """
    # Проверка корректности входного значения
    if not isinstance(month, int) or month < 1 or month > 12:
        raise ValueError("Номер месяца должен быть целым числом от 1 до 12")

    # Словарь: диапазоны месяцев для каждого сезона
    season_map = {
        (12, 1, 2): "Зима",
        (3, 4, 5): "Весна",
        (6, 7, 8): "Лето",
        (9, 10, 11): "Осень"
    }

    # Поиск сезона по номеру месяца
    for months, season in season_map.items():
        if month in months:
            return season

    # Резервный возврат (на случай логических ошибок — теоретически не достижим при корректных данных)
    raise ValueError("Неизвестный месяц")

# Примеры использования функции
print(month_to_season(2))   # Зима
print(month_to_season(5))   # Весна
print(month_to_season(8))   # Лето
print(month_to_season(11))  # Осень
print(month_to_season(12))  # Зима