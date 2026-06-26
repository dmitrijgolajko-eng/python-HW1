from address import Address
from mailing import Mailing

# Создаём адрес отправителя
from_addr = Address("101000", "Москва", "Арбат", "1", "5")

# Создаём адрес получателя
to_addr = Address("190000", "Санкт-Петербург", "Невский проспект", "10", "23")

# Создаём экземпляр почтового отправления
mailing = Mailing(
    to_address=to_addr,
    from_address=from_addr,
    cost=350,
    track="RU123456789ZZ"
)

# Формируем и выводим информацию об отправлении
print(
    f"Отправление {mailing.track} из {mailing.from_address.index}, "
    f"{mailing.from_address.city}, {mailing.from_address.street}, "
    f"{mailing.from_address.house} - {mailing.from_address.apartment} "
    f"в {mailing.to_address.index}, {mailing.to_address.city}, "
    f"{mailing.to_address.street}, {mailing.to_address.house} -"
    f"{mailing.to_address.apartment}. Стоимость {mailing.cost} рублей."
)
