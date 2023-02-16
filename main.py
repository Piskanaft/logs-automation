import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
from PyQt5 import uic

MyWindow, base_class = uic.loadUiType('./gui.ui')
class MainWindow(base_class):
    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)
        self.ui = MyWindow()
        self.ui.setupUi(self)
        

        self.ui.select_file_btn.clicked.connect(self.load_catalog)

    def load_catalog(self):
        file_path = qtw.QFileDialog.getOpenFileName(self, 'Open File',filter="Txt (*.txt)")
        if not file_path:
            return None
        file_path = file_path[0]
        print(file_path)
        self.ui.selected_file_lbl.setText(file_path)
        


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec_())