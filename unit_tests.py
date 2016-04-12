import sys
import unittest
from main import ToDoList
from PyQt5 import QtWidgets, QtGui, QtTest, QtCore

app = QtWidgets.QApplication(sys.argv)

class ToDoListTest(unittest.TestCase):

    def setUp(self):
        self.form = ToDoList()

    def testUrgentList(self):
        #total 1 item in list at beginning
        self.assertEqual(self.form.ui.urgent.count(), 1)

        #add item on clic Add Task
        self.form.UrgentListEdit(self.form.ui.urgent.item(0))
        self.assertEqual(self.form.ui.urgent.count(), 2)

        #enabled to edit on click to task
        self.form.UrgentListEdit(self.form.ui.urgent.item(1))
        self.assertEqual(self.form.ui.urgent.item(1).flags(), QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable)
        self.assertEqual(self.form.ui.urgent.item(1).isSelected(),True)
        self.assertEqual(self.form.ui.urgent.count(), 2)

        #delete item on Delete press
        QtTest.QTest.keyClick(self.form, QtCore.Qt.Key_Delete )
        self.assertEqual(self.form.ui.urgent.count(), 1)

        #clear list on clear button click
        self.form.UrgentListEdit(self.form.ui.urgent.item(0))
        self.form.UrgentListEdit(self.form.ui.urgent.item(0))
        self.form.UrgentListEdit(self.form.ui.urgent.item(0))
        self.form.UrgentListEdit(self.form.ui.urgent.item(0))
        self.form.UrgentListEdit(self.form.ui.urgent.item(0))
        self.form.clearList()
        self.assertEqual(self.form.ui.urgent.count(), 1)

        #can`t remove add task item
        self.form.UrgentListEdit(self.form.ui.urgent.item(0))
        QtTest.QTest.keyClick(self.form, QtCore.Qt.Key_Delete )
        self.assertEqual(self.form.ui.urgent.count(), 1)

if __name__ == '__main__':
    unittest.main()