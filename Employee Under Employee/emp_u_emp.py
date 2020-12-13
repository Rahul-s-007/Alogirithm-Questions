# refrence: https://www.techiedelight.com/find-employees-who-reports-to-manager/

# Recursive DP function to find all employees who directly or indirectly
# reports to a given manager and store the result in the result dict
def findAllReportingEmployees(manager, managerToEmployeeMappings, result):
 
    # if the sub-problem is already seen before
    if manager in result:
        # return the already computed mapping
        return result.get(manager)
 
    # find all employees reporting directly to the current manager
    managerEmployees = managerToEmployeeMappings.get(manager)
 
    if managerEmployees:
        # find all employees reporting in-directly to the current manager
        for reportee in managerEmployees.copy():
            # find all employees reporting to the current employee
            employees = findAllReportingEmployees(reportee, managerToEmployeeMappings,
                                                result)
 
            # move those employees to the current manager
            if employees:
                managerEmployees.extend(employees)
 
    # save the result to avoid re-computation and return it
    result[manager] = managerEmployees
    return managerEmployees
 
 
# Find all employees who directly or indirectly reports to a manager
def findEmployees(employeeToManagerMappings):
 
    # store manager to employee mappings in a dict
    # is used since a manager can have several employees mapped
    managerToEmployeeMappings = {}
 
    # fill above dict with the manager to employee mappings
    for employee, manager in employeeToManagerMappings.items():
        # don't map an employee with itself
        if employee != manager:
            managerToEmployeeMappings.setdefault(manager, []).append(employee)
 
    # construct an ordered dict to store the result
    result = {}
 
    # find all reporting employees (direct and indirect) for every manager
    # and store the result in a dict
    for key in employeeToManagerMappings.keys():
        findAllReportingEmployees(key, managerToEmployeeMappings, result)
 
    # print contents of the result dict
    for key, value in result.items():
        print(key, "->", value)
 
 
if __name__ == '__main__':
 
    # construct a dictionary of employee to manager mappings
    employeeToManagerMappings = {'A': 'A', 'B': 'A', 'C': 'B',
                                'D': 'B', 'E': 'D', 'F': 'E'}
    findEmployees(employeeToManagerMappings)