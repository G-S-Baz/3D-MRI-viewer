# 3D fMRI viewer
By [Guy Baz](https://g-s-baz.github.io/)

This project will enable the visualization of fMRI data in a 3D manner, compared to the traditional 2D viewers.
Hopefully, that will aid in looking at activity changes that exist within and between tasks and subjects at a certain brain region. For my research, I;m specifically interested in visualizing the striatum.

For the visualization, masks files representing certain areas of the brain will be used and ploted as a mesh plot.
FMRI activity will be ploted as a 3D scatter plot - with activity intensity represented by color.
if time will allow, a GUI that help controling the different features of the plot will be devoloped as well.

The viewer wiil utilize a vtk python package called [vtkplotlib](https://vtkplotlib.readthedocs.io/en/v1.5.1/Plots.html).
[VTK - The Visualization Toolkit](https://vtk.org/) is a strong 3D visualization tool, but not that easy to learn and operate. Thats why vtkplotlib will be helpfull.

I'm planning on using the following packages:
* numpy - for manipulating the images data.
* nibabel - for loading the MRI data which is in NIFTI format.
* stl & skimage - to create mesh objects.
* vtkplotlib - for ploting.
