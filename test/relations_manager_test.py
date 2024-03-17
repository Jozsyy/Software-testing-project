import sys
import os

src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../src'))
sys.path.append(src_path)

import relations_manager
from employee import Employee
import datetime

rel_manager=relations_manager.RelationsManager()

def test_is_leader():
    employee1=Employee(id=1, first_name="John", last_name="Doe", base_salary=3000,
                     birth_date=datetime.date(1970, 1, 31), hire_date=datetime.date(1990, 10, 1))
    output=rel_manager.is_leader(employee1)
    assert output == True

def test_get_team_members():
    employee1=Employee(id=1, first_name="John", last_name="Doe", base_salary=3000,
                     birth_date=datetime.date(1970, 1, 31), hire_date=datetime.date(1990, 10, 1))
    output=rel_manager.get_team_members(employee1)
    assert output==[2, 3]
    assert output!=[5]

def test_calculate_salary():
    employee_list=rel_manager.get_all_employees()
    output=False
    for employee in employee_list:
        if employee.first_name=="Gretchen" and employee.last_name=="Watford" and employee.base_salary==4000:
            output=True
    assert output==True
   
def test_not_team_leader():
    empolyee=Employee(id=5, first_name="Tomas", last_name="Andre", base_salary=1600,
                     birth_date=datetime.date(1995, 1, 1), hire_date=datetime.date(2015, 1, 1))
    output=rel_manager.is_leader(empolyee)
    assert output==False
    out2=rel_manager.get_team_members(empolyee)
    assert out2==None

def test_get_all_employees():
    employee_list=rel_manager.get_all_employees()
    output=False
    for employee in employee_list:
        if employee.first_name=="Jude" and employee.last_name=="Overcash":
            output=True
    assert output==False