##How to Generate Meshes for FEniCS from MRI Data
* Download MeVisLab ver >= 3.1.1, and appropriate files from the 'mesh_generation' directory.
  * I downloaded verion 2.8 and was missing two required modules
* Load 'LV_Segmentation_UKY.mlab' in MeVisLab.
* Using the DicomImport module in MeVisLab, convert raw MRI images to DICOM format.
* Follow instructions from FEniCS_LV_Segmentation.pdf. This should yield a '.stl' file. Do this for epi and endo volumes.
    * Some clarification for the Transform World Matrix: Change the entries in the last column so that the contours are in the center of the viewing volume. **Make sure to use the same transformation for both endo and epi volumes.**  
* Run the 1.createLV.py script on the stl files (creating json input for this now to be able to specify output directory and mesh name). This creates .vtk files.
* Run LV_Test.py on the New_Mesh files to yield the HDF5 file. This is what is needed for FEniCS. This step creates the mesh and assignes fiber angles, as well as the local coordinate system for each element.
