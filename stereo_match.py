#!/usr/bin/env python

'''
Simple example of stereo image matching and point cloud generation.

Resulting .ply file cam be easily viewed using MeshLab ( http://meshlab.sourceforge.net/ )
'''

# Python 2/3 compatibility
from __future__ import print_function

import numpy as np
import cv2 as cv
import control_utils as PU

ply_header = '''ply
format ascii 1.0
element vertex %(vert_num)d
property float x
property float y
property float z
property uchar red
property uchar green
property uchar blue
end_header
'''

# Initialization of TK App
PU.init()
App = PU.get_app_handle()

def write_ply(fn, verts, colors):
    verts = verts.reshape(-1, 3)
    colors = colors.reshape(-1, 3)
    verts = np.hstack([verts, colors])
    with open(fn, 'wb') as f:
        f.write((ply_header % dict(vert_num=len(verts))).encode('utf-8'))
        np.savetxt(f, verts, fmt='%f %f %f %d %d %d ')


def main():
    while True:

        App.update()
        print('loading images...')
        imgL = cv.pyrDown(cv.imread('/home/vignesh/PycharmProjects/stereovision_trial/calib_images/obj_03_left.png'))
        # downscale images for faster processing
        imgR = cv.pyrDown(cv.imread('/home/vignesh/PycharmProjects/stereovision_trial/calib_images/obj_03_right.png'))

        window_size = PU.sad_window_size
        min_disp = PU.min_disparity
        num_disp = PU.num_disparity
        stereo = cv.StereoSGBM_create(minDisparity = min_disp,
            numDisparities = num_disp,
            blockSize = PU.block_size,
            P1 = PU.p1,
            P2 = PU.p2,
            disp12MaxDiff =PU.disp12maxdiff,
            uniquenessRatio = PU.uniqueness_ratio,
            speckleWindowSize = PU.speckle_window_size,
            speckleRange = PU.speckle_range
        )


        print('computing disparity...')
        disp = stereo.compute(imgL, imgR).astype(np.float32) / 16.0

        print('generating 3d point cloud...',)
        h, w = imgL.shape[:2]
        f = 0.8*w                          # guess for focal length
        Q = np.float32([[1, 0, 0, -0.5*w],
                        [0,-1, 0,  0.5*h], # turn points 180 deg around x-axis,
                        [0, 0, 0,     -f], # so that y-axis looks up
                        [0, 0, 1,      0]])
        points = cv.reprojectImageTo3D(disp, Q)
        colors = cv.cvtColor(imgL, cv.COLOR_BGR2RGB)
        mask = disp > disp.min()
        out_points = points[mask]
        out_colors = colors[mask]
        out_fn = 'out.ply'
        write_ply(out_fn, out_points, out_colors)
        print('%s saved' % out_fn)

        # cv.imshow('left', imgL)
        # cv.imshow('right', imgR)
        cv.imshow('disparity', (disp-min_disp)/num_disp)
        cv.waitKey(5)

        print('Done')


if __name__ == '__main__':
    print(__doc__)
    main()
    cv.destroyAllWindows()