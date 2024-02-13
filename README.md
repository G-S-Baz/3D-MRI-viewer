# 3D fMRI viewer - project proposel
This project will enable the visualization of fMRI data in a 3D manner, compared to the traditional 2D viewers.
Hopefully, that will aid in looking at activity changes that exist within and between tasks and subjects.

For the visualization, masks files representing certain areas of the brain will be used and ploted ass a mesh plot.
FMRI activity, on the other hand, will be ploted as a 3D scatter plot - with activity intensity represented by color.
if time will allow, a GUI that help controling the different features of the plot will be devoloped as well.

for that manner, a vtk python package called [vtkplotlib](https://vtkplotlib.readthedocs.io/en/v1.5.1/Plots.html) will be used.
[VTK - The Visualization Toolkit](https://vtk.org/) is a strong 3D visualization tool, but not that easy to operate. Thats why vtkplotlib will be helpfull.

I'm planning on using the following packages:
* numpy - for manipulating the images data.
* nibabel - for loading the MRI data which is in NIFTI format.
* stl & skimage - to create mesh objects.
*  vtkplotlib - for ploting.
