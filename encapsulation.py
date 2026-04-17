# week 2/Day 9/encapsulation.py

class Student:
    school_name = "ABC Public School"  # class-level attribute

    def __init__(self, name, id_number):
        self.name = name              # public attribute
        self.__id_number = id_number  # private attribute

    # Getter method
    def get_id(self):
        return self.__id_number

    # Setter method with validation
    def set_id(self, new_id):
        if isinstance(new_id, int) and 1000 <= new_id <= 9999:
            self.__id_number = new_id
            print("ID updated successfully.")
        else:
            print("Invalid ID. Must be a 4-digit number.")

    # Instance method
    def study(self, subject):
        print(f"{self.name} is studying {subject}")

    # Class method
    @classmethod
    def school_info(cls):
        print(f"School Name: {cls.school_name}")


# ------------------ Testing ------------------

# Public vs Private
student1 = Student("Albin", 1234)
print(student1.name)  # Works fine

# Accessing private data directly (will raise AttributeError)
try:
    print(student1.__id_number)
except AttributeError as e:
    print("Error:", e)

# Using Getter and Setter
print("Current ID:", student1.get_id())
student1.set_id(5678)   # Valid update
print("Updated ID:", student1.get_id())
student1.set_id(12)     # Invalid update

# Instance method
student1.study("Python")

# Class method
Student.school_info()
