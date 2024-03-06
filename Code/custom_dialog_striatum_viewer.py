import sys
from PyQt6 import QtWidgets

class CustomFileDialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Upload NIfTI Files")
        self.layout = QtWidgets.QVBoxLayout(self)

        self.buttons = []
        self.selected_files = []

        file_types = ["STR R", "STR L", "fMRI"]

        for file_type in file_types:
            button = QtWidgets.QPushButton(f"Choose {file_type}")
            button.clicked.connect(lambda _, file_type=file_type: self.choose_file(file_type))
            self.buttons.append(button)
            self.layout.addWidget(button)

        self.ok_button = QtWidgets.QPushButton("OK")
        self.ok_button.clicked.connect(self.accept)
        self.layout.addWidget(self.ok_button)

    def choose_file(self, file_type):
        file_dialog = QtWidgets.QFileDialog()
        file_dialog.setNameFilter("NIfTI files (*.nii)")
        file_dialog.setFileMode(QtWidgets.QFileDialog.FileMode.ExistingFiles)
        file_dialog.setViewMode(QtWidgets.QFileDialog.ViewMode.List)
        file_dialog.setWindowTitle(f"Choose {file_type}")

        if file_dialog.exec() == QtWidgets.QDialog.DialogCode.Accepted:
            selected_files = file_dialog.selectedFiles()
            if selected_files:
                self.selected_files.append(selected_files[0])
                index = self.buttons.index(self.sender())
                self.buttons[index].setText(f"{file_type}: {selected_files[0].split('/')[-1]}")
            else:
                print("No file selected.")