class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
    
    def move(self):
        return 'Транспорт движется'
    
    
    def info(self):
        return f'Марка: {self.brand}, Год: {self.year}'
    
    
carFer = Vehicle('Ferari', 2017)

class Car(Vehicle):
    def __init__(self, brand, year, num_doors):
        super().__init__(brand, year)   # Вместо self.brand = ... и self.year = ...
        self.num_doors = num_doors      # Исправлена опечатка

    def move(self):
        return f"Автомобиль {self.brand} едет по дороге"

    def info(self):
        base = super().info()
        return f"{base}, Количество дверей: {self.num_doors}"