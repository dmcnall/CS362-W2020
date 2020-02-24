# !/usr/local/bin/python
# -*- coding: utf-8 -*-
import sys, os
import unittest
from classroom_manager import Student
from classroom_manager import Assignment 

class testStudent(unittest.TestCase):
    
    def test_Init(self):
        self.Student1 = Student(1, "John", "Smith")
     #   self.Student2 = Student(2, "Dave", "Johnson")
        self.assertEqual(len(self.Student1.assignments), 0)

    def test_FullName(self):
         self.Student1 = Student(1, "John", "Smith")

         self.assertEqual("John,Smith", self.Student1.get_full_name)
     #   self.assertEqual("Dave,Johnson", self.Student2.get_full_name)
    
    def test_submit_assignment(self):
        self.Student1.assignment1 = Assignment("assignment1", 40)
        self.Student1.assignment1.assign_grade(16)
        self.Student1.assignment2 = Assignment("assignment2", 50)
        self.Student1.assignment2.assign_grade(14)
        self.assertEqual(2, len(self.Student1.submit_assignment))

    def test_get_assignments(self):
        self.assertNotEqual(0, len(self.Student1.get_assignments))

    def test_get_assignment(self):
        self.assertEqual("assignment1", self.Student1.get_assignment("assignment1"))
    
    def test_get_Average(self):
        self.assertEqual(15, self.Student1.get_average)
    
    def test_remove_assignment(self):
        self.Student1.remove_assignment("assignment1")
        self.assertNotIn("assignment1", self.Student1.assignments)

class testAssignment(unittest.TestCase):
    
    def test_Init2(self):
        self.assignmentTest1 = Assignment("Essay1", 41)
        self.assignmentTest2 = Assignment("Essay2", 14)
        self.assertEqual(-1, self.assignmentTest1.grade)
        self.assertEqual(-1, self.assignmentTest2.grade)

    def test_assign_grade(self):
        self.assignmentTest1 = Assignment("Essay1", 41)
        self.assignmentTest2 = Assignment("Essay2", 14)

        self.assertEqual(self.assignmentTest1.assign_grade(30),30)
        self.assertEqual(self.assignmentTest1.assign_grade(15),-1)
        self.assertEqual(self.assignmentTest2.assign_grade(12), 12)

if __name__ == '__main__':
    unittest.main()