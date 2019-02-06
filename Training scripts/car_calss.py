# coding=utf-8
# noinspection PyByteLiteral
class Car():
    """Простая модель автомобиля."""

    def __init__(self, make, model, year):
        """Инициализирует атрибуты описания автомобиля."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """ Возвращает аккуратно отформатированное описание. """
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """Reads odometer value and print it (keeps mileage of current car)"""
        print("This car has {0} miles on it".format(str(self.odometer_reading)))

    def update_odometer(self, mileage):
        """Set defined value for odometer, if value decreased the changes
        ignored"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You cannot roll back the odometer!")

    def increment_odometer(self, miles):
        """Increase odometer value according to set increment"""
        self.odometer_reading += miles


my_used_car = Car("Subaru", "Outback", 2008)
print(my_used_car.get_descriptive_name())
my_used_car.update_odometer(23500)
my_used_car.read_odometer()
my_used_car.increment_odometer(100)
my_used_car.read_odometer()

my_new_car = Car('audi', 'a4', 2016)
my_new_car.update_odometer(55)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
