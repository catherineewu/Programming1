import time
import login_system_exception_handling
import login_system
import unittest


class Tester:
    class_value = 50

    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2

    @classmethod  # Simple class method, can reference all class attributes with cls as first argument
    def value_of_class(cls):
        print(f'The value of this class is {cls.class_value}.')
        return cls.class_value

    @classmethod
    def change_class_value(cls, change):  # Class method with one EXTERNAL parameter change
        print(f'Value of class changed from {cls.class_value} to {change + cls.class_value}.')
        cls.class_value += change
        return cls.class_value

    @classmethod  # FACTORY METHOD: creates and returns new class object/instance
    def new_tester_class(cls, v1, v2):
        return cls(v1, v2)

    def put_together(self, additional):  # Instance method
        return self.v1 + self.v2 + additional


class InnerTester(Tester):
    def __init__(self, v1, v2, v3):
        Tester.__init__(self, v1, v2)
        self.v3 = v3

    @classmethod  # Class method that references base class attribute of class_value
    def replace_class_value(cls, new_value):
        print(f'Original class value of {cls.class_value} replaced with {new_value}.')
        cls.class_value = new_value
        return cls.class_value

    @staticmethod
    def print_a_countdown(seconds):
        for i in range(seconds, -1, -1):
            print(i, end=' ')
            time.sleep(1)
        print()

    def put_together_3(self, v1, v2, v3):
        return self.v1 + self.v2 + self.v3


class InnermostTester(InnerTester):
    def __init__(self, v1, v2, v3, v4):
        InnerTester.__init__(self, v1, v2, v3)
        self.v4 = v4

    def add_all_values(self):
        return self.v1 + self.v2 + self.v3 + self.v4


def main():
    cl = Tester.new_tester_class(10, 20)
    print(cl.put_together(5))

    while True:
        print('\nMENU:\n\t1. Countdown\n\t2. Value of Class (Static, Base)\n\t3. Add to Value of Class (Class, Base)'
              '\n\t4. Replace Value of Class (Class, InnerClass)\n\t5. Quit\n')
        option = input('Menu selection: ')
        if option == '1':
            countdown_time = int(input('Enter countdown time: '))
            InnerTester.print_a_countdown(countdown_time)
        elif option == '2':
            class_value = Tester.value_of_class()
        elif option == '3':
            added_value = int(input('Enter additional value of class (accepts negative): '))
            class_value = Tester.change_class_value(added_value)
        elif option == '4':
            replacement_value = int(input('Enter new value of class: '))
            class_value = InnerTester.replace_class_value(replacement_value)
        elif option == '5':
            break
        else:
            print('Invalid menu selection. Returning to menu.\n')

    InnerTester.print_a_countdown('two')
    instance1 = Tester(3, 4)
    print(f'Tester put_together: {instance1.put_together(10)}')
    InnerTester.print_a_countdown(3)
    instance2 = InnerTester(1, 2, 3)
    print(f'InnerTester countdown static: ', end='')
    instance2.print_a_countdown(5)


'''
def main():
    from datetime import date

    # random Person
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        @classmethod
        def fromBirthYear(cls, name, birthYear):
            return cls(name, date.today().year - birthYear)

        def display(self):
            print(self.name + "'s age is: " + str(self.age))

    person = Person('Adam', 19)
    person.display()

    person1 = Person.fromBirthYear('John', 1985)
    person1.display()
'''

if __name__ == '__main__':
    main()
