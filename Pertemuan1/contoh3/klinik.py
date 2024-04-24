class Klinik:
    def __init__(self):
        self._employee = None
        self._dept = None

    @property
    def employee(self):
        return self._employee
    
    @employee.setter
    def employee(self, value):
        self._employee = value

    @property
    def dept(self):
        return self._dept
    
    @dept.setter
    def dept(self, value):
        self._dept = value

    def staffData(self):
        print(f"Name: {self.employee}\nDept: {self.dept}")

klinik = Klinik()
employee = input("Nama Pegawai : ")
dept = input("Departement : ")

klinik.employee = employee
klinik.dept = dept
klinik.staffData()