class Person:
    """
    Represents a general person in the system.

    Attributes:
        name (str): The full name of the person.
        age (int): The age of the person in years.
    """

    def __init__(self, name: str, age: int):
        """
        Initializes a new Person instance.

        Args:
            name (str): The full name of the person.
            age (int): The age of the person in years.
        """
        self.name = name
        self.age = age

    def view_info(self):
        """Displays the person's name and age formatted in the console."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

# Create the object and pass the data directly in one step
person1 = Person("Alex", 25)

# View person information
person1.view_info()