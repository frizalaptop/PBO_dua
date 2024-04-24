class Klinik:
    def __init__(self):
        self.employee = None
        self.dept = None

    def getData(self, employee, dept):
        self.employee = employee
        self.dept = dept

    def staffData(self):
        print(f"Name: {self.employee}\nDept: {self.dept}")

staff = Klinik()
employee = input("Nama Pegawai : ")
dept = input("Departement : ")

staff.getData(employee, dept)
staff.staffData()