class SchoolMember:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


class Teacher(SchoolMember):
    def __init__(self, first_name, last_name, salary,position,your_class):
        super().__init__(first_name, last_name)
        self.salary = salary
        self.position = position
        self.your_class=your_class

    def tell(self):
        print(f"Вчитель: {self.first_name} {self.last_name},\n Зарплата: {self.salary},\n Посада: {self.position},\n Свій клас: {self.your_class}")


class Student(SchoolMember):
    def __init__(self, first_name, last_name, grades,classs):
        super().__init__(first_name, last_name)
        self.grades = grades
        self.classs=classs

    def average_grade(self):
        return sum(self.grades) / len(self.grades)

    def tell(self):
        average = self.average_grade()
        print(f"Учень: {self.first_name} {self.last_name},\n середній бал: {average:.2f},\n Клас {self.classs}")


teacher1 = Teacher("Ліля", "Синишин", 6700, 'Вчитель української мови','кірівник класу 10-A')
teacher2 = Teacher("Оксана", "Цура", 20000,'Деректор','Дура тупа яка мені префаєром ставила мені 1 з алгебри')
teacher3 = Teacher("Олена", "не пам'ятаю", 6700,'Вчитель Зарубіжної літератури','кірівник класу 11-А')


student1 = Student("Саня", "Кругліков", [1, 12, 3, 7],'11-b')
student2 = Student("Остап", "Крочак", [12, 12, 12, 12],'10-a')

teacher1.tell()
teacher2.tell()
student1.tell()
student2.tell()
