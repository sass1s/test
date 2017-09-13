#!/usr/bin/env python3
import sys
from collections import Counter


class Person(object):
    """
    返回具有给定名称的 Person 对象
    """

    def __init__(self, name):
        self.name = name

    def get_details(self):
        """
        返回包含人名的字符串
        """
        return self.name

    def get_grade(self):
        pass


class Student(Person):
    """
    返回 Student 对象，采用 name, branch, year 3 个参数
    """

    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade

    def get_grade(self):
        c = Counter(self.grade)
        r = c.most_common(4)
        pn = sum(x[1] for x in r if x[0] != 'D')
        fn = sum(x[1] for x in r if x[0] == 'D')
        print('Pass: {}, Fail: {}'.format(pn, fn))


class Teacher(Person):
    """
    返回 Teacher 对象，采用字符串列表作为参数
    """

    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade

    def get_grade(self):
        c = Counter(self.grade)
        r = c.most_common(4)
        s = ['{}: {}'.format(x[0], x[1]) for x in r]
        print(', '.join(s))


if __name__ == '__main__':
    str1 = sys.argv[1]
    str2 = sys.argv[2]
    if str1.startswith('tea'):
        Teacher(str1, str2).get_grade()
    if str1.startswith('stu'):
        Student(str1, str2).get_grade()
