#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Person:
    # __init__是类的构造函数
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# 单继承
class Man(Person):
    def __init__(self, name, age):
        Person.__init__(self, name, age) # 单继承的构造方法需要用父类名调用
        self.gender = 'man'
    # 重写父类的方法
    def say_hello(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old, I am {self.gender}.")

class Employee(Person):
    def __init__(self, name, age, salary):
        Person.__init__(self,name, age)
        self.salary = salary

    def say_hello(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old, and my salary is {self.salary}.")

# 多继承
class MaleEmployee(Man, Employee):
    def __init__(self, name, age, salary):
        Man.__init__(self, name, age) # 多继承的构造方法需要用父类名调用
        self.salary = salary

    def say_hello(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old, I am {self.gender}, and my salary is {self.salary}.")

# 实例化对象
person = Person('Zack', 25)
man = Man('Jack', 30)
employee = Employee('Tom', 35, 5000)
male_employee = MaleEmployee('Jane', 40, 6000)


# 调用方法
person.say_hello()
man.say_hello()
employee.say_hello()
male_employee.say_hello()

#调用父类被重写的方法
super(Employee, male_employee).say_hello()