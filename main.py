from time import time
from random import randint
print("Task 1".center(170, "="))
# Створіть функцію, що повертає список з усіма простими числами від 0 до 1000.
# Використовуючи механізм декораторів порахуйте скільки секунд знадобилося для обчислення всіх простих чисел.
# Відобразіть на екран кількість секунд і прості числа.

def decorator(func):
    def wrapper():
        start_time = time()
        func()
        print()
        end_time = time()
        print(f"You spent {end_time - start_time} seconds.")
    return wrapper

def is_prime(n):
    if n <= 2:
        return False
    for i in range(2, int(n**(1/2))+1):
        if n % i == 0:
            return False
    return True

@decorator
def prime_in_range(start=0, end=1000):
    c = 0
    for n in range(start, end):
        if is_prime(n):
            print(str(n).rjust(3), end=" ")
            c += 1
            if c % 42 == 0:
                print()

prime_in_range()

#Додайте до першого завдання можливість передавати межі діапазону для пошуку всіх простих чисел.
print("Task 2".center(170, "="))
def use_range(start, end):
    def decorator(func):
        def wrapper():
            return func(start, end)
        return wrapper
    return  decorator
@decorator
@use_range(100, 250)
def prime_in_range(start=0, end=1000):
    c = 0
    for n in range(start, end):
        if is_prime(n):
            print(str(n).rjust(3), end=" ")
            c += 1
            if c % 42 == 0:
                print()

prime_in_range()

print("Task 3".center(170, "="))
#Щороку ваша компанія надає різним державним організаціям фінансову звітність.
#Залежно від організації формати звітності різні.
#Використовуючи механізм декораторів, розв'яжіть питання звітності для організацій
base_data = {"field"+str(i): randint(1000, 1000_000) for i in range(1, 11) }
print(base_data)


class Company:
    def __init__(self):
        self.fields = {
        'count_employee' : 100,
        'avg_salary' : 10_000,
        'seo_salary' : 100_000,
        'count_women' : 405,
        }

    def get_report(self):
        return self.fields

    def print_report(self):
        for field in self.fields:
            print(f'{field}: {self.fields[field]}')

def add_field(field_name):
    def decorator(func):
        def wrapper(company):
            company.fields[field_name] = base_data[field_name]
            return func(company)
        return wrapper
    return decorator

company1 = Company()
'''
print(company1.get_report())
@add_field("field2")
def nalogovaya(company1):
    return company1.get_report()

print(nalogovaya(company1))
'''
@add_field("field4")
@add_field("field7")
@add_field("field9")
def print_report_for_org1(company):
    company.print_report()

print("Print report for org1:")
print_report_for_org1(company1)
print()

company2 = Company()
@add_field("field2")
@add_field("field3")
@add_field("field10")
def print_report_for_org2(company):
    company.print_report()

print("Print report for org2:")
print_report_for_org2(company2)
print()