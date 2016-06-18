import sys
from PyQt4 import QtGui, QtCore

cnt = 0
result = 0

class Form(QtGui.QWidget):
    def __init__(self):
        super(Form, self).__init__()
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
            elif name == 'Close':
                button.clicked.connect(QtCore.QCoreApplication.instance().quit)
            elif name == 'Cls':
                button.clicked.connect(self.btnCls)
            elif name == 'Bck':
                button.clicked.connect(self.btnBck)
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
            newNum = self.line.text() + newNum
            self.line.setText(newNum)
    
    def btnOp(self):
        global newNum, extNum, funC

        funC = self.sender()
        extNum = newNum
        self.line.clear()

    def btnEq(self):
        global newNum, extNum, result, funC, cnt
        
        if cnt == 0:
            result = int(extNum)

        if funC.text() == '+':
            result += int(newNum)
        elif funC.text() == '-':
            result -= int(newNum)
        elif funC.text() == '*':
            result *= int(newNum)
        elif funC.text() == '/':
            result /= int(newNum)

        self.line.setText(str(result))
        cnt += 1

    def btnCls(self):
        global result, newNum, extNum, cnt

        newNum = 0
        extNum = 0
        result = 0
        cnt = 0
        self.line.clear()
    
    def btnBck(self):
        # '='가 입력된 이후에는 작동하지않도록 설정
        global newNum

        self.line.backspace()
        newNum = self.line.text()

def main():
    app = QtGui.QApplication(sys.argv)
    f = Form()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

'''수정해야할 것
1. Bck 한 이후의 숫자를 갖도록 하자. (ok)
2. 

'''
