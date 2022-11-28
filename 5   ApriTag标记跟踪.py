import sensor, image, time, math

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QQVGA) # 如果分辨率大得多，内存就用完了
sensor.skip_frames(30)
sensor.set_auto_gain(False)  # 必须关闭此选项以防止图像被洗掉...
sensor.set_auto_whitebal(False)  # 必须关闭此选项以防止图像被洗掉...
clock = time.clock()

while(True):
    clock.tick()  # 开始计算运行时间
    img = sensor.snapshot()  # 拍摄一张照片
    for tag in img.find_apriltags(): # 默认为TAG36H11，不带 "families"  查找 roi 内的所有AprilTag
        img.draw_rectangle(tag.rect(), color = (255, 0, 0))  # 画框
        img.draw_cross(tag.cx(), tag.cy(), color = (0, 255, 0))  # 画十字
        degress = 180 * tag.rotation() / math.pi  # 计算角度
        print(tag.id(),degress)  # 输出距离和角度