import os
import random
from PIL import Image, ImageDraw, ImageFont, ImageFilter

root_dir = os.path.dirname(os.path.abspath(__file__))


# 随机字母
def rand_char():
    return chr(random.randint(65, 90))


# 随机颜色1
def rand_color():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))


# 随机颜色2
def rand_color_2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))


# 240 x 60
width, height = 60 * 4, 60
image = Image.new('RGB', (width, height), (255, 255, 255))

# 创建Font对象
font = ImageFont.truetype('Arial.ttf', 36)  # 36是字体大小
# 创建Draw对象
draw = ImageDraw.Draw(image)
# 填充每个像素
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rand_color())

# 输出文字
for t in range(4):
    draw.text((60 * t + 10, 10), rand_char(), font=font, fill=rand_color_2())

# 模糊
image = image.filter(ImageFilter.BLUR)
image.save(root_dir + '/images/code.jpg', 'jpeg')
