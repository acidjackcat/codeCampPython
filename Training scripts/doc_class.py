class Dog():
    """Simple model of regular dog"""

    def __init__(self, name, age):
        """Initialise atributes name and age."""
        self.name = name
        self.age = age

    def sit(self):
        """Собака садится по команде."""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """Собака перекатывается по команде."""
        print(self.name.title() + " rolled over!")
