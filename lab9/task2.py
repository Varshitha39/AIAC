class sru_student:
    """
    A class representing a student at SRU.

    Attributes:
        name (str): The name of the student.
        roll_no (str): The roll number of the student.
        hostel_status (str): The hostel status of the student.
        fee_paid (bool): Indicates whether the student's fee has been paid.

    Methods:
        __init__(name, roll_no, hostel_status):
            Initializes a new sru_student instance with the given name, roll number, and hostel status.
            Sets fee_paid to False by default.

        fee_update(status):
            Updates the fee_paid status for the student.

        display():
            Prints the student's details including name, roll number, hostel status, and fee payment status.
    """
    def __init__(self,name,roll_no,hostel_status):
        # Assign the student's name
        self.name = name
        # Assign the student's roll number
        self.roll_no = roll_no
        # Assign the student's hostel status
        self.hostel_status = hostel_status
        # Initialize fee_paid as False (not paid by default)
        self.fee_paid = False

    def fee_update(self,status):
        # Update the fee_paid attribute with the given status (True or False)
        self.fee_paid

    def display(self):
        # Print the student's name
        print(f"Name:{self.name}")
        # Print the student's roll number
        print(f"Roll No:{self.roll_no}")
        # Print the student's hostel status
        print(f"Hostel Status:{self.hostel_status}")
        # Print whether the student's fee has been paid
        print(f"Fee Paid:{'Yes' if self.fee_paid else 'No'}")
            
# Create a new student object with name "Alice", roll number 101, and hostel status "Yes"
student1 = sru_student("Alice", 101, "Yes")
# Update the fee status for the student to True (fee paid)
student1.fee_update(True)
# Display the student's details
student1.display()
