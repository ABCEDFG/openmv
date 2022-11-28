import sensor, image

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QQVGA) 
sensor.skip_frames(30)
sensor.set_auto_gain(False) # 必须关闭此选项以防止图像被洗掉

while(True):
    img = sensor.snapshot()
    img.lens_corr(1.8) # 1.8的强度对于2.8毫米的镜头是很好的。
    for code in img.find_qrcodes():
        print(code)
