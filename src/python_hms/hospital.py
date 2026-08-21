from department import Department


class Hospital:
    '''
    Represent a hospital that contains multiple departments.

    Attributes:
        name (str): The name of the hospital.
        location (str): The location of the hospital.
        departments (list[Department]): Departments contained in the hospital.
    '''

    def __init__(self, name: str, location: str):
        '''
        Initialize a Hospital.

        Args:
            name (str): The name of the hospital.
            location (str): The location of the hospital.

        Example:
            hospital = Hospital("City Hospital", "Cairo")
        '''
        self.name = name
        self.location = location
        self.departments: list[Department] = []

    def add_department(self, department: Department) -> None:
        '''
        Add a department to the hospital.

        Args:
            department (Department): The department to be added.

        Returns:
            None

        Example:
            hospital.add_department(department)
        '''
        self.departments.append(department)
        print(f"Department '{department.name}' added to {self.name}.")