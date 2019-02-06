class Restaurant():
    """New class restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """Method that describe restaurant"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Print Restaurant description"""
        print("Welcome to {0} what serves the best {1} cuisine".format(
            str(self.restaurant_name), str(
                self.cuisine_type)))

    def open_restaurant(self):
        """Method that say if place is open or no"""
        print("This gorgeous place {0} is Open!".format(self.restaurant_name))


restaurant_cassiopiea = Restaurant('Cassiopeia', 'Greece')
restaurant_cassiopiea.describe_restaurant()
restaurant_cassiopiea.open_restaurant()
print(restaurant_cassiopiea.restaurant_name, restaurant_cassiopiea.cuisine_type)
