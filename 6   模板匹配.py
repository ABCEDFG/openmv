import time, sensor, image
from image import SEARCH_EX, SEARCH_DS
#从imgae模块引入SEARCH_EX和SEARCH_DS。使用from import仅仅引入SEARCH_EX,
#SEARCH_DS两个需要的部分，而不把image模块全部引入。

# 复位传感器
sensor.reset()

# 设置传感器设置
sensor.set_contrast(1)
sensor.set_gainceiling(16)
# 与搜索引擎匹配的最大分辨率为QVGA
sensor.set_framesize(sensor.QQVGA)
# 您可以设置窗口以减少搜索图像.
#sensor.set_windowing(((640-80)//2, (480-60)//2, 80, 60))
sensor.set_pixformat(sensor.GRAYSCALE)

# 加载模板.
# 模板应该是一个小的（例如32x32像素）灰度图像
template = image.Image("/template.pgm")
#加载模板图片 

clock = time.clock()  #返回一个时钟对象

# 运行模板匹配
while (True):
    clock.tick()  # 开始计算运行时间
    img = sensor.snapshot()  # 拍摄一张照片

    # 查找模板（模板、阈值、[roi、步骤、搜索]）
    # ROI: 感兴趣区域元组 (x, y, w, h).
    # Step: 使用的循环步骤 (y+=step, x+=step) 使用更大的步骤使其更快.
    # 搜索可以是image.Search\u EX进行穷举搜索，也可以是image.Search\u DS进行菱形搜索
    #
    # Note1: ROI必须小于图像，大于模板.
    # Note2: 在菱形搜索中，步长和ROI都被忽略.
    r = img.find_template(template, 0.70, step=4, search=SEARCH_EX) #, roi=(10, 0, 60, 60))
    #find_template(template, threshold, [roi, step, search]),threshold中
    #的0.7是相似度阈值,roi是进行匹配的区域（左上顶点为（10，0），长80宽60的矩形）
    #注意roi的大小要比模板图片大，比frambuffer小。
    #把匹配到的图像标记出来
    if r:
        img.draw_rectangle(r)  # 绘制一个矩形

    print(clock.fps())  # 打印帧数
