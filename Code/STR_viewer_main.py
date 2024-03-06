import sys
from PyQt6 import QtWidgets
from striatum_viewer_ui import STRviewerUI

# Main part of the script
def main():
    qapp = QtWidgets.QApplication.instance() or QtWidgets.QApplication(sys.argv)

    window = STRviewerUI()
    window.show()
    qapp.exec()

if __name__ == "__main__":
    main()

# import sys
# from PyQt6 import QtWidgets
# from STRviewerUIElements import STRViewerUI
# from STRviewerLogic import STRViewerLogic

# # Main part of the script
# def main():
#     qapp = QtWidgets.QApplication.instance() or QtWidgets.QApplication(sys.argv)

#     # Create UI elements
#     ui_elements = STRViewerUI()

#     # Create logic class and pass UI elements
#     logic = STRViewerLogic(ui_elements)

#     # Show the UI
#     ui_elements.show()

#     qapp.exec()

# if __name__ == "__main__":
#     main()