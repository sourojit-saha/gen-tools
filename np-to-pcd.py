#!/usr/bin/env python3
# For mor info visit: http://www.open3d.org/docs/0.7.0/tutorial/Basic/working_with_numpy.html

# The numpy array (.npy format) should be of the form Nx3, where N is the number of points, and 
# the first column is X coordinate
# the second column is Y coordinate
# the third column is Z coordinate

import numpy as np
import open3d as o3d

def np_to_pcd(source, destination):

    xyz = np.load(source)

    ## uncomment the below line to remove duplicate rows 
    # xyz = np.unique(xyz, axis=0) 

    ## print the shape of np.array...for reference
    print("xyz shape: ",xyz.shape)
    if xyz.shape[1]!=3:
        return

    ## Pass xyz to Open3D.o3d.geometry.PointCloud and visualize
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(xyz)
    o3d.io.write_point_cloud(destination, pcd) 
    print("File saved!!")

    ## Load saved point cloud and visualize it
    pcd_load = o3d.io.read_point_cloud(destination)
    o3d.visualization.draw_geometries([pcd_load])
    
    return

if __name__ == "__main__":

    source = "/home/p43s/slam_project_ws/nb-slam_run_1-partial.npy" ## insert the path to the numpy array 
    destination = "yoyo-nb-slam_run_1-partial.ply" ## insert path where you want to save it

    np_to_pcd(source, destination)

