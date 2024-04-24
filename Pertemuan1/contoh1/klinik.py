class Klinik:
    def __init__(self, employee, dept):
        self.employee = employee
        self.dept = dept

    def staffData(self):
        print(f"Name: {self.employee}\nDept: {self.dept}")

staff = Klinik("Friza", "IT")
staff.staffData()