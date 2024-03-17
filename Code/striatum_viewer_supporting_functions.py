import vtkplotlib as vpl
import nibabel as nib
import numpy as np
from stl import mesh
import skimage as si
from matplotlib.cm import get_cmap

% loading the probability image for a certain breain structure
def LoadAndPreprocessMask(path):
    Nifti_img  = nib.load(path)
    nii_data = Nifti_img.get_fdata()
    nii_data = si.filters.gaussian(nii_data,sigma=0.5)
    nii_data = np.array(nii_data>0.5)
    return nii_data

% making a mesh coordinats from the probability file
def MeshFromBinary(binary_image):
    verts, faces, normals, values = si.measure.marching_cubes(binary_image, 0)

    obj_3d = mesh.Mesh(np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype))

    for i, f in enumerate(faces):
        obj_3d.vectors[i] = verts[f]
    
    return obj_3d

% creating vertices from the coordinates
def create_vertices(nii_data):
    nii_data = MeshFromBinary(nii_data)
    vertices = nii_data.vectors
    return vertices

% loading the 4D fMRI data
def LoadfMRI(path):
    Nifti_img  = nib.load(path)
    nii_data = Nifti_img.get_fdata()
    return nii_data

# ploting the fMRI data as 3D scatter plot
def Draw_fMRI(fMRIdata,mask,threshold,radius_value,opacity_value):
    coordinats = np.argwhere(mask) # what points to draw
    if threshold[1] >= threshold[0]:
        plots = []
        for voxel in range(0,coordinats.shape[0]-1):
            voxel_data = fMRIdata[coordinats[voxel,0],coordinats[voxel,1],coordinats[voxel,2]]
            if voxel_data > threshold[0]:
                color_value = ((voxel_data - threshold[0])/(threshold[1] - threshold[0]))
                plot = vpl.scatter(coordinats[voxel,:], radius = radius_value, color = get_cmap("autumn")(color_value), opacity=opacity_value)
                plots.append(plot)
        return plots
