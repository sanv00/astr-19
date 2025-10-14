# Define a class describing your favorite animal
class Pig:
    def __init__(self, arm_length, leg_length, num_eyes, has_tail, is_furry):
        self.arm_length = arm_length        # float
        self.leg_length = leg_length        # float
        self.num_eyes = num_eyes            # int
        self.has_tail = has_tail            # bool
        self.is_furry = is_furry            # bool

    # Member function to describe the animal
    def describe(self):
        print("Animal: Pig")
        print(f"Length of arms: {self.arm_length} inches")
        print(f"Length of legs: {self.leg_length} inches")
        print(f"Number of eyes: {self.num_eyes}")
        print(f"Has a tail: {'Yes' if self.has_tail else 'No'}")
        print(f"Is furry: {'Yes' if self.is_furry else 'No'}")


# Create an instance of the class with example values
my_pig = Pig(arm_length=8.0, leg_length=12.5, num_eyes=2, has_tail=True, is_furry=False)

# Call the describe method to print the information
my_pig.describe()