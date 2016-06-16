import sys
from PyQt4 import QtGui

class Example(QtGui.QMainWindow):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

#Creat all numbers step by step    
    def initUI(self):
        """Button setting"""
        self.btn0 = QtGui.QPushButton('0', self)
        self.btn0.resize(50, 40)
        self.btn0.move(70, 250)

        self.btn1 = QtGui.QPushButton('1', self)
        self.btn1.resize(50, 40)
        self.btn1.move(10, 200)
        
        self.btn2 = QtGui.QPushButton('2', self)
        self.btn2.resize(50, 40)
        self.btn2.move(70, 200)

        self.btn3 = QtGui.QPushButton('3', self)
        self.btn3.resize(50, 40)
        self.btn3.move(130, 200)

        self.btn4 = QtGui.QPushButton('4', self)
        self.btn4.resize(50, 40)
        self.btn4.move(10, 150)

        self.btn5 = QtGui.QPushButton('5', self)
        self.btn5.resize(50, 40)
        self.btn5.move(70, 150)

        self.btn6 = QtGui.QPushButton('6', self)
        self.btn6.resize(50, 40)
        self.btn6.move(130, 150)

        self.btn7 = QtGui.QPushButton('7', self)
        self.btn7.resize(50, 40)
        self.btn7.move(10, 100)

        self.btn8 = QtGui.QPushButton('8', self)
        self.btn8.resize(50, 40)
        self.btn8.move(70, 100)

        self.btn9 = QtGui.QPushButton('9', self)
        self.btn9.resize(50, 40)
        self.btn9.move(130, 100)

        self.btnCE = QtGui.QPushButton('CE', self)
        self.btnCE.resize(50, 40)
        self.btnCE.move(10, 50)

        self.btnC = QtGui.QPushButton('C', self)
        self.btnC.resize(50, 40)
        self.btnC.move(70, 50)

        self.btnBck = QtGui.QPushButton('<-', self)
        self.btnBck.resize(50, 40)
        self.btnBck.move(130, 50)

        self.btnDiv = QtGui.QPushButton('/', self)
        self.btnDiv.resize(50, 40)
        self.btnDiv.move(190, 50)

        self.btnMul = QtGui.QPushButton('*', self)
        self.btnMul.resize(50, 40)
        self.btnMul.move(190, 100)

        self.btnSub = QtGui.QPushButton('-', self)
        self.btnSub.resize(50, 40)
        self.btnSub.move(190, 150)

        self.btnAdd = QtGui.QPushButton('+', self)
        self.btnAdd.resize(50, 40)
        self.btnAdd.move(190, 200)

        self.btnEqual = QtGui.QPushButton('=', self)
        self.btnEqual.resize(50, 40)
        self.btnEqual.move(190, 250)

        self.btnSwitch = QtGui.QPushButton('+/-', self)
        self.btnSwitch.resize(50, 40)
        self.btnSwitch.move(10, 250)

        self.btnDot = QtGui.QPushButton('.', self)
        self.btnDot.resize(50, 40)
        self.btnDot.move(130, 250)


        # self.btn1.clicked.connect(self.btn1)
        # self.btn2.clicked.connect(self.btn2)
        # self.btn3.clicked.connect(self.plus)
        # self.btn4.clicked.connect(self.equal)

        self.le = QtGui.QLineEdit(self)
        self.le.setReadOnly(True)
        self.le.resize(230, 30)
        self.le.move(10, 10)

        self.setGeometry(300, 300, 250, 300)
        self.setWindowTitle('Calculator')
        self.show()

def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
