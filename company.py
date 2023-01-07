"""
Program: company.py
Author: Stavros Batsinelas
Date: 1/13/2021

This file defines classes "Customer" and "Employee". The base class
"Person" is imported from person.py, and is inherited by the classes.
Unique instance variables are created for each class with accessor and
mutator methods. The __str__() method is then overrided so it will format
and return the information. The classes can now be imported by
test_company.py to display profile information for customers and employees
of a company. 
"""

from person import Person

# define subclass Person of class Customer
class Customer(Person):

    #constructor
    def __init__(self, name, address, phone, credit_score):

        #inherit elements of Person
        Person.__init__(self, name, address, phone)

        #initialize credit score
        self.credit_score = credit_score

    # getter for credit score
    def get_credit_score(self):
        return self.credit_score

    # setter for credit score
    def set_credit_score(self, credit_score):
        self.credit_score = credit_score

    # override __str__()
    def __str__(self):        
        return "name:         " + str(self.name) + \
               "\naddress:      " + str(self.address) + \
               "\nphone:        " + str(self.phone) + \
               "\ncredit_score: " + str(self.credit_score)


# define subclass Person of class Employee
class Employee(Person):
    
    # constructor, initialize elements of Employee
    def __init__(self, name, address, phone, badge, salary):        

        #inherit elements of Person
        Person.__init__(self, name, address, phone)

        #initialize badge and salary
        self.badge = badge
        self.salary = salary

    # getter for badge and salary
    def get_badge(self):
        return self.badge

    def get_salary(self):
        return self.salary

    # setter for badge and salary
    def set_badge(self, badge):
        self.badge = badge

    def set_salary(self, salary):
        self.salary = salary

    # override __str__()
    def __str__(self):        
        return "name:         " + str(self.name) + \
               "\naddress:      " + str(self.address) + \
               "\nphone:        " + str(self.phone) + \
               "\nbadge:        " + str(self.badge)

    # define __eq__()
    def __eq__(self, other):
        
        # return equality of badge number
        return self.badge == other.badge
