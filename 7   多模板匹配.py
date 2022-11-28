import time, sensor, image
from image import SEARCH_EX, SEARCH_DS
#从imgae模块引入SEARCH_EX和SEARCH_DS。使用from import仅仅引入SEARCH_EX, 
#SEARCH_DS两个需要的部分，而不把image模块全部引入。

# Reset sensor
sensor.reset()

# 设置传感器设置
sensor.set_contrast(1)  # 设置相机对比度 -3~+3
sensor.set_gainceiling(16)  # 设置相机增益上限
# 与搜索引擎匹配的模板的最大分辨率为QVGA
sensor.set_framesize(sensor.QQVGA)  #设置分辨率
# 您可以设置窗口以减少搜索图像。
#sensor.set_windowing(((640-80)//2, (480-60)//2, 80, 60))
sensor.set_pixformat(sensor.GRAYSCALE)  #设置相机的像素模式

# 加载模板.
# 模板应该是一个小的（如32x32像素）灰度图像。
templates = ["/0.pgm", "/1.pgm", "/2.pgm", "/6.pgm"] #保存多个模板
#加载模板图片

clock = time.clock()

# Run template matching
while (True):
    clock.tick()
    img = sensor.snapshot()

    # 查找模板（模板、阈值、[roi、步骤、搜索]）
    # 感兴趣区域元组（x，y，w，h）
    # 步骤：使用的循环步骤（y+=步骤，x+=步骤）使用更大的步骤使其更快.
    # 搜索可以是image.Search\u EX进行穷举搜索，也可以是image.Search\u DS进行菱形搜索
    #
    # 注1：ROI必须小于图像且大于模板.
    # 注2：在菱形搜索中，step和ROI都被忽略.
    for t in templates:
        template = image.Image(t)
        #对每个模板遍历进行模板匹配
        r = img.find_template(template, 0.70, step=4, search=SEARCH_EX) #, roi=(10, 0, 60, 60))
    #find_template(template, threshold, [roi, step, search]),threshold中
    #的0.7是相似度阈值,roi是进行匹配的区域（左上顶点为（10，0），长80宽60的矩形），
    #注意roi的大小要比模板图片大，比frambuffer小。
    #把匹配到的图像标记出来
        if r:
            img.draw_rectangle(r)
            print(t) #打印模板名字

    #print(clock.fps())