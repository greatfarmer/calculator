import sys
from PyQt4 import QtGui

class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        #Button setting
        grid = QtGui.QGridLayout()
        self.setLayout(grid)

        names = ['Cls', 'Bck', '', 'Close',
                '7', '8', '9', '/',
                '4', '5', '6', '*',
                '1', '2', '3', '-',
                '.', '0', '=', '+']
        
        positions = [(i, j) for i in range(5) for j in range(4)]

        for position, name in zip(positions, names):
            if name == '':
                continue
            button = QtGui.QPushButton(name)
            grid.addWidget(button, *position)

            if name.isdigit() == True:
                button.clicked.connect(self.btnClicked)
        
        self.line = QtGui.QLineEdit()

        grid.addWidget(self.line, 5, 0)

        # self.btn1.clicked.connect(self.btn1)
        # self.btn2.clicked.connect(self.btn2)
        # self.btn3.clicked.connect(self.plus)
        # self.btn4.clicked.connect(self.equal)

        self.move(300, 150)
        self.setWindowTitle('Calculator')
        self.show()

    def btnClicked(self):
        sender = self.sender()
        self.line.setText(sender.text())

def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
