import sys
import os

src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../src'))
sys.path.append(src_path)

from employee import Employee
import employee_manager
import datetime
from relations_manager import RelationsManager

emp_manager=employee_manager.EmployeeManager(RelationsManager())

def test_calculate_salary():
    employee=Employee(id=7, first_name="John", last_name="Walker", base_salary=1000,
                     birth_date=datetime.date(1970, 1, 31), hire_date=datetime.date(1998, 10, 10))  #1998
    salary=emp_manager.calculate_salary(employee)
    assert salary==3000

def test_calculate_salary_leader():
    employee=Employee(id=8, first_name="Marty", last_name="Byrde", base_salary=2000,
                     birth_date=datetime.date(1970, 1, 31), hire_date=datetime.date(2008, 10, 10))  #2008
    salary=emp_manager.calculate_salary(employee)
    assert salary==3600

def test_send_email():
    employee=Employee(id=9, first_name="Joseph", last_name="White", base_salary=1500,
                     birth_date=datetime.date(1970, 1, 31), hire_date=datetime.date(2008, 10, 5))  #2008
    output=emp_manager.calculate_salary_and_send_email(employee)
    message=output.split(" ")
    for i in range(0,len(message)):
        if i==0:
            assert message[i] == "Joseph"
        elif i==1:
            assert message[i] == "White"
        elif i==2:
            assert message[i] == "3100"
        else:
            break




