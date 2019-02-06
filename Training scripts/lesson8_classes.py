class Animate:
    pass


class Animals(Animate):
    def breathe(self):
        print('Breath')

    def move(self):
        print('Move')

    def eat_food(self):
        print('Eat')


class Mammals(Animals):
    def feed_young_with_milk(self):
        print('Feed youngs with milk')


class Giraffes(Mammals):
    def __init__(self, spots):
        self.giraffe_spots = spots

    def eat_leaves_from_trees(self):
        self.eat_food()
        print('Eat leaves from the trees')

    def find_food(self):
        self.move()
        print('I\'ve found food')
        self.eat_food()

    def left_foot_forward(self):
        print('Left foot forward!')

    def left_foot_back(self):
        print('left foot back!')

    def right_foot_forward(self):
        print('right foot forward!')

    def right_foot_back(self):
        print('right foot back!')

    def dance_a_jig(self):
        self.right_foot_forward()
        self.left_foot_forward()
        self.right_foot_back()
        self.left_foot_back()


ozwald = Giraffes(100)
gertrude = Giraffes(150)
reginald = Giraffes(50)
harold = Giraffes(10)

reginald.move()
reginald.eat_leaves_from_trees()
harold.move()
reginald.dance_a_jig()
reginald.dance_a_jig()
reginald.find_food()
reginald.eat_food()
