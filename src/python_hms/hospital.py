import json

from department import Department
from patient import Patient
from staff import Staff


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
            hospital = Hospital('City Hospital', 'Cairo')
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

    def to_dict(self) -> dict:

        '''
        Convert the hospital object into a dictionary.

        Returns:
            dict: A dictionary containing the hospital's name,
                  location, and all its departments.

        Example:
            data = hospital.to_dict()
        '''

        return {
            'name': self.name,
            'location': self.location,
            'departments': [
                department.to_dict()
                for department in self.departments
            ]
        }

    def save_to_json(self, filename: str = 'hospital_data.json') -> None:

        '''
        Save the hospital data to a JSON file.

        Args:
            filename (str): The name of the JSON file where the
                            hospital data will be saved.

        Returns:
            None

        Example:
            hospital.save_to_json('hospital_data.json')
        '''

        data = self.to_dict()

        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(
                data,
                file,
                indent=4,
                ensure_ascii=False
            )
        print(f'\nAll hospital data successfully saved to {filename}.')

    @classmethod
    def load_from_json(
        cls,
        filename: str = 'hospital_data.json'
    ) -> 'Hospital | None':

        '''
        Load hospital data from a JSON file and rebuild the objects.

        Args:
            filename (str): The name of the JSON file containing
                            the hospital data.

        Returns:
            Hospital | None: A Hospital object containing the loaded
                             data, or None if the file does not exist.

        Example:
            hospital = Hospital.load_from_json('hospital_data.json')
        '''

        try:
            with open(filename, 'r', encoding='utf-8') as file:
                data = json.load(file)

            # Create the hospital object
            hospital = cls(
                data['name'],
                data['location']
            )

            # Create departments
            for department_data in data.get('departments', []):

                department = Department(
                    department_data['name']
                )

                # Create patients
                for patient_data in department_data.get('patients', []):

                    patient = Patient(
                        patient_data['name'],
                        patient_data['age'],
                        patient_data['medical_record']
                    )

                    department.add_patient(patient)

                # Create staff
                for staff_data in department_data.get('staff', []):

                    staff = Staff(
                        staff_data['name'],
                        staff_data['age'],
                        staff_data['position']
                    )

                    department.add_staff(staff)

                hospital.add_department(department)

            print(f'\nData successfully loaded from {filename}.')

            return hospital

        except FileNotFoundError:

            print(f'\nError: The file {filename} was not found.')

            return None

    def display_info(self) -> None:

        '''
        Display the hospital information, including departments,
        patients, and staff members.

        Returns:
            None

        Example:
            hospital.display_info()
        '''

        print(f'\nHospital: {self.name}')
        print(f'Location: {self.location}')

        for department in self.departments:

            print(f'\nDepartment: {department.name}')

            print('Patients:')
            for patient in department.patients:
                print(f'  - {patient.view_record()}')

            print('Staff:')
            for staff in department.staff:
                print(f'  - {staff.view_info()}')