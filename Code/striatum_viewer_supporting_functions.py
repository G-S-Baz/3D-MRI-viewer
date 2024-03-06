import vtkplotlib as vpl
import nibabel as nib
import numpy as np
from stl import mesh
import skimage as si
from matplotlib.cm import get_cmap

def LoadAndPreprocessMask(path):
    Nifti_img  = nib.load(path)
    nii_data = Nifti_img.get_fdata()
    nii_data = si.filters.gaussian(nii_data,sigma=0.5)
    nii_data = np.array(nii_data>0.5)
    return nii_data

def MeshFromBinary(binary_image):
    verts, faces, normals, values = si.measure.marching_cubes(binary_image, 0)

    obj_3d = mesh.Mesh(np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype))

    for i, f in enumerate(faces):
        obj_3d.vectors[i] = verts[f]
    
    return obj_3d

def create_vertices(nii_data):
    nii_data = MeshFromBinary(nii_data)
    vertices = nii_data.vectors
    return vertices

def LoadfMRI(path):
    Nifti_img  = nib.load(path)
    nii_data = Nifti_img.get_fdata()
    return nii_data

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

# def Save3D_str_figure(selectedFiles,self):
#     file_path = selectedFiles()[0]
#     file_format = file_path.split(".")[-1]

#     # Get the VTK render window associated with the QtFigure
#     vtk_render_window = self.figure.renWin()

#     # Convert VTK render window to image
#     window_to_image_filter = vtkWindowToImageFilter()
#     window_to_image_filter.SetInput(vtk_render_window)
#     window_to_image_filter.Update()

#     # Save the image to file
#     writer = vtk.vtkPNGWriter()
#     writer.SetFileName(file_path)
#     writer.SetInputConnection(window_to_image_filter.GetOutputPort())
#     writer.Write()