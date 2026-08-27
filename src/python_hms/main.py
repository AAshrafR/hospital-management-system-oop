from hospital import Hospital
from department import Department
from patient import Patient
from staff import Staff


def main() -> None:

    '''
    Run the Hospital Management System.

    Allows the user to create hospital data, add departments,
    patients, and staff members, and save or load the data
    using a JSON file.

    Returns:
        None
    '''

    hospital = Hospital(
        input('Enter hospital name: '),
        input('Enter hospital location: ')
    )

    while True:

        print('\nHospital Management System')
        print('1. Add Department')
        print('2. Add Patient')
        print('3. Add Staff')
        print('4. Save Data')
        print('5. Load Data')
        print('6. Exit')

        choice = input('Enter your choice: ')

        if choice == '1':

            department_name = input(
                'Enter department name: '
            )

            department = Department(department_name)
            hospital.add_department(department)

        elif choice == '2':

            if not hospital.departments:
                print('Please add a department first.')
                continue

            name = input('Enter patient name: ')
            age = int(input('Enter patient age: '))
            medical_record = input(
                'Enter medical record: '
            )

            print('\nAvailable Departments:')

            for index, department in enumerate(
                hospital.departments,
                start=1
            ):
                print(f'{index}. {department.name}')

            department_index = int(
                input('Choose department: ')
            )

            department = hospital.departments[
                department_index - 1
            ]

            patient = Patient(
                name,
                age,
                medical_record
            )

            department.add_patient(patient)

        elif choice == '3':

            if not hospital.departments:
                print('Please add a department first.')
                continue

            name = input('Enter staff name: ')
            age = int(input('Enter staff age: '))
            position = input('Enter staff position: ')

            print('\nAvailable Departments:')

            for index, department in enumerate(
                hospital.departments,
                start=1
            ):
                print(f'{index}. {department.name}')

            department_index = int(
                input('Choose department: ')
            )

            department = hospital.departments[
                department_index - 1
            ]

            staff = Staff(
                name,
                age,
                position
            )

            department.add_staff(staff)

        elif choice == '4':

            hospital.save_to_json()

        elif choice == '5':

            loaded_hospital = Hospital.load_from_json()

            if loaded_hospital is not None:
                hospital = loaded_hospital
                hospital.display_info()

        elif choice == '6':

            break

        else:

            print('Invalid choice. Please try again.')


if __name__ == '__main__':
    main()