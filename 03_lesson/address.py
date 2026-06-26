class Address:
    def __init__(self, index, city, street, house, apartment):
        """
        Конструктор класса Address.

        Args:
            index (str): индекс
            city (str): город
            street (str): улица
            house (str): дом
            apartment (str): квартира
        """
        self.index = index
        self.city = city
        self.street = street
        self.house = house
        self.apartment = apartment
