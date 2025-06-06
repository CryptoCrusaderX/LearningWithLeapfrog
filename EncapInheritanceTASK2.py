class Person:
    def __init__(self, name, age, number):
        self._name = name
        self._age = age
        self.__contact_number = number

    @property
    def contact_number(self):
        return self.__contact_number

    @contact_number.setter
    def contact_number(self, new_num):
        if new_num:
            self.__contact_number = new_num
        else:
            raise ValueError("Contact number can't be empty!")

    def display_person_info(self):
        print(f"Name: {self._name}")
        print(f"Age: {self._age}")
        print(f"Contact Number: {self.__contact_number}")


# Patient class inheriting Person class
class Patient(Person):
    def __init__(self, name, age, number, patient_id, ailments=None):
        super().__init__(name, age, number)
        self.__patient_id = patient_id
        self.__ailments = ailments if ailments else []

    def add_ailment(self, new_ailment):
        if new_ailment:
            self.__ailments.append(new_ailment)
        else:
            raise ValueError("Ailment can't be empty!")

    def view_ailments(self):
        print(f"Ailments: {self.__ailments}")

    def get_patient_id(self):
        return self.__patient_id

    def display_patient_details(self):
        self.display_person_info()
        print(f"Patient ID: {self.__patient_id}")
        self.view_ailments()


# Doctor class extending Person class
class Doctor(Person):
    def __init__(self, name, age, number, doctor_id):
        super().__init__(name, age, number)
        self.__doctor_id = doctor_id
        self._assigned_patients = []

    def assign_patient(self, patient):
        self._assigned_patients.append(patient)

    def remove_patient_by_id(self, pid):
        self._assigned_patients = [
            p for p in self._assigned_patients if p.get_patient_id() != pid
        ]

    def display_assigned_patients_ids(self):
        ids = [p.get_patient_id() for p in self._assigned_patients]
        print(f"Assigned Patient IDs: {ids}")

    def display_doctor_details(self):
        self.display_person_info()
        print(f"Doctor ID: {self.__doctor_id}")
        self.display_assigned_patients_ids()


# Hospital class to manage patients
class Hospital:
    def __init__(self):
        self._admitted_patients = []

    def admit_patient(self, patient):
        self._admitted_patients.append(patient)
        print(f"Patient {patient.get_patient_id()} admitted.")

    def discharge_patient(self, pid):
        self._admitted_patients = [
            p for p in self._admitted_patients if p.get_patient_id() != pid
        ]
        print(f"Patient {pid} discharged.")

    def show_admitted_patients(self):
        print("Admitted Patients IDs:")
        for p in self._admitted_patients:
            print(p.get_patient_id())


# Just testing everything here
if __name__ == "__main__":
    # hospital setup
    hospital = Hospital()

    # making patients
    p1 = Patient("Aayush", 28, "9800000001", "P001", ["Cold"])
    p2 = Patient("Rina", 35, "9800000002", "P002", ["Fever"])
    p3 = Patient("Sita", 22, "9800000003", "P003")

    # add more ailments to one patient
    p3.add_ailment("Cough")

    # admit them
    hospital.admit_patient(p1)
    hospital.admit_patient(p2)
    hospital.admit_patient(p3)

    hospital.show_admitted_patients()

    # make a doctor
    d1 = Doctor("Dr. Karki", 45, "9841000000", "D101")

    # assign patients
    d1.assign_patient(p1)
    d1.assign_patient(p3)

    print("\n--- Doctor Details ---")
    d1.display_doctor_details()

    print("\n--- Patient Details ---")
    p1.display_patient_details()
    print()
    p3.display_patient_details()

    # remove a patient from doctor
    d1.remove_patient_by_id("P003")
    print("\n--- Updated Patients Assigned to Doctor ---")
    d1.display_assigned_patients_ids()

    # discharge one patient
    hospital.discharge_patient("P002")
    print("\n--- Updated Admitted Patients ---")
    hospital.show_admitted_patients()
