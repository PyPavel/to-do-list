import sys
import unittest
from main import ToDoList
from PyQt5 import QtWidgets, QtGui, QtTest, QtCore

app = QtWidgets.QApplication(sys.argv)

class ToDoListTest(unittest.TestCase):

    def setUp(self):
        self.form = ToDoList()

    def testAddEmptyItemToListOnClick(self):
        self.assertEqual(self.form.ui.urgent.count(), 1)

        self.form.UrgentListEdit(self.form.ui.urgent.item(0))
        self.assertEqual(self.form.ui.urgent.count(), 2)

        self.form.UrgentListEdit(self.form.ui.urgent.item(1))
        self.assertEqual(self.form.ui.urgent.count(), 2)

    def testEditItem(self):
        QtTest.QTest.keyClicks(self.form.ui.urgent.item(1), "Edit task 1")
        self.assertEqual(self.form.ui.urgent.item(1).text(), "Edit task 1")

if __name__ == '__main__':
    unittest.main()