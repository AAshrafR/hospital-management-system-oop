from hospital import Hospital
from department import Department
from patient import Patient
from staff import Staff


def main() -> None:
    '''
    Run a simple test of the Hospital Management System.

    Creates a hospital, departments, patients, and staff members,
    then connects them according to the system relationships.

    Returns:
        None
    '''

    # Create a hospital
    hospital = Hospital("Cairo Hospital", "Cairo")

    # Create departments
    cardiology = Department("Cardiology")
    emergency = Department("Emergency")

    # Create patients
    patient1 = Patient("Mario", 30, "Heart disease")
    patient2 = Patient("Mark", 45, "Chest pain")

    # Create staff members
    staff1 = Staff("Abdelmasih", 35, "Doctor")
    staff2 = Staff("Sarah", 29, "Nurse")

    # Add departments to the hospital
    hospital.add_department(cardiology)
    hospital.add_department(emergency)

    # Add patients to departments
    cardiology.add_patient(patient1)
    emergency.add_patient(patient2)

    # Add staff to departments
    cardiology.add_staff(staff1)
    emergency.add_staff(staff2)

    # Display information
    print(f"Hospital: {hospital.name}")
    print(f"Location: {hospital.location}")
    print(f"Departments: {len(hospital.departments)}")

    print("\n________Staff Information ")
    print(staff1.view_info())
    print(staff2.view_info())

    print("\n________Patient Records ")
    print(patient1.view_record())
    print(patient2.view_record())


if __name__ == "__main__":
    main()