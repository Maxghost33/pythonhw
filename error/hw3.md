1. Modify your department:
    * change giving salary method: if there is not Employee in manager's team, raise SalaryGivingError(You should create the Error class)
    * Add method add_to_team(array) to manager class, which adds employees to team. If there are not Employees in array, raise your own NotEmployeeException and if Employee is Manager, reise `WrongEmployeeRoleError` with parameter `"second_name"`. String representation of error should return message `"Employee @second_name@ has unexpected role!"`
    * In Department class create method add_team_members(manager, array) which tries to add array of Employees to manager team. Handle the exceptions, raised in manager's add_to_team method.

2. Cover your basics task functions with unit tests. (Possible to use `setUp()` while testing)
