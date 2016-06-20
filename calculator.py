import sys
from PyQt4 import QtGui, QtCore

cnt = 0
numCnt = 0
eqCnt = False
opCnt = False
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
        self.line.setReadOnly(True)
        grid.addWidget(self.line, 5, 0)

        self.label = QtGui.QLabel()
        grid.addWidget(self.label, 5, 1)

        self.move(300, 150)
        self.setWindowTitle('Calculator')
        self.show()

    def btnNum(self):
        global newNum, extNum, result, funC, cnt, numCnt, eqCnt, opCnt

        if eqCnt == True and opCnt == False:
            self.btnCls()

        sender = self.sender()
        newNum = sender.text()

        if self.line.text() == "":
            if newNum == '0':
                return
            else:
                self.line.setText(newNum)
        else:
            newNum = self.line.text() + newNum
            self.line.setText(newNum)

        self.label.setText(self.label.text() + sender.text())
        
        eqCnt = False
        opCnt = False

        print("newNum =", newNum) 

    def btnOp(self):
        global newNum, extNum, result, funC, cnt, numCnt, eqCnt, opCnt

        funC = self.sender().text()
        extNum = newNum
        self.line.clear()
        self.label.setText(self.label.text() + funC)

        numCnt += 1
        opCnt = True

        if numCnt > 1:
            self.cal()
        
        print("Oper =", funC)
        print("extNum =", extNum)
        print("result =", result)        
    
    def cal(self):
        global newNum, extNum, result, funC, cnt, numCnt, eqCnt, opCnt

        if cnt == 0:
            result = int(extNum)

        if funC == '+':
            result += int(newNum)
        elif funC == '-':
            result -= int(newNum)
        elif funC == '*':
            result *= int(newNum)
        elif funC == '/':
            if int(newNum) == 0:
                result = "0으로 나눌 수 없습니다."
            else:
                result /= int(newNum)

        cnt += 1

    def btnEq(self):
        global newNum, extNum, result, funC, cnt, numCnt, eqCnt, opCnt

        self.cal()

        numCnt = 0
        eqCnt = True

        self.line.setText(str(result))
        self.label.clear()

        print("final result =", result)

    def btnCls(self):
        global newNum, extNum, result, funC, cnt, numCnt, eqCnt, opCnt

        newNum = 0
        extNum = 0
        result = 0
        cnt = 0
        numCnt = 0
        self.line.clear()
        self.label.clear()
    
    def btnBck(self):
        # '='가 입력된 이후에는 작동하지않도록 설정
        # Setting diable 'btnBck' after 'btnEq'
        global newNum

        self.line.backspace()
        newNum = self.line.text()

        print("Bck newNum = ", newNum)

def main():
    app = QtGui.QApplication(sys.argv)
    f = Form()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

'''수정해야할 것
1. Bck 한 이후의 숫자를 갖도록 하자. (ok)
2. '='버튼이 입력된 이후에는 'Bck'버튼이 작동하지않도록 설정
3. 0으로 나누는 문제 (ok)
4. 레이아웃 문제
5. 처음에 0이 쓰여지지않게 하는 문제 예를 들어 02, 002 가 나오지 않도록 (ok)
6. 여러 작업했을 때 에러 ex) 1+2+3이 2+3만 됨. (ok)
7. global을 쓰지 않고 구현하는 방법
8. 결과가 나온 후 숫자를 입력하면 결과값 삭제
9. ex) 1+2+12 마지막 2를 지우고 1+2+1 = 5로 나오는 오류

'''
