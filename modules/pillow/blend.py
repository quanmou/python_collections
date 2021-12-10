"""
图像混合

透明度混合主要是使用Image中的blend(im1, im2, alpha) 方法，对该方法的解释如下：
im1：Image对象，在混合的过程中，透明度设置为（1-apha）
im2：Image对象，在混合的过程中，透明度设置为（apha）
alpha：透明度，取值是0-1。当透明度为0是，显示im1对象；当透明度为1时，显示im2对象

注意：im1和im2的大小必须一样，且mode都为RGB
"""

from PIL import Image

# 打开im1
im1 = Image.open('1.png').convert(mode='RGB')
# 创建一个和im1大小一样的图像
im2 = Image.new('RGB', im1.size, 'red')
# 混合图片，并显示
Image.blend(im1, im2, 0.5).show()
