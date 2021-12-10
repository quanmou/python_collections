import os
from PIL import Image

root_dir = os.path.dirname(os.path.abspath(__file__))

# 打开一个jpg图像文件，注意是当前路径
im = Image.open(root_dir + '/images/test.jpeg')
# 获得图像尺寸
w, h = im.size
print('Original image size: %s x %s' % (w, h))

# 缩放50%，thumbnail是直接在原图上修改，resize是生成新的图
im.thumbnail((w//2, h//2), Image.ANTIALIAS)
# im = im.resize((w//2, h//2), Image.ANTIALIAS)  # resize还可以用来放大，thumbnail只能缩小
print('Resize image to: %s x %s' % (w//2, h//2))

# 把缩放后的图像用jpeg格式保存
im.save(root_dir + '/images/thumbnail.jpg', 'jpeg')
