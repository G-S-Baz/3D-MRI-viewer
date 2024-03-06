import numpy as np
import vtkplotlib as vpl
from PyQt6 import QtWidgets, QtCore
from custom_dialog_striatum_viewer import CustomFileDialog
import striatum_viewer_supporting_functions as sf

class STRviewerUI(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # Initialize variables to hold plots
        self.structure_L_plot = []
        self.structure_R_plot = []
        self.function_L_plots = []
        self.function_R_plots = []
        
        # Go for a vertical stack layout.
        vbox = QtWidgets.QVBoxLayout()
        self.setLayout(vbox)
        self.setWindowTitle('striatum viewer')

        # Create the figure
        self.figure = vpl.QtFigure()
        self.index = 1 # image number
        toolbar = QtWidgets.QToolBar("My main toolbar")

        # Add choose files to the toolbar
        files_upload = toolbar.addAction("Files")
        files_upload.triggered.connect(self.files_upload_dialog)

        # Add a save button to the toolbar
        save_action = toolbar.addAction("Save")
        save_action.triggered.connect(self.save_as_image)
        
        # Add widgets to the toolbar
        reset_action = toolbar.addAction("Reset Camera Distance")
        reset_action.triggered.connect(self.camera_reset_button)

        struct_color_action = toolbar.addAction("Choose Structure Color")
        struct_color_action.triggered.connect(self.color_picker)
        self.struct_color = "dark red"

        set_index = toolbar.addAction("set image")
        set_index.triggered.connect(self.set_image_index)
        
        # Create buttons for left and right arrows controling the index of the image
        left_arrow_button = toolbar.addAction("<")
        left_arrow_button.triggered.connect(self.decrement_index)
        right_arrow_button = toolbar.addAction(">")
        right_arrow_button.triggered.connect(self.increment_index)
        self.title_label = QtWidgets.QLabel(f" Image Number: {self.index}")
        self.title_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        # Create checkboxes for structural plots
        self.label_structure = QtWidgets.QLabel("       structure")
        self.checkbox_L_structure = QtWidgets.QCheckBox("STR L")
        self.checkbox_L_structure.setChecked(False)
        self.checkbox_L_structure.toggled.connect(self.onClickedLstructure)

        self.checkbox_R_structure = QtWidgets.QCheckBox("STR R")
        self.checkbox_R_structure.setChecked(False)
        self.checkbox_R_structure.toggled.connect(self.onClickedRstructure)
        
        # Create checkboxes for functional plots
        self.label_function = QtWidgets.QLabel("        function")
        self.checkbox_L_function = QtWidgets.QCheckBox("STR L")
        self.checkbox_L_function.setChecked(True)
        self.checkbox_L_function.toggled.connect(self.onClickedLfunction)

        self.checkbox_R_function = QtWidgets.QCheckBox("STR R")
        self.checkbox_R_function.setChecked(True)
        self.checkbox_R_function.toggled.connect(self.onClickedRfunction)

        # Create tvalue range with 2 QSpinBox
        self.label_Tvalue_range = QtWidgets.QLabel("t-value range")
        self.input_min = QtWidgets.QSpinBox() # "min: "
        self.input_min.setValue(2)
        self.input_min.valueChanged[int].connect(self.onInputChanged)
        self.input_max = QtWidgets.QSpinBox() # "max: "
        self.input_max.setValue(7)
        self.input_max.valueChanged[int].connect(self.onInputChanged)

        # control radius with slider
        self.radius_slider_label = QtWidgets.QLabel("radius")
        self.radius_slider = QtWidgets.QSlider()
        self.radius_slider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.radius_slider.setRange(0, 10)  # Values represent 0.0 to 1.0
        self.radius_slider.setSingleStep(1)  # Step size represents 0.1
        self.radius_slider.setTickInterval(1)
        self.radius_slider.setTickPosition(QtWidgets.QSlider.TickPosition.TicksBelow)
        self.radius_slider.setValue(5)
        self.radius_slider.valueChanged.connect(self.slider_change)

        # control opacity with slider
        self.opacity_slider_label = QtWidgets.QLabel("opacity")
        self.opacity_slider = QtWidgets.QSlider()
        self.opacity_slider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.opacity_slider.setRange(0, 10)  # Values represent 0.0 to 1.0
        self.opacity_slider.setSingleStep(1)  # Step size represents 0.1
        self.opacity_slider.setTickInterval(1)
        self.opacity_slider.setTickPosition(QtWidgets.QSlider.TickPosition.TicksBelow)
        self.opacity_slider.setValue(5)
        self.opacity_slider.valueChanged.connect(self.slider_change)
        
        # upload the files:
        self.files_upload_dialog()

        # making the structural and functional tickboxes layout
        line = QtWidgets.QFrame()
        line.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        structural_layout = QtWidgets.QVBoxLayout()
        structural_layout.addWidget(self.checkbox_L_structure)
        structural_layout.addWidget(self.checkbox_R_structure)

        functional_layout = QtWidgets.QVBoxLayout()
        functional_layout.addWidget(self.checkbox_L_function)
        functional_layout.addWidget(self.checkbox_R_function)

        checkbox_layout = QtWidgets.QHBoxLayout()
        checkbox_layout.addWidget(self.label_structure)
        checkbox_layout.addLayout(structural_layout)
        checkbox_layout.addWidget(line)
        checkbox_layout.addWidget(self.label_function)
        checkbox_layout.addLayout(functional_layout)
        
        # Add widgets to layout:
        vbox.addWidget(toolbar)
        vbox.addWidget(self.label_Tvalue_range)
        vbox.addWidget(self.input_min)
        vbox.addWidget(self.input_max)
        vbox.addWidget(self.title_label)
        vbox.addWidget(self.figure)
        vbox.addLayout(checkbox_layout)
        vbox.addWidget(self.radius_slider_label)
        vbox.addWidget(self.radius_slider)
        vbox.addWidget(self.opacity_slider_label)
        vbox.addWidget(self.opacity_slider)
        
        
    def files_upload_dialog(self):
        dialog = CustomFileDialog()
        if dialog.exec() == QtWidgets.QDialog.DialogCode.Accepted:
            selected_files = dialog.selected_files
            if len(selected_files) == 3:
                for file, button in zip(selected_files, dialog.buttons):
                    if "STR R" in button.text():
                        self.Rmask_name = file
                        self.Lmask = sf.LoadAndPreprocessMask(self.Rmask_name)
                    elif "STR L" in button.text():
                        self.Lmask_name = file
                        self.Rmask = sf.LoadAndPreprocessMask(self.Lmask_name)
                    elif "fMRI" in button.text():
                        self.fMRI_name = file
                        self.fMRI = sf.LoadfMRI(self.fMRI_name)
                print("Selected Files:")
                print("STR R:", self.Rmask_name)
                print("STR L:", self.Lmask_name)
                print("fMRI:", self.fMRI_name)

                self.index_max = self.fMRI.shape[3] # max image number
                self.onInputChanged()
            else:
                print("Please select exactly 3 NIfTI files.")
    
    def set_image_index(self):
        dialog = QtWidgets.QInputDialog()
        dialog.setLabelText("Image Number:")
        dialog.setInputMode(QtWidgets.QInputDialog.InputMode.IntInput)
        dialog.setIntMinimum(1)
        dialog.setIntMaximum(self.index_max)
        dialog.resize(250, dialog.height())

        ClickedButten = dialog.exec()
        if ClickedButten:
            self.index = dialog.intValue()
            self.onInputChanged()
            self.title_label.setText(f" Image Number: {self.index}")
        
    def increment_index(self):
        if self.index != self.index_max:
            self.index += 1
            self.onInputChanged()
            self.title_label.setText(f" Image Number: {self.index}")

    def decrement_index(self):
        if self.index != 1:
            self.index -= 1
            self.onInputChanged()
            self.title_label.setText(f" Image Number: {self.index}")
            
    def camera_reset_button(self):
        vpl.reset_camera(self.figure)
        self.figure.update()

    def onInputChanged(self):
        for plot in self.function_L_plots:
            self.figure.remove_plot(plot)
        for plot in self.function_R_plots:
            self.figure.remove_plot(plot)
        self.figure.update()
        self.onClickedLfunction()
        self.onClickedRfunction()
        
    def color_picker(self):
        color = QtWidgets.QColorDialog.getColor()
        self.struct_color = color
        if self.structure_R_plot:
            self.figure.remove_plot(self.structure_R_plot)
        if self.structure_L_plot:
            self.figure.remove_plot(self.structure_L_plot)
        self.onClickedLstructure()
        self.onClickedRstructure()

    def onClickedLstructure(self):
        if self.checkbox_L_structure.isChecked():
            vertices = sf.create_vertices(self.Lmask)
            self.structure_L_plot = vpl.plot(vertices, join_ends=True, opacity = 0.1, color = self.struct_color)
            vpl.reset_camera(self.figure)
            self.figure.update()
        elif self.structure_L_plot:
            self.figure.remove_plot(self.structure_L_plot)  # Remove the mesh if exists
            self.structure_L_plot = []
            self.figure.update()

    def onClickedRstructure(self):
        if self.checkbox_R_structure.isChecked():
            vertices = sf.create_vertices(self.Rmask)
            self.structure_R_plot  = vpl.plot(vertices, join_ends=True, opacity = 0.1, color = self.struct_color)
            vpl.reset_camera(self.figure)
            self.figure.update()
        elif self.structure_R_plot:
            self.figure.remove_plot(self.structure_R_plot)  # Remove the mesh if exists
            self.structure_R_plot = []
            self.figure.update()

    def onClickedLfunction(self):
        if self.checkbox_L_function.isChecked():
            threshold_min = self.input_min.value()
            threshold_max = self.input_max.value()
            threshold = np.array([threshold_min, threshold_max])
            radius_value = self.radius_slider.value() / 10.0
            opacity_value = self.opacity_slider.value() / 10.0
            plots = sf.Draw_fMRI(self.fMRI[:,:,:,self.index - 1], self.Lmask, threshold, radius_value, opacity_value)
            if plots:
                self.function_L_plots.extend(plots)
            vpl.reset_camera(self.figure)
            self.figure.update()
        else:
            for plot in self.function_L_plots:
                self.figure.remove_plot(plot)
            self.function_L_plots = []
            self.figure.update()

    def onClickedRfunction(self):
        if self.checkbox_R_function.isChecked():
            threshold_min = float(self.input_min.text())
            threshold_max = float(self.input_max.text())
            threshold = np.array([threshold_min, threshold_max])
            radius_value = self.radius_slider.value() / 10.0
            opacity_value = self.opacity_slider.value() / 10.0
            plots = sf.Draw_fMRI(self.fMRI[:,:,:,self.index - 1], self.Rmask, threshold, radius_value, opacity_value)
            if plots:
                self.function_R_plots.extend(plots)
            vpl.reset_camera(self.figure)
            self.figure.update()
        else:
            for plot in self.function_R_plots:
                self.figure.remove_plot(plot)
            self.function_R_plots = []
            self.figure.update()

    def slider_change(self):
        self.onInputChanged()
        
    def save_as_image(self):
        file_dialog = QtWidgets.QFileDialog(self)
        file_dialog.setFileMode(QtWidgets.QFileDialog.FileMode.AnyFile)
        file_dialog.setAcceptMode(QtWidgets.QFileDialog.AcceptMode.AcceptSave)
        file_dialog.setNameFilter("Images (*.tiff *.jpg *.png)")

        if file_dialog.exec() == QtWidgets.QDialog.DialogCode.Accepted:
            # Save3D_str_figure(file_dialog.selectedFiles,self)
            file_path = file_dialog.selectedFiles()[0]
            print(file_path)
            # file_format = file_path.split(".")[-1]
            vpl.save_fig(file_path, off_screen = True, fig = self.figure) #
            
    def show(self):
        # The order of these two are interchangeable.
        super().show()
        self.figure.show()

    def closeEvent(self, event):
        # ensures everything gets deleted in the right order.
        self.figure.closeEvent(event)