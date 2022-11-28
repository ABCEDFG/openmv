import sensor, image, time

sensor.reset() # 初始化摄像头
sensor.set_pixformat(sensor.RGB565) # 格式为 RGB565.
sensor.set_framesize(sensor.QQVGA)
sensor.skip_frames(10) # 跳过10帧，使新设置生效

while(True):
    img = sensor.snapshot()         # 拍照并返回图像
    
    img.draw_line((20, 30, 40, 50))  # 划线
    img.draw_line((80, 50, 100, 100), color=(255,0,0))  # 划线 颜色
    img.draw_rectangle((20, 30, 41, 51), color=(255,0,0))  # 画矩形
    img.draw_circle(50, 50, 30)  # 画圆 x,y,r
    img.draw_cross(90,60,size=10)  # 画十字架 x,y,长
    img.draw_string(10,10, "hello world!")  # 写字 x,y,字符串  \n可用