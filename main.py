import sys
from PyQt5.QtWidgets import *

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.Main()

    def Main(self):
        self.setWindowTitle('Secret')
        self.setGeometry(600, 300, 800, 500)
        self.show()

if __name__=="__main__":
    app = QApplication(sys.argv)
    Main = Main()
    Main.show()
    sys.exit(app.exec_())