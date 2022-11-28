import sensor, image, time

# 要使颜色跟踪工作得很好，理想情况下，你应该处于一个非常非常，
# 非常，受控的环境，照明是恒定的。。。
yellow_threshold   = ( 56,   83,    5,   57,   63,   80)
# 您可能需要调整以上设置以跟踪绿色内容。。。
# 在帧缓冲区中选择一个区域以复制颜色设置。

sensor.reset() # 初始化摄像头传感器。
sensor.set_pixformat(sensor.RGB565) #使用RGB565。
sensor.set_framesize(sensor.QQVGA) # 使用QVGA提高速度。
sensor.skip_frames(10) #让新设置生效。
sensor.set_auto_whitebal(False) # 把这个关掉。
clock = time.clock() #跟踪FPS。

K=5000  # 应测量该值

while(True):
    clock.tick() # 跟踪快照之间经过的毫秒数。
    img = sensor.snapshot() # 拍摄一张照片并返回图像。

    blobs = img.find_blobs([yellow_threshold])
    if len(blobs) == 1:
        # 在水滴周围画一个矩形。
        b = blobs[0]
        img.draw_rectangle(b[0:4]) # rect
        img.draw_cross(b[5], b[6]) # cx, cy
        Lm = (b[2]+b[3])/2
        length = K/Lm
        print(length)

    #print(clock.fps()) #注意：您的OpenMV Cam运行速度约为
    # 已连接到您的计算机。一旦断开连接，FPS应增加。
