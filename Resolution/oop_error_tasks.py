import os


class Error(Exception):
    def __init__(self):
        Exception.__init__(self)

class SalaryGivingError(Error):
    def __init__(self):
        Error.__init__(self)
        self.message = "Object does not exist in Employee and can`t give method give_salary()"
    
    def __str__(self):
        return "Object does not exist in Employee and  can`t give method give_salary()"

class NotEmployeeException(Error):
    def __init__(self):
        Error.__init__(self)
        self.message = "List does not exist type Employee"

    def __str__(self):
        return "Some arguments are not exist object type Employee"

class WrongEmployeeRoleError(Error):
    def __init__(self, second_name):
        Error.__init__(self)
        self.second_name = second_name
    def __str__(self):
        return "Employee " +  self.second_name + " has unexpected role!"


class Employee(object):
    def __init__(self, name, secname, salary, experiance):
        self.name = name
        self.secname = secname
        self.salary = salary
        self.exp = experiance

    def __str__(self):
        return self.name + " " + self.secname + ", manager: "
    
    def get_salary(self):
        if self.exp > 2 and self.exp < 5:
            self.salary = int(self.salary) + 200
        elif self.exp > 5:
            self.salary = int(self.salary)*1.2 +  500
        print (int(self.salary))
        return int(self.salary)
 
class developer(Employee):
    def __init__(self, name, secname, salary, experiance, man):
        super().__init__(name, secname, salary, experiance)
        self.hman = man


    def __str__(self):
        return super().__str__() + self.hman[0].name + ", experiance: " + str(self.exp)

class designer(Employee):
    def __init__(self, name, secname, salary, experiance, effcoeff, man):
        super().__init__(name, secname, salary, experiance)
        self.coeff = effcoeff
        self.hman = man
    def __str__(self):
        return super().__str__() + self.hman[0].name + ", experiance: " + str(self.exp)

    def get_salary(self):
        self.salary = super().get_salary()*self.coeff
        print (self.salary)
        return int(self.salary)


class manager(Employee):
    def __init__(self, name, secname, salary, experiance, man, team):
        super().__init__(name, secname, salary, experiance)
        self.hman = man
        self._team = team


    def __str__(self):
        return super().__str__() + self.hman[0].name + ", experiance: " + str(self.exp)

    def getteam (self):
        print(self._team)
        return self._team
    
    def setteam (self, members):
        count = 0
        for i in members:
            if type(i) not in (manager, designer, developer):
                count += 1
        try:
            if len(members) == 0 or count == len(members) or count > 0:
                raise NotEmployeeException
            for i in members:
                if type(i) == manager:
                    raise WrongEmployeeRoleError(i.secname)
        except NotEmployeeException as ex:
            print(ex.message)
        except WrongEmployeeRoleError:
            print(WrongEmployeeRoleError(i.secname))
        else:
            for i in members:
                self._team.append(i)
            return self._team
    
    def delteam(self):
        del self._team
    
    def get_salary(self):
        if len(self._team) > 5:
            self.salary = super().get_salary() + 200
        elif len(self._team) > 10:
            self.salary = super().get_salary() + 300
        elif sum(type(i) == developer for i in self._team) > len(self._team) / 2:
            self.salary = super().get_salary()*1.1
        print(int(self.salary))
        return (int(self.salary))
    
    teams = property(getteam, setteam, delteam, "property teams")



class department(object):
    def __init__(self, list):
       self._list = list
                
    
    def give_salary(self):
        try:
            for i in self._list:
                if type(i) not in (manager, designer, developer):
                    raise SalaryGivingError
        except SalaryGivingError as ex:
            print("Exception: " + ex.message)
        else:
            for i in self._list:
                print(i.name + " " + i.secname + ": got salary " + str(int(i.salary)))

    def setlist(self, value):
        self._list.extend(value)
        return self._list
    def add_to_team (self, m, t):
        m.teams = t
        self._list.append(m)
        for i in t:
            self._list.append(i)
        return self._list
 
    lists = property(fset = setlist, doc="property lists")

def main():
    Dep = department([])
    A = manager("Manager", "Cool", 1000, 10, [], [])
    D = designer("Web", "Designer", 1000, 10, 0.5, [A])
    B = developer("Max", "Zhovanik", 500, 2, [A])
    C = developer ("Max", "Goose", 500, 0.5, [A])
    S = "Error"
    Q = manager("Manager2", "Cool2", 10000, 10, [], [])
    F = developer("Ghost", "Goose", 550, 1, [Q])
    A.teams = [B, C, Q]
    A.get_salary()
    B.get_salary()
    C.get_salary()
    D.get_salary()
    Dep.add_to_team(A, [Q, C, F])
    Dep.lists = [Q, D, B, "AAA"]
    Dep.give_salary()


if __name__ == "__main__":
    main()
