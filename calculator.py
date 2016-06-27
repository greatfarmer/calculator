import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt


cntNum = 0
newNum = 0

clkOp = False
cntOp = 0
funC = 0

clkEq = False
clkDot = False

result = 0


class Form(QtGui.QWidget):
    def __init__(self):
        super(Form, self).__init__()
        self.initUI()

    def initUI(self):
        #Icon setting (if you doesn't want, del this)
        self.setWindowIcon(QtGui.QIcon('patrick.jpg'))

        #Button setting
        grid = QtGui.QGridLayout()
        self.setLayout(grid)

        self.line = QtGui.QLineEdit("0")
        self.line.setReadOnly(True)
        self.line.setAlignment(Qt.AlignRight)
        grid.addWidget(self.line, 1, 0, 1, 4)
        grid.addWidget

        self.label = QtGui.QLabel()
        self.label.setAlignment(Qt.AlignRight)
        grid.addWidget(self.label, 0, 0, 1, 4)

        names = ['Cls', 'Bck', '', 'Close',
                '7', '8', '9', '/',
                '4', '5', '6', '*',
                '1', '2', '3', '-',
                '.', '0', '=', '+']
        
        positions = [(i, j) for i in range(2, 7) for j in range(4)]

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
            elif name == '.':
                button.clicked.connect(self.btnDot)
            else:
                button.clicked.connect(self.btnOp)
        
        self.move(300, 150)
        self.setWindowTitle('Calculator')
        self.show()

    def btnNum(self):
        global newNum, clkEq, clkOp, cntNum

        if clkEq == True and clkOp == False:
            self.btnCls()

        if cntNum == 0:
            self.line.clear()
            self.line.setText("0")

        sender = self.sender()
        newNum = sender.text()


        if self.line.text() != "0":
            newNum = self.line.text() + newNum
        self.line.setText(newNum)
        cntNum += 1

        clkOp = False
        clkEq = False
        print("newNum =", newNum) 

    def btnOp(self):
        global newNum, result, funC, cntOp, clkEq, clkOp, cntNum

        if cntOp == 0:
            result = float(newNum)
        elif clkEq == True:
            funC = 0
        else:
            self.cal()

        funC = self.sender().text()
        self.line.clear()
        self.line.setText(str(result))

        if clkEq == False:
            self.label.setText(self.label.text() + newNum + funC)
        else:
            self.label.setText(self.label.text() + str(result) + funC)

        cntOp += 1
        clkOp = True

        cntNum = 0
        clkEq = False
        clkDot = False
        print("Oper =", funC)    
    
    def cal(self):
        global newNum, result, funC

        if funC == '+':
            result += float(newNum)
        elif funC == '-':
            result -= float(newNum)
        elif funC == '*':
            result *= float(newNum)
        elif funC == '/':
            if float(newNum) == 0:
                result = "0으로 나눌 수 없습니다."
            else:
                result /= float(newNum)
        else:
            return

    def btnEq(self):
        global newNum, result, funC, cntOp, clkEq, clkOp, cntNum

        clkEq = True

        cntNum = 0
        clkOp = False
        clkDot = False

        if cntOp == 0:
            return

        if newNum != 0:
            self.cal()
        
        self.line.setText(str(result))
        self.label.clear()

        print("result =", result)

    def btnCls(self):
        global newNum, result, funC, cntOp, clkEq, clkOp, cntNum

        cntNum = 0
        newNum = 0

        clkOp = False
        cntOp = 0
        funC = 0

        clkEq = False
        clkDot = False

        result = 0

        self.initLine()
        self.label.clear()
    
    def btnBck(self):
        global newNum, clkEq, clkOp

        if clkEq == True or clkOp == True:
            return

        self.line.backspace()

        if self.line.text().count(".") == 0:
            clkDot = False 

        if self.line.text() == "":
            newNum = 0
            self.line.setText("0")
        else:
            newNum = self.line.text()

        print("Bck newNum = ", newNum)

    def btnDot(self):
        global newNum, clkDot, cntNum

        if clkDot == True:
            return
        
        if clkEq == True or clkOp == True:
            self.initLine()

        newNum = self.line.text() + "."
        self.line.setText(newNum)

        clkDot = True
        cntNum += 1

        print("newNum =", newNum)

    def initLine(self):
        self.line.clear()
        self.line.setText("0")

def main():
    app = QtGui.QApplication(sys.argv)
    f = Form()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

'''수정해야할 것
1. Bck 한 이후의 숫자를 갖도록 하자. (ok)
2. '='버튼이 입력된 이후에는 'Bck'버튼이 작동하지않도록 설정 (ok)
3. 0으로 나누는 문제 (ok)
4. 레이아웃 문제 (ok)
5. 처음에 0이 쓰여지지않게 하는 문제 예를 들어 02, 002 가 나오지 않도록 (ok)
6. 여러 작업했을 때 에러 ex) 1+2+3이 2+3만 됨. (ok)
7. global을 쓰지 않고 구현하는 방법
8. 결과가 나온 후 숫자를 입력하면 결과값 삭제 (ok)
9. ex) 1+2+12 마지막 2를 지우고 1+2+1 = 5로 나오는 오류 (ok)
10. 1000이 넘어가면 1,000 표시해주기 -> 세 자리숫자 마다 , 표시
11. '.' 소수점 기능 추가하기
12. 5/0 햇을때 0이 안뜸 (ok)
13. 숫자누르고 바로 = 눌렀을때 오류 (ok)
14. 함수에 return으로 True, False 하는 방법 (clkOp, clkEq)
15. 테스트코드 작성해서 동작해보기
16. state pattern 구현하기
17. 15/0 이후 0으로 나눌수 없습니다 메시지 후 새롭게 계산하면 안됨

'''