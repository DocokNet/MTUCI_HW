import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton
from PyQt5.QtGui import QFont

class Calculator(QWidget):

    
    def __init__(self):
        super(Calculator, self).__init__()
        self.setWindowTitle('Калькулятор')
        self.vbox = QVBoxLayout(self)
        self.hbox_input = QHBoxLayout()
        self.hbox_first = QHBoxLayout()
        self.hbox_second= QHBoxLayout()
        self.hbox_third = QHBoxLayout()
        self.hbox_forth = QHBoxLayout()
        self.hbox_fifth = QHBoxLayout()
        self.hbox_result = QHBoxLayout()
        self.vbox.addLayout(self.hbox_input)
        self.vbox.addLayout(self.hbox_first)
        self.vbox.addLayout(self.hbox_second)
        self.vbox.addLayout(self.hbox_third)
        self.vbox.addLayout(self.hbox_forth)
        self.vbox.addLayout(self.hbox_fifth)
        self.vbox.addLayout(self.hbox_result)
        self.setStyleSheet('background-color: skyblue',)

        self.input = QLineEdit(self)
        self.hbox_input.addWidget(self.input)

        self.b_1 = QPushButton("1", self)
        self.hbox_first.addWidget(self.b_1)
        
        self.b_2 = QPushButton("2", self)
        self.hbox_first.addWidget(self.b_2)
        
        self.b_3 = QPushButton("3", self)
        self.hbox_first.addWidget(self.b_3)

        self.b_4 = QPushButton("4", self)
        self.hbox_second.addWidget(self.b_4)
        
        self.b_5 = QPushButton("5", self)
        self.hbox_second.addWidget(self.b_5)
        
        self.b_6 = QPushButton("6", self)
        self.hbox_second.addWidget(self.b_6)

        self.b_7 = QPushButton("7", self)
        self.hbox_third.addWidget(self.b_7)
        
        self.b_8 = QPushButton("8", self)
        self.hbox_third.addWidget(self.b_8)
        
        self.b_9 = QPushButton("9", self)
        self.hbox_third.addWidget(self.b_9)
        
        self.b_dot = QPushButton(".", self)
        self.hbox_forth.addWidget(self.b_dot)

        self.b_0 = QPushButton("0", self)
        self.hbox_forth.addWidget(self.b_0)

        self.b_result = QPushButton("=", self)
        self.hbox_forth.addWidget(self.b_result)

        self.b_plus = QPushButton("+", self)
        self.hbox_first.addWidget(self.b_plus)

        self.b_minus = QPushButton("-", self)
        self.hbox_second.addWidget(self.b_minus)

        self.b_mult = QPushButton("*", self)
        self.hbox_third.addWidget(self.b_mult)

        self.b_divide = QPushButton("/", self)
        self.hbox_forth.addWidget(self.b_divide)
        
        self.b_clear = QPushButton("ОЧИСТИТЬ", self)
        self.hbox_fifth.addWidget(self.b_clear)
        

        self.b_plus.clicked.connect(lambda: self._operation("+"))
        self.b_minus.clicked.connect(lambda: self._operation("-"))
        self.b_mult.clicked.connect(lambda: self._operation("*"))
        self.b_divide.clicked.connect(lambda: self._operation("/"))
        self.b_result.clicked.connect(self._result)
        self.b_clear.clicked.connect(self._clear)

        self.b_1.clicked.connect(lambda: self._button("1"))
        self.b_2.clicked.connect(lambda: self._button("2"))
        self.b_3.clicked.connect(lambda: self._button("3"))
        self.b_4.clicked.connect(lambda: self._button("4"))
        self.b_5.clicked.connect(lambda: self._button("5"))
        self.b_6.clicked.connect(lambda: self._button("6"))
        self.b_7.clicked.connect(lambda: self._button("7"))
        self.b_8.clicked.connect(lambda: self._button("8"))
        self.b_9.clicked.connect(lambda: self._button("9"))
        self.b_0.clicked.connect(lambda: self._button("0"))
        self.b_dot.clicked.connect(lambda: self._button("."))

        self.b_1.setFont(QFont('Times', 20))
        self.b_2.setFont(QFont('Times', 20))
        self.b_3.setFont(QFont('Times', 20))
        self.b_4.setFont(QFont('Times', 20))
        self.b_5.setFont(QFont('Times', 20))
        self.b_6.setFont(QFont('Times', 20))
        self.b_7.setFont(QFont('Times', 20))
        self.b_8.setFont(QFont('Times', 20))
        self.b_9.setFont(QFont('Times', 20))
        self.b_0.setFont(QFont('Times', 20))
        self.b_dot.setFont(QFont('Times', 20))
        self.b_clear.setFont(QFont('Times', 20))
        self.b_plus.setFont(QFont('Times', 20))
        self.b_minus.setFont(QFont('Times', 20))
        self.b_mult.setFont(QFont('Times', 20))
        self.b_divide.setFont(QFont('Times', 20))
        self.b_result.setFont(QFont('Times', 20))
        self.input.setFont(QFont('Times', 30))


    def _button(self, param):
        line = self.input.text()
        if param not in ('1234567890.'):
            line = ''
        self.input.setText(line + param)

    
    def _operation(self, op):
        s = self.input.text()
        if s:
            try:
                self.num_1 = float(s)
                self.op = op
                self.input.setText("")
            except ValueError:
                self.input.setText("Вводите числа!")


    def div(self, x, y):
        try: s = x / y 
        except ZeroDivisionError: s = 'Деление на ноль невозможно!'
        return s


    def _clear(self):
        self.input.setText("")
        self.num_1 = None
        self.num_2 = None


    def _result(self):
        s = self.input.text()
        if s != '':
            self.num_2 = float(self.input.text())

            ops = {
                '+': self.num_1 + self.num_2,
                '-': self.num_1 - self.num_2,
                '*': self.num_1 * self.num_2,
                '/': self.div(self.num_1, self.num_2)
            }
            
            n = ops[self.op]
            if int(n) == n:
                self.input.setText(f"{ops[self.op]}")
            else:
                self.input.setText(f"{ops[self.op]:.3f}")


app = QApplication(sys.argv)
win = Calculator()
win.show()
sys.exit(app.exec_())
