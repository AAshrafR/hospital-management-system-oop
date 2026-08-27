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

    def view_info(self) -> str:
        '''this function returns the person name and age '''
        return f"Name: {self.name}, Age: {self.age}"