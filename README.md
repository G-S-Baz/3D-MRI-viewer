## project's description

This project took on a mission to achieve visualization of fMRI activation over multiple time points in a 3D manner.
In my research, I'm especially interested in a structure called the striatum, which relatively to a subcortical area is also quite large, so changed that occur over time might be more pronounced.
In the current project of this project i've decided to focus on that area, and even named my program "straitum viewer" (though any kind of structure image can be used as long as its a probabilty atlas with dimention that match the fMRI).

The program is comprised of a GUI based on the PyQt6 package and is splitted into 4 codes (in the Code folder):.
* STR_viewer_main.py - the main code. The program runs when calling it in the command line.
* striatum_viewer_ui.py - the main GUI code with all the widgets that were implemented.
* custom_dialog_striatum_viewer.py - a code that helps implement user dialog for choosing the required files for the code.
* striatum_viewer_supporting_functions.py - a set of functions that the program is utilizing for uploading, processing and plotting the MRI \ fMRI data.

Upon activation (using python .\STR_viewer_main.py in the cmd) a dialog is open...

Future prespectives include:
* Allowing for several sets of structures (each with a different NIFTI file) to be included and presented.
* spliting the striatum_viewer_ui.py code into 2 since its too long.
* allowing the user to chose several activation maps on different files instead of one NIFTI that contains all.

