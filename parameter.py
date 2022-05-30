#----------------------------路径相关参数---------------------------

raw_dataset_path = 'D:/test-use/zhifangtu'  #没做预处理的输入数据路径

raw_ct_path = 'D:/test-use/zhifangtu/vol' #原始ct路径路径

raw_seg_path = 'D:/test-use/zhifangtu/seg' #金标准的数据路径

fixed_dataset_path = 'D:/test-use/zhifangtu' #预处理后的数据集根路径

fixed_ct_path = 'D:/test-use/zhifangtu/vol' #预处理后的原始ct路径

fixed_seg_path = 'D:/test-use/zhifangtu/seg' #预处理后的金标准数据路径

#----------------------路径相关参数----------------------------------------

#------------------------------训练数据获取相关参数---------------------------

upper , lower = 200 ,-200  #CT数据灰度阶段窗口

down_scale = 0.5 #横断面降采样因子

size = 48 #使用48张连续切片作为网络的输入

slice_thickness = 1  # 将所有数据在z轴的spacing归一化到1mm

expand_slice = 20  # 仅使用包含肝脏以及肝脏上下20张切片作为训练样本

#------------------------------训练数据获取相关参数---------------------------
