import sys
from PyQt5.QtWidgets import QApplication, \
    QWidget, QLabel, QTextEdit, QVBoxLayout, QMainWindow


class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.Main()

    def Main(self):
        self.lbl1 = QLabel('Enter your sentence:')
        self.te = QTextEdit()
        self.te.setAcceptRichText(False)
        self.lbl2 = QLabel('The number of words is 0')

        self.te.textChanged.connect(self.text_changed)

        vbox = QVBoxLayout()
        vbox.addWidget(self.lbl1)
        vbox.addWidget(self.te)
        vbox.addWidget(self.lbl2)
        vbox.addStretch()

        self.setLayout(vbox)

        self.setWindowTitle('Secret')
        self.setGeometry(600, 300, 800, 500)
        self.show()

    def text_changed(self):
        text = self.te.toPlainText()
        self.lbl2.setText(text + "는 바보 입니다")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Main()
    sys.exit(app.exec_())

