from PyQt5 import QtWidgets, QtGui
import sys
from main_window_design import Ui_MainWindow

class ToDoList(QtWidgets.QMainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #initial set up
        self.ui.urgent.addItem("Add task")

        #connect signals to slots
        self.ui.urgent.itemClicked.connect(self.UrgentListEdit)
    
    #list edits
    def UrgentListEdit(self, item):
        if( item.text() == "Add task" ):
            item = "New task " + str(self.ui.urgent.count())
            self.ui.urgent.addItem(item) 

def main():
    app = QtWidgets.QApplication(sys.argv)
    myapp = ToDoList()
    myapp.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()