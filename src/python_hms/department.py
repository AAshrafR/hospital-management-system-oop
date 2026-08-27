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
        
    def to_dict(self) -> dict:
        '''
        Convert the department object into a dictionary.

        Returns:
            dict: A dictionary containing the department's name,
                patients, and staff. Each patient and staff member
                is converted into a dictionary using their to_dict()
                method.
        '''
        return {
            'name': self.name,
            'patients': [patient.to_dict() for patient in self.patients],
            'staff': [staff.to_dict() for staff in self.staff]
        }

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