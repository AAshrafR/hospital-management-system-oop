from patient import Patient
from staff import Staff


class Department:
    '''
    Represent a hospital department.

    Attributes:
        name (str): The name of the department.
        patients (list[Patient]): Patients managed by the department.
        staff (list[Staff]): Staff members employed by the department.
    '''

    def __init__(self, name: str):
        '''
        Initialize a Department.

        Args:
            name (str): The name of the department.

        Example:
            department = Department("Cardiology")
        '''
        self.name = name
        self.patients: list[Patient] = []
        self.staff: list[Staff] = []

    def add_patient(self, patient: Patient) -> None:
        '''
        Add a patient to the department.
  
        Args:
            patient (Patient): The patient to be added.

        Returns:
            None

        Example:
            department.add_patient(patient)
        '''
        self.patients.append(patient)

    def add_staff(self, staff_member: Staff) -> None:

        '''
        Add a staff member to the department.

        Args:
            staff_member (Staff): The staff member to be added.

        Returns:
            None

        Example:
            department.add_staff(staff)
        '''
        self.staff.append(staff_member)