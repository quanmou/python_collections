import os
from PIL import Image

root_dir = os.path.dirname(os.path.abspath(__file__))

# 打开一个jpg图像文件，注意是当前路径
im = Image.open(root_dir + '/images/test.jpeg')
# 获得图像尺寸
w, h = im.size
print('Original image size: %s x %s' % (w, h))

# 缩放50%
im.thumbnail((w//2, h//2))
print('Resize image to: %s x %s' % (w//2, h//2))

# 把缩放后的图像用jpeg格式保存
im.save(root_dir + '/images/thumbnail.jpg', 'jpeg')
