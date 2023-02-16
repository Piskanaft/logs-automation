import sys
import os
from math import pi
from openpyxl import Workbook
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
        self.connect_buttons()
        
    def connect_buttons(self):
        self.ui.select_file_btn.clicked.connect(self.load_catalog)
        self.ui.write_btn.clicked.connect(self.write_button_pressed)

    def load_catalog(self):
        file_path = qtw.QFileDialog.getOpenFileName(self, 'Open File',filter="Txt (*.txt)")
        if not file_path:
            return None
        self.file_path = file_path[0]
        
        selected_file_name = os.path.basename(self.file_path)
        self.ui.selected_file_lbl.setText(f'Выбран файл\n{selected_file_name}')
    def write_button_pressed(self):
        logs = self.compose_logs()
        print(logs)
        wb = Workbook()
        ws = wb.active
        for row in logs:
            ws.append(row)
        wb.save('doc.xlsx')
    def compose_logs(self):
        logs = [['Date', 'Origin time', 'Lat', 'Lon', 'Depth', 'DepthMIN','DepthMAX', 'M', 'AzMajor', 'Rminor', 'Rmajor', 'S', 'N stations']]
        with open(self.file_path,'r',encoding='utf-8') as file:
            text = file.read()
            events = text.split('END EVENT')
            events.pop()
            for event in events:
                event_log = []
                event = event.strip()
                event = event[:event.find('\nAZIMUTHAL GAP')]
                splitted = event.split('\n')
                dating = event[event.find('PROB='):event.find('NSTAT')]
                dating = dating[dating.find('(')+1:dating.find(')')]
                date,time=dating.split()
                lat,lon = event[event.find(')')+2:event.find('PROB')].split()[:-1]
                
                lat,lon = float(lat.split('=')[1]), float(lon.split('=')[1])
                depths = event[event.find('DEPTH'):]
                
                depth, depthmin, depthmax = [d.split('=')[1] for d in depths.split()]
                M = ''
                azimuth = event[event.find('ELLIPSE: ')+9:event.find('DEPTH')-1]
                AzMajor, Rminor, Rmajor = [d.split('=')[1] for d in azimuth.split()]
                S = float(Rminor) * float(Rmajor) * pi
                Nstat = event[event.find('NSTAT'):event.find('NPHASES')-1].split('=')[1]
                event_log = [date,time.replace('.',':'),round(lat,3),round(lon,3), depth, depthmin, depthmax, M, AzMajor, Rminor, Rmajor, S, Nstat]
                logs.append(event_log)
        return logs


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec_())