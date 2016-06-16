import sys
from PyQt4 import QtGui

class Example(QtGui.QMainWindow):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

#Creat all numbers step by step    
    def initUI(self):
        #Button setting
        grid = QtGui.QGridLayout()
        self.setLayout(grid)

        names = ['Cls', 'Bck', '', 'Close',
                '7', '8', '9', '/',
                '4', '5', '6', '*',
                '1', '2', '3', '-',
                '0', '.', '=', '+']
        
        positions = [(i, j) for i in range(5) for j in range(4)]

        for position, name in zip(positions, names):
            if name == '':
                continue
            button = QtGui.QPushButton(name)
            grid.addWidget(button, *position)

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
