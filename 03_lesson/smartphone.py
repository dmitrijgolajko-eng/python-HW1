class Smartphone:
    def __init__(self, brand, model, phone_number):
        """
        Конструктор класса Smartphone.

        Args:
            brand (str): марка телефона
            model (str): модель телефона
            phone_number (str): абонентский номер (например, '+79...')
        """
        self.brand = brand
        self.model = model
        self.phone_number = phone_number
