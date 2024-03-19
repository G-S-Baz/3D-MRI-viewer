# Project's description

Viewing functional MRI images in 3D.
The viewer plots both the outline of a brain structure as mesh plots (taken from probability maps) and the activity (represented by t-value) of each pixel \ voxel within the structure as a 3D scatter plot.

The program is split into 4 codes (in the Code folder), containing a GUI based on the PyQt6 package:
* STR_viewer_main.py - the main program code to execute the GUI.
* striatum_viewer_ui.py - the main GUI code with all the widgets that were implemented.
* custom_dialog_striatum_viewer.py - a code that helps implement user dialog for choosing the required MRI files.
* striatum_viewer_supporting_functions.py - a set of functions that the program is utilizing for uploading, processing, and plotting the MRI \ fMRI data.

# How to use it
Download all data in the repository.
Then, run: 
    pip install -r requirements.txt
To run the program, the user should type "python .\STR_viewer_main.py" in the cmd while in the code folder.
Upon activation, a dialog box asks the user the choose 3 NIFTI files (it is a medical imaging file format):
Example files are given in the ExampleData folder.
* A probability atals of the left striatum (In the ExampleData: rwSTR_L_prob_mni_non_linear_young.nii).
* A probability atals of the right striatum(In the ExampleData: rwSTR_R_prob_mni_non_linear_young.nii).
* An fMRI activation map (3D) with time coded at the forth dimention(In the ExampleData: swTmaps_1-10.nii).

At the toolbar, you can find:
* files - Choosing new files to present. They are uploaded when pressing OK in the dialog box.
* save - saving the figure in either jpeg, png, or tiff format.
* Reset camera distance - if you zoom in or out it can reset the camera distance
* Choose structure color - can change the color of the structure mesh plot.
* set image - an important feature helping to set the activation map required to be presented. The current image is written the figure title.
* right and left arrows - changing the activation map index.

The GUI features from top to down:
* 't-value range' - those are the upper and lower limits for the colors representing activity in the form of t-value (as costumed in fMRI). data bellow the lower threshold won't be presented.
* title containing the current image index.
* the figure itself.
* Check-boxes allow the user to choose whether to present the activity and\or the structure of the left and\or right side.
* A slider that controls the radius of the points in the scatter plot that represents fMRI activity.
* A slider that controls the opacity of the points (should be set to maximum when the plot is to be saved, otherwise the saved image colors would be off in a weird way).

# Personal comments:
This project took on a mission to achieve visualization of fMRI activation over multiple time points in a 3D manner.
In my research, I'm especially interested in the brain activity of a structure called the striatum. Relatively to a subcortical area, it is quite large structure, so changes that occur over time might be more pronounced in there.
In the current phase of this project i've decided to focus solely on that area, and even named my program "striatum viewer" (though any kind of structure image can be used as long as it is a probability atlas with dimensions matching the fMRI).

(Future perspectives for the project are:
* Split the striatum_viewer_ui.py code into 2 since it is too long.
* Allowing for several sets of structures (each with a different NIFTI file) to be included and presented.
* Allowing the user to choose several activation maps on different files instead of one NIFTI that contains all.
* Allowing for negative activation value (in case they are of interest).)
