import os
import shutil
import nibabel as nib
import glob
import imageio
import numpy as np
import multiprocessing
from utils.preprocessing_utils_png import sitk2slices, sitk2labels
import SimpleITK as sitk


if __name__ == '__main__':
    fixed_raw_path = 'D:/test-use/zhifangtu/vol/'
    fixed_label_path = 'D:/test-use/zhifangtu/seg/'
    # tr_path = 'D:/p-200-200/tr/'
    # ts_path = 'D:/p-200-200/ts/'
    tr_raw_path = 'D:/test-use/zhifangtu/seg-1/'
    tr_label_path = 'D:/test-use/zhifangtu/vol-1/'
    # ts_raw_path = 'D:/p-200-200/LITS/pred-nii/ts_vol_png/'
    # ts_label_path = 'D:/p-200-200/LITS/pred-nii/ts_label_png/'

    # for i in range(28):
    #     print(i)
    #     ct = sitk.ReadImage(fixed_raw_path +'volume-'+str(i)+'.nii',sitk.sitkInt16)
    #     ct_array = np.rot90(sitk.GetArrayFromImage(ct))
    #     ct_array = np.rot90(ct_array)
    #
    #     seg = sitk.ReadImage(fixed_label_path+'segmentation-'+str(i)+'.nii',sitk.sitkInt16)
    #     seg_array = np.rot90(sitk.GetArrayFromImage(seg))
    #     seg_array = np.rot90(seg_array)
    #
    #     slices_in_order = sitk2slices(ct_array,0,400)
    #     labels_in_order = sitk2labels(seg_array)
    #     for n in range(len(slices_in_order)):
    #         imageio.imwrite(ts_raw_path +str(i)+'_'+str(n).zfill(4)+'.png', slices_in_order[n].astype(np.uint8))
    #         imageio.imwrite(ts_label_path+str(i)+'_'+str(n).zfill(4)+'.png', labels_in_order[n].astype(np.uint8))

    for i in range(29, 30):
        print(i)
        ct = sitk.ReadImage(fixed_raw_path+ 'volume-' + str(i) + '.nii', sitk.sitkInt16)
        ct_array = np.rot90(sitk.GetArrayFromImage(ct))
        ct_array = np.rot90(ct_array)

        seg = sitk.ReadImage(fixed_label_path+ 'segmentation-' + str(i) + '.nii', sitk.sitkInt16)
        seg_array = np.rot90(sitk.GetArrayFromImage(seg))
        seg_array = np.rot90(seg_array)

        slices_in_order = sitk2slices(ct_array,0,2000)
        labels_in_order = sitk2labels(seg_array)
        for n in range(len(slices_in_order)):
            imageio.imwrite(tr_raw_path+str(i)+'_'+str(n).zfill(4)+'.png', slices_in_order[n].astype(np.uint8))
            imageio.imwrite(tr_label_path+str(i)+'_'+str(n).zfill(4)+'.png', labels_in_order[n].astype(np.uint8))