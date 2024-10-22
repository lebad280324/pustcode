class Employee:
    def __init__(self,name,age,gmail):
        self.name = name
        self.age = age
        self.gmail = gmail

    def full_name(self):
        return '{} {}'.format(self.name,self.age)

    def gmai(self,fist,last):
        self.fist = fist
        self.last = last
        self.gmail = self.fist + self.last + '@gmail.com'
        return self.gmail

    def in_ra(self):
        return (f'ten: {self.name}, tuoi: {self.age}, gmail: {self.gmail}')

emp = Employee("dung",32,None)
emp.gmai('dung','leba')
print(emp.in_ra())


class Develomen(Employee):
    def __init__(self,name,age,gmail):
        super().__init__(name,age,gmail)

    def show(self):
        pea = super().in_ra()
        return pea

i = Develomen('long',12,None)
i.gmai('long','meo')
print(i.show())


class Manager(Employee):
    def __init__(self,name,age,gmai):
        super().__init__(name,age,gmai)

    def show(self,quanly):
        in_ra = f"{super().in_ra()} ,so nguoi quan ly:{quanly}, "
        return in_ra

hehe = Manager("manh",22,None)
hehe.gmai("manh","mongmanh")
print(hehe.show(43))