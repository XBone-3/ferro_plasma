import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QGridLayout, QVBoxLayout, QLineEdit
from PyQt5.QtCore import Qt
from functools import partial

ERROR_MSG = 'ERRRRRRR ERROR'


class CalculatorUi(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calculator 1.0')
        self.setFixedSize(235, 235)
        self.generalLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)
        self._createScreen()
        self._createButtons()

    def _createScreen(self):
        self.screen = QLineEdit()
        self.screen.setFixedHeight(35)
        self.screen.setAlignment(Qt.AlignRight)
        self.screen.setReadOnly(True)
        self.generalLayout.addWidget(self.screen)

    def _createButtons(self):
        self.buttons = {}
        buttonsLayout = QGridLayout()
        buttons = {'7': (0, 0),
                   '8': (0, 1),
                   '9': (0, 2),
                   '/': (0, 3),
                   'C': (0, 4),
                   '4': (1, 0),
                   '5': (1, 1),
                   '6': (1, 2),
                   '*': (1, 3),
                   '(': (1, 4),
                   '1': (2, 0),
                   '2': (2, 1),
                   '3': (2, 2),
                   '-': (2, 3),
                   ')': (2, 4),
                   '0': (3, 0),
                   '00': (3, 1),
                   '.': (3, 2),
                   '+': (3, 3),
                   '=': (3, 4)}
        for btnText, pos in buttons.items():
            self.buttons[btnText] = QPushButton(btnText)
            self.buttons[btnText].setFixedSize(40, 40)
            buttonsLayout.addWidget(self.buttons[btnText], pos[0], pos[1])
        self.generalLayout.addLayout(buttonsLayout)

    def setScreenText(self, text):
        self.screen.setText(text)
        self.screen.setFocus()

    def screenText(self):
        return self.screen.text()

    def clearScreen(self):
        self.setScreenText("")


class CalculatorControl:
    def __init__(self, model, view):
        self._evaluate = model
        self._view = view
        self._connectSignals()

    def _calculateResult(self):
        result = self._evaluate(expression=self._view.screenText())
        self._view.setScreenText(result)

    def _buildExpression(self, sub_exp):
        if self._view.screenText() == ERROR_MSG:
            self._view.clearScreen()
        expression = self._view.screenText() + sub_exp
        self._view.setScreenText(expression)

    def _connectSignals(self):
        for btnText, btn in self._view.buttons.items():
            if btnText not in ('=', 'C'):
                btn.clicked.connect(partial(self._buildExpression, btnText))
        self._view.buttons['='].clicked.connect(self._calculateResult)
        self._view.screen.returnPressed.connect(self._calculateResult)
        self._view.buttons['C'].clicked.connect(self._view.clearScreen)


def calculator_evaluate(expression):
    try:
        result = str(eval(expression))
    except Exception:
        result = ERROR_MSG
    return result


if __name__ == '__main__':
    calculator = QApplication(sys.argv)
    evaluate = calculator_evaluate
    UI = CalculatorUi()
    UI.show()
    CalculatorControl(model=evaluate, view=UI)
    sys.exit(calculator.exec())
