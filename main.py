import os
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QDate
from PyQt5 import uic

# 절대경로를 상대경로로 변경 하는 함수
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

#UI파일 연결
# main_window= uic.loadUiType(resource_path("/Users/black/projects/make_erp/main_window.ui"))[0] # Mac 사용시 ui 주소
main_window= uic.loadUiType(resource_path("C:.\main_window.ui"))[0] # Window 사용시 ui 주소

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, main_window) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("구창_용인창고")
        # self.slots()

        menu_bar = self.menuBar()
        outgoing_menu = menu_bar.addMenu("출고")
        incommig_menu = menu_bar.addMenu("입고")
        inventory_menu = menu_bar.addMenu("재고")
        upload_menu = menu_bar.addMenu("업로드")
        
        outgoing = QAction('제품출고', self)
        outgoing.setStatusTip("제품출고")
        outgoing.triggered.connect(self.outgoing)

        upload_location = QAction('제품위치 업로드', self)
        upload_location.setStatusTip("제품위치 업로드")
        upload_location.triggered.connect(self.upload_location)

        upload_barcode = QAction('바코드 업로드', self)
        upload_barcode.setStatusTip("바코드 업로드")
        upload_barcode.triggered.connect(self.upload_barcode)

        upload_saleslist = QAction('출고리스트 업로드', self)
        upload_saleslist.setStatusTip("출고리스트 업로드")
        upload_saleslist.triggered.connect(self.upload_saleslist)

        item_location = QAction('제품위치 입력', self)
        item_location.setStatusTip("제품위치 입력")
        item_location.triggered.connect(self.item_location)

        make_cjnumber = QAction('CJ송장번호 생성', self)
        make_cjnumber.setStatusTip("CJ송장번호 생성")
        make_cjnumber.triggered.connect(self.make_cjnumber)

        outgoing_menu.addAction(outgoing)
        outgoing_menu.addAction(make_cjnumber)
        upload_menu.addAction(upload_location)
        upload_menu.addAction(upload_barcode)
        upload_menu.addAction(upload_saleslist)
        inventory_menu.addAction(item_location)

        status_bar = self.statusBar()
        self.setStatusBar(status_bar)

    def outgoing(self):
        print("new menu call")

    def upload_location(self):        
        import upload_location as inv_loc

        self.location = inv_loc.WindowClass() #메인창에서 띄우려면 메인창을 뜻하는 self 추가
        self.location.show() #메인창에서 띄우려면 메인창을 뜻하는 self 추가

    def upload_barcode(self):
        import upload_barcode as bar_loc

        self.barcode = bar_loc.WindowClass() #메인창에서 띄우려면 메인창을 뜻하는 self 추가
        self.barcode.show() #메인창에서 띄우려면 메인창을 뜻하는 self 추가

    def upload_saleslist(self):
        import upload_saleslist as saleslist

        self.saleslist = saleslist.WindowClass() #메인창에서 띄우려면 메인창을 뜻하는 self 추가
        self.saleslist.show() #메인창에서 띄우려면 메인창을 뜻하는 self 추가

    def item_location(self):
        import toexcel_location as item_loc

        self.item_loc = item_loc.WindowClass() #메인창에서 띄우려면 메인창을 뜻하는 self 추가
        self.item_loc.show() #메인창에서 띄우려면 메인창을 뜻하는 self 추가

    def make_cjnumber(self):
        import CJ_number_v1_2 as cj_number

        self.cj_number = cj_number.WindowClass() #메인창에서 띄우려면 메인창을 뜻하는 self 추가
        self.cj_number.show() #메인창에서 띄우려면 메인창을 뜻하는 self 추가

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    try:
        myWindow = WindowClass()
        myWindow.show()
        app.exec_()
    except Exception as e:
        msg = QMessageBox()
        msg.setWindowTitle("Error")               # 제목설정
        msg.setText(e)                          # 내용설정
        msg.exec_()  