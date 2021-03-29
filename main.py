import sys
from PyQt5.QtWidgets import QApplication, \
    QWidget, QLabel, QTextEdit, QVBoxLayout, QMainWindow, QPushButton


class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.Main()

    def Main(self):
        label1 = QLabel('삐빅 삐빅 알 수 없음', self)
        label1.move(290, 30)
        font1 = label1.font()
        font1.setPointSize(20)
        label1.setFont(font1)
        label2 = QLabel(' 좋아하는 단어와 문장을 영어로 작성하여',self)
        label2.move(260, 100)
        font2 = label2.font()
        font2.setPointSize(13)
        label2.setFont(font2)
        label3 = QLabel('암호문이 된 문장을 확인해보세요!', self)
        label3.move(290, 130)
        font3 = label3.font()
        font3.setPointSize(13)
        label3.setFont(font3)

        self.textedit = QTextEdit(self)

        btn1 = QPushButton('결과 보기', self)
        btn1.move(370, 530)
        btn1.resize(100, 30)

        self.setWindowTitle('Secret')
        self.setGeometry(600, 300, 800, 600)
        self.show()

    def text_changed(self):
        text = self.te.toPlainText()
        self.lbl2.setText(text + "는 바보 입니다")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Main()
    sys.exit(app.exec_())

