import sys
from PyQt4 import QtGui

newNum = 0
extNum = 0
result = 0

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
                button.clicked.connect(self.btnNum)
            elif name == '=':
                button.clicked.connect(self.btnEq)
            else:
                button.clicked.connect(self.btnOp)
        
        self.line = QtGui.QLineEdit()
        grid.addWidget(self.line, 5, 0)

        self.move(300, 150)
        self.setWindowTitle('Calculator')
        self.show()

    def btnNum(self):
        global newNum

        sender = self.sender()
        newNum = sender.text()

        if self.line.text() == "":
            self.line.setText(newNum)
        else:
            self.line.setText(self.line.text() + newNum)
    
    def btnOp(self):
        global newNum
        global extNum
        global funC

        funC = self.sender()
        extNum = newNum
        self.line.clear()

    def btnEq(self):
        global newNum
        global extNum
        global result
        global funC

        if funC.text() == '+':
            result = int(extNum) + int(newNum)                 
        elif funC.text() == '-':
            result = int(extNum) - int(newNum)
        elif funC.text() == '*':
            result = int(extNum) * int(newNum)
        elif funC.text() == '/':
            result = int(extNum) / int(newNum)

        self.line.setText(str(result))


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
