def addition_simplified(*args):
    return sum(args)

addition_simplified(1, 3, 4, 5, 6, 7)

def what_are_kwargs(*args, **kwargs):
    print(args)
    print(kwargs)

what_are_kwargs(12, 45, 66, name="test", target=30)

# named paramaters
def func(name, location):
    print(name)
    print(location)

func(location='VN', name='AAA')



class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)

    @classmethod
    def friend(cls, origin, friend_name, *args, **kwargs):
        return cls(friend_name, origin.school, *args, **kwargs)

class WorkingStudent(Student):
    def __init__(self, name, school, salary, job_title):
        super().__init__(name, school)
        self.salary = salary

anna = WorkingStudent("Anna", "Oxf", 20.00, "Dev")
print(anna.salary)
friend = WorkingStudent.friend(anna, "Greg", 90, job_title='PM')
print(friend.salary)

tom = Student("Tom", "HUA")
alice = Student.friend(tom, "Alice")
print(alice.name)