from person import Person

class Patient(Person):
    """
    Represents a patient in the hospital system, inheriting core attributes from Person.

    Attributes:
        medical_record (str): Detailed medical history or clinical notes.
        department (Department or None): The hospital department assigned to the patient.
    """

    def __init__(self, name: str, age: int, medical_record: str = ""):
        """
        Initializes a new Patient instance.

        Args:
            medical_record (str, optional): Initial medical record entries. Defaults to "".

        Raises:
            TypeError: If medical_record is not a string.
        """
        
        super().__init__(name, age)
        
        if not isinstance(medical_record, str):
            raise TypeError("Medical record must be a text string.")

        self.medical_record = medical_record
        self.department = None
        
        print(f" Patient created: {self.name}")

    def view_record(self) -> str:
        """
        Retrieves the medical record of the patient.

        Returns:
            str: A formatted message containing the medical record or stating its absence.
        """
        if self.medical_record:
            return f"Medical record for {self.name}: {self.medical_record}"
        return f"No medical record found for {self.name}."

    def update_record(self, new_record: str) -> None:
        """
        Updates or overwrites the patient's medical record.

        Args:
            new_record (str): The new details to store in the medical record.

        Raises:
            TypeError: If new_record is not a string.
            ValueError: If new_record is empty or contains only whitespace.
        """
        if not isinstance(new_record, str):
            raise TypeError("New medical record must be a text string.")
        if not new_record.strip():
            raise ValueError("New medical record cannot be empty.")

        self.medical_record = new_record
        print(f" Medical record updated for {self.name}")

    def set_department(self, department) -> None:
        """
        Assigns the patient to a specific department.

        Args:
            department (Department): The department object to link with the patient.

        Raises:
            ValueError: If the department argument is None.
        """
        if department is None:
            raise ValueError("Department object cannot be None.")

        self.department = department

    def view_info(self) -> str:
        """
        Displays comprehensive information about the patient.

        Overrides Person.view_info() to append department and medical record details.

        Returns:
            str: Combined string of base person details, department, and medical record.
        """
        base_info = super().view_info()
        dept_info = f", Department: {self.department.name}" if self.department else ", No department assigned"
        record_info = f", Record: {self.medical_record}" if self.medical_record else ", No record"
        return base_info + dept_info + record_info