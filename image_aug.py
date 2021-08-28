import Augmentor

# 确定原始图像存储路径以及掩码文件存储路径
p = Augmentor.Pipeline("D:/test-use/seg")
p.ground_truth("D:/test-use/vol")

# 图像旋转： 按照概率0.8执行，最大左旋角度10，最大右旋角度10
# p.rotate(probability=0.5, max_left_rotation=20, max_right_rotation=20)

# 图像左右互换： 按照概率0.5执行
# p.flip_left_right(probability=0.8)

# # # 图像放大缩小： 按照概率0.8执行，面积为原始图0.85倍
# p.zoom_random(probability=1, percentage_area=0.8)
# 弹性形变 magnitude形变的程度
# p.skew_corner(probability=0.8, magnitude=0.5)
#
# p.flip_random(probability=0.8)
# 最终扩充的数据样本数
p.sample(20)
