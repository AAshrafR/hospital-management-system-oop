# 🏥 Hospital Management System

A simple **Hospital Management System** developed using **Python and Object-Oriented Programming (OOP)** principles.

The project was developed as a team based on the provided **UML class diagram**. We implemented the main classes and their relationships according to the UML design, then extended and improved the system with additional functionality and better data management.

## 📌 Project Overview

The Hospital Management System is designed to represent the basic structure of a hospital and manage its:

* Hospitals
* Departments
* Patients
* Staff members
* Patient medical records

The project demonstrates important **Object-Oriented Programming concepts**, including:

* Classes and Objects
* Inheritance
* Encapsulation
* Associations between classes
* Composition/containment relationships
* Modular project structure

---

## 🧩 UML Design

The system was initially designed using the following UML class diagram.

Our team implemented the system according to this UML and then **developed and extended the design** to provide more functionality and a more complete hospital management system.

<img width="634" height="521" alt="hospital_uml_diagram" src="https://github.com/user-attachments/assets/ee6166d8-3fa1-4dc8-8763-0396c13939ec" />


### Main Relationships

The UML design defines the following relationships:

* A **Hospital** contains multiple **Departments**.
* A **Department** manages multiple **Patients**.
* A **Department** employs multiple **Staff** members.
* Both **Patient** and **Staff** inherit from the base **Person** class.
* A **Patient** has a medical record.
* A **Staff** member has a specific position.

---

## 🏗️ Project Structure

```text
hospital-management-system-oop/
│
├── src/
│   └── python_hms/
│       ├── person.py
│       ├── patient.py
│       ├── staff.py
│       ├── department.py
│       ├── hospital.py
│       └── main.py
│
├── README.md
├── LICENSE
└── .gitignore
```

---

## 👨‍💻 Classes

### `Person`

The base class for people in the system.

It contains common information such as:

* `name`
* `age`

It also provides basic information display functionality.

---

### `Patient`

`Patient` inherits from `Person`.

In addition to the common person information, a patient has:

* `medical_record`
* `department`

The patient class provides functionality for:

* Viewing medical records
* Updating medical records
* Assigning a patient to a department
* Viewing complete patient information

---

### `Staff`

`Staff` also inherits from `Person`.

A staff member has an additional:

* `position`

For example:

```text
Doctor
Nurse
Administrator
```

The class provides functionality for displaying staff information.

---

### `Department`

A department represents a hospital department such as:

```text
Cardiology
Emergency
Surgery
```

Each department can manage:

* Multiple patients
* Multiple staff members

It provides methods such as:

```python
add_patient()
add_staff()
```

---

### `Hospital`

The `Hospital` class represents the hospital itself.

It contains:

* `name`
* `location`
* A collection of departments

Departments can be added using:

```python
add_department()
```

---

## 💾 Data Persistence

The system supports saving hospital data so that information can be preserved instead of being lost when the program closes.

When the data is saved, the system creates/updates:

```text
hospital_data.json
```

This JSON file is used to store the hospital's data and allows the system to keep previously saved information.

Example:

```text
hospital_data.json
```

This provides a simple and lightweight way to persist the system's data without requiring an external database.

---

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/AAshrafR/hospital-management-system-oop.git
```

### 2. Navigate to the project

```bash
cd hospital-management-system-oop
```

### 3. Run the main program

```bash
python src/python_hms/main.py
```

---

## 🧪 Example

The system can create a hospital with multiple departments, patients, and staff members.

For example:

```text
Hospital
│
├── Cardiology
│   ├── Patients
│   │   └── Mario
│   └── Staff
│       └── Doctor
│
└── Emergency
    ├── Patients
    │   └── Mark
    └── Staff
        └── Nurse
```

---

## 🎯 OOP Concepts Demonstrated

This project focuses on applying Object-Oriented Programming concepts in a practical example.

### Inheritance

`Patient` and `Staff` inherit common attributes and behavior from `Person`.

```text
        Person
        /    \
       /      \
   Patient    Staff
```

### Encapsulation

Each class is responsible for managing its own data and behavior.

For example, `Patient` manages its medical record, while `Department` manages its patients and staff members.

### Relationships

The system models real-world relationships between hospitals, departments, patients, and staff members.

---

## 🤝 Team Development

This project was developed collaboratively by our team.

We started from the provided **UML class diagram** and implemented the system according to its structure and relationships. During development, we didn't just reproduce the UML; we **improved and extended the original design** by adding additional functionality and data persistence features.

This allowed us to turn the initial UML design into a more complete and practical Hospital Management System.

---

## 📚 Technologies Used

* **Python**
* **Object-Oriented Programming (OOP)**
* **JSON** for data persistence
* **Git & GitHub** for version control and collaboration
* **UML** for system design

---

## 📄 License

This project is licensed under the **MIT License**.
