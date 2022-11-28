#快照示例
#
#注意：运行此示例需要SD卡。
#
#您可以使用OpenMV Cam保存图像文件。


import sensor, image, pyb

RED_LED_PIN = 1
BLUE_LED_PIN = 3

sensor.reset() #初始化摄像头传感器。
sensor.set_pixformat(sensor.GRAYSCALE) #或传感器灰度
sensor.set_framesize(sensor.B128X128) # 或sensor.qvga（或其他）
sensor.set_windowing((92,112))
sensor.skip_frames(10) # 让新设置生效。
sensor.skip_frames(time = 2000)

num = 1 #设置被拍摄者序号，第一个人的图片保存到s1文件夹，第二个人的图片保存到s2文件夹，以此类推。每次更换拍摄者时，修改num值。

n = 20 #设置每个人拍摄图片数量。

#连续拍摄n张照片，每间隔3s拍摄一次。
while(n):
    #红灯亮
    pyb.LED(RED_LED_PIN).on()
    sensor.skip_frames(time = 3000) # 给用户准备的时间。等待3s，准备一下表情。

    #红灯灭，蓝灯亮
    pyb.LED(RED_LED_PIN).off()
    pyb.LED(BLUE_LED_PIN).on()

    #保存截取到的图片到SD卡
    print(n)
    sensor.snapshot().save("singtown/s%s/%s.pgm" % (num, n) ) #或“example.bmp”（或其他）

    n -= 1

    pyb.LED(BLUE_LED_PIN).off()
    print("Done! Reset the camera to see the saved image.")
