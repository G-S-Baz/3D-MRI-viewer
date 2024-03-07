## project's description

This project took on a mission to achieve visualization of fMRI activation over multiple time points in a 3D manner.
In my research, I'm especially interested in the brain activity of a structure called the striatum. Relatively to a subcortical area it is quite large structure, so changes that occur over time might be more pronounced in there.
In the current phase of this project i've decided to focus solely on that area, and even named my program "straitum viewer" (though any kind of structure image can be used as long as its a probabilty atlas with dimention that match the fMRI).

The program is splitted into 4 codes (in the Code folder), containing a GUI based on the PyQt6 package:
* STR_viewer_main.py - the main program code to excute the GUI.
* striatum_viewer_ui.py - the main GUI code with all the widgets that were implemented.
* custom_dialog_striatum_viewer.py - a code that helps implement user dialog for choosing the required MRI files.
* striatum_viewer_supporting_functions.py - a set of functions that the program is utilizing for uploading, processing and plotting the MRI \ fMRI data.

Upon activation (typing python .\STR_viewer_main.py in the cmd) a dialog box asking the user the chose 3 NIFTI file:
* A probability atals of the left striatum.
* A probability atals of the right striatum.
* An fMRI activation map (3D) with time coded at the forth dimention.
Example files are given at the ExampleData folder.
New files can be chosed from the GUI using the files tab at the toolbar, they are uploaded when pressing OK at the dialog box.

At the toolbar, you can find as well:
* save - saving the figure in either jpeg, png or tiff format.
* Reset camera distance - if you zoomed in or out it can reset the camera distance
* Choose structure color - can change the color of the structure mesh plot.
* set image - an important feature helping to set the activation map required to be presented. The current image is written the figure title.
* right and left arrows - changing the activation map index.

Then, The GUI also contains:
* 't-value range' - those are the upper and lower limits for the colors representing activity in the form of t-value (as castumed in fMRI). data bellow the lower threshold won't be presented.
* title containing the current image index.
* the figure itself.
* Check boxes allowing the user to choose whether to present the activity and\or the structure of the left and\or right side.
* A slider controling the radius of the points in the scatter plot that represents fMRI activity.
* A slider controling the opacity of the points (should be set to maximum when image is to be saved, otherwise colors would be off in a weird way).

Future prespectives for the project include:
* Allowing for several sets of structures (each with a different NIFTI file) to be included and presented.
* Spliting the striatum_viewer_ui.py code into 2 since its too long.
* Allowing the user to chose several activation maps on different files instead of one NIFTI that contains all.
* Allowing for negative activation value (in case they are of interest).

For the code to run, the following python packages should be installed:
- vtkplotlib
- nibabel
- numpy
- stl
- skimage
- matplotlib
- PyQt6
