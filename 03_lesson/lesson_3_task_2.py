from smartphone import Smartphone

# Создаём список для хранения смартфонов
catalog = []

# Наполняем список пятью разными экземплярами класса Smartphone
catalog.append(Smartphone("Samsung", "Galaxy S24", "+79001112233"))
catalog.append(Smartphone("Apple", "iPhone 15", "+79004445566"))
catalog.append(Smartphone("Xiaomi", "Redmi Note 13", "+79007778899"))
catalog.append(Smartphone("Honor", "Magic 6", "+79002223344"))
catalog.append(Smartphone("Realme", "GT 6", "+79005556677"))

# Проходим по списку и выводим информацию о каждом смартфоне
for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")
