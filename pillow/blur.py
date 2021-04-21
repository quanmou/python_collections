import os
from PIL import Image, ImageFilter

root_dir = os.path.dirname(os.path.abspath(__file__))

# 打开一个jpg图像文件，注意是当前路径
im = Image.open(root_dir + '/images/test.jpeg')
# 应用模糊滤镜
im2 = im.filter(ImageFilter.BLUR)
im2.save(root_dir + '/images/blur.jpg', 'jpeg')
