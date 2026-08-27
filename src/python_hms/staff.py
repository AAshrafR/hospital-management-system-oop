from person import Person


class Staff(Person):

    '''
    Represent a hospital staff member.

    Inherits the name and age attributes from Person and adds
    a position attribute specific to the staff member.

    Attributes:
        position (str): The job position of the staff member.
    '''

    def __init__(self, name: str, age: int, position: str):

        '''
        Initialize a Staff object.

        Args:
            name (str): The name of the staff member.
            age (int): The age of the staff member.
            position (str): The job position of the staff member.

        Example:
            staff = Staff("John", 35, "Doctor")
        '''

        super().__init__(name, age)
        self.position = position

    def to_dict(self) -> dict:
        '''
        Convert the staff object into a dictionary.

        Returns:
            dict: A dictionary containing the staff member's name,
                age, and position.
        '''
        return {
            "name": self.name,
            "age": self.age,
            "position": self.position
        }
    
    def view_info(self) -> str:
        '''
        Return information about the staff member.

        Returns:
            str: The staff member's name, age, and position.

        Example:
            staff.view_info()
            'Name: John, Age: 35, Position: Doctor'
        '''
        return (
            f"Name: {self.name}, "
            f"Age: {self.age}, "
            f"Position: {self.position}"
        )