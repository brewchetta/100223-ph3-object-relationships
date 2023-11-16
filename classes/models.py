# CAR - GARAGE RELATIONSHIP ###

# CAR ###
class Car:

    all_cars = []

    def __init__(self, make, model, license_plate, garage):
        self.make = make
        self.model = model
        self.license_plate = license_plate
        self.garage = garage
        Car.all_cars.append(self)

    def __repr__(self):
        return f"Car(make={self.make}, model={self.model}, license_plate={self.license_plate})"

# GARAGE ###
class Garage:
    
    def __init__(self, address):
        self.address = address

    def __repr__(self):
        return f"Garage(address={self.address})"

    def filter_car(self, car):
        return car.garage == self

    def cars(self):
        return [ car for car in Car.all_cars if car.garage == self ]
        # return list(filter(self.filter_car, Car.all_cars))


my_garage = Garage("Main St")

pontiac = Car("Pontiac", "GTO", "123456", my_garage)
batmobile = Car("Wayne Enterprises", "Batmobile", "JUSTICE", my_garage)
ferrari = Car("Ferrari", "812 Superfast", "COOLGUY", my_garage)

moises_garage = Garage("42nd St")

pop_mobile = Car("Vatican Industries", "Popemobile", "HOLYSEE", moises_garage)
ice_cream_truck = Car("Mr Softee", "Soft Serve", "GOODHUMOUR", moises_garage)
tesla = Car("X", "Tesla", "X", moises_garage)





##############################



# DOCTOR - PATIENT RELATIONSHIP ###

# DOCTOR ###
class Doctor:

    def __init__(self, name, specialty):
        self.name = name
        self.specialty = specialty

    def __repr__(self):
        return f"Doctor(name={self.name}, specialty={self.specialty})"
    
    def appointments(self):
        return [ appt for appt in Appointment.all_appointments if appt.doctor == self]
    
    def patients(self):
        all_patients = [ appt.patient for appt in Appointment. all_appointments if appt.doctor == self]

        uniq_patients = list( set( all_patients ) )

        return uniq_patients

# PATIENT ###
class Patient:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return f"Patient(first_name={self.first_name}, last_name={self.last_name})"
    
    def appointments(self):
        return [ appt for appt in Appointment.all_appointments if appt.patient == self]

class Appointment:

    all_appointments = []

    def __init__(self, date, doctor, patient):
        self.date = date
        self.doctor = doctor
        self.patient = patient
        Appointment.all_appointments.append(self)

    def __repr__(self):
        return f"Appoinment(date={self.date}, patient_name={self.patient.first_name} {self.patient.last_name}, doctor={self.doctor.name} )"
    

p1 = Patient("John", "Doe")
p2 = Patient("Jane", "Doe")
p3 = Patient("Jim", "Doe")

d1 = Doctor("Smith", "Dermatology")
d2 = Doctor("Johnson", "Neuroproctology")

a1 = Appointment("Nov 16", d1, p1)
a2 = Appointment("Nov 22", d1, p2)
a3 = Appointment("Nov 32", d1, p3)
a4 = Appointment("Nov 64", d2, p1)
a5 = Appointment("Nov 128", d1, p1)
a6 = Appointment("Nov 256", d2, p2)
a7 = Appointment("Nov 512", d2, p1)




##############################
    
# we didn't get to this but you can attempt it if you want!

# STUDENT - INSTRUCTOR - COURSE - ASSIGNMENT - SCHOOL RELATIONSHIP ###

# STUDENT ###
class Student:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Student(name={self.name})"
    
# INSTRUCTOR ###
class Instructor:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Instructor(name={self.name})"
    
# COURSE ###
class Course:

    def __init__(self, subject, start_date):
        self.subject = subject

    def __repr__(self):
        return f"Course(subject={self.subject})"

# ASSIGNMENT ###
class Assignment:

    def __init__(self, title, grade):
        self.title = title
        self.grade = grade

    def __repr__(self):
        return f"Assignment(title={self.title}, grade={self.grade})"

# SCHOOL ###
class School:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"School(name={self.name})"
        
##############################