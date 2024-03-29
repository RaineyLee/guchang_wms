import sys
from cx_Freeze import setup, Executable
import traceback
from PyQt5.QtWidgets import QApplication, QMessageBox

try:
    # 개발 참조 사이트
    # https://cx-freeze.readthedocs.io/en/latest/setup_script.html#cmdoption-arg-include_files
    build_exe_options = {"include_files": [""]}

    # executables = (
    #     [
    #         Executable(
    #             "main.py",
    #             copyright="Copyright (C) 2023 cx_Freeze",
    #             # base=base,
    #             icon="wms.256x231.png",
    #         ),
    #     ],
    # )

    setup(
        name="WMS",
        version="1.0",
        description="Guchang WMS",
        executables=[
            Executable(
                "main.py",
                copyright="Copyright (C) 2023 cx_Freeze",
                # base="C:\Python Workplace\Make_ERP",
                icon="warehouse.ico",
            ),
        ],
        options={
            "build_exe": build_exe_options,
            # "bdist_msi": bdist_msi_options,
        },
    )
except Exception as e:
    app = QApplication(sys.argv)

    msg = QMessageBox()
    msg.setWindowTitle("Error")               # 제목설정
    msg.setText(str(e))                          # 내용설정
    msg.exec_()    