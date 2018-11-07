import os


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
        #print (int(self.salary))
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
        #print (self.salary)
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
        #print(int(self.salary))
        return (int(self.salary))
    
    teams = property(getteam, setteam, delteam, "property teams")



class department(object):
    def __init__(self, list):
       self._list = list
                
    
    def give_salary(self):
        for i in self._list:
            print(i.name + " " + i.secname + ": got salary " + str(int(i.salary)))

    def setlist(self, value):
        for i in value:
            self._list.append(i)
        return self._list

    lists = property(fset = setlist, doc="property lists")

def main():
    Dep = department([])
    A = manager("Manager", "Cool", 1000, 10, [], [])
    D = designer("Web", "Designer", 1000, 10, 0.5, [A])
    B = developer("Max", "Zhovanik", "500", 2, [A])
    C = developer ("Max", "Goose", "500", 0.5, [A])
    A.teams = [B, C, D]
    A.get_salary()
    B.get_salary()
    C.get_salary()
    D.get_salary()
    Dep.lists = [A, B, C, D]
    Dep.give_salary()
    print(B)
if __name__ == "__main__":
    main()
