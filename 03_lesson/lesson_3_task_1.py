from user import User

# Создаём экземпляр класса User и сохраняем в переменную
my_user = User("Алексей", "Смирнов")

# Вызываем все методы у объекта
my_user.print_first_name()      # Вывод: Алексей
my_user.print_last_name()       # Вывод: Смирнов
my_user.print_full_name()       # Вывод: Алексей Смирнов
