def cross_join(employees, departments):
    """
    Реализует декартово произведение списков employees и departments

    :param employees: Список LastName сотрудников таблицы Employee
    :param departments: Список DepartmentName таблицы Department
    :return: Генератор пар (LastName, DepartmentName)
    """

    i_max = len(employees)
    j_max = len(departments)

    for i in range(i_max):
        for j in range(j_max):
            yield employees[i], departments[j]
