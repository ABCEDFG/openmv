import sensor,image,lcd,time

#摄像头初始化
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.set_vflip(1) #后置模式，所见即所得

#lcd初始化
lcd.init()

clock=time.clock()

# 颜色识别阈值 (L Min, L Max, A Min, A Max, B Min, B Max) LAB模型
# 下面的阈值元组是用来识别 红、绿、蓝三种颜色，当然你也可以调整让识别变得更好。
thresholds = [(30, 100, 15, 127, 15, 127), # 红色阈值
              (30, 100, -64, -8, -32, 32), # 绿色阈值
              (0, 30, 0, 64, -128, -20)] # 蓝色阈值

while True:

    clock.tick()  #开始追踪运行时间

    img=sensor.snapshot()  # 拍摄一张照片

    blobs = img.find_blobs([thresholds[2]]) # 0,1,2分别表示红，绿，蓝色。
    if blobs:
        for b in blobs:
            tmp=img.draw_rectangle(b[0:4])  # 画框
            tmp=img.draw_cross(b[5], b[6])  # 画十字

    lcd.display(img)     #LCD显示图片
    print(clock.fps())   #打印FPS（帧数）