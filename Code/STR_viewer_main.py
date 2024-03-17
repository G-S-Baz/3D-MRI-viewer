import sys
from PyQt6 import QtWidgets
from striatum_viewer_ui import STRviewerUI

# Running the GUI
def main():
    qapp = QtWidgets.QApplication.instance() or QtWidgets.QApplication(sys.argv)

    window = STRviewerUI()
    window.show()
    qapp.exec()

if __name__ == "__main__":
    main()
