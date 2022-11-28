import sensor, image

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QQVGA) 
sensor.skip_frames(30)
sensor.set_auto_gain(False) # ����رմ�ѡ���Է�ֹͼ��ϴ��

while(True):
    img = sensor.snapshot()
    img.lens_corr(1.8) # 1.8��ǿ�ȶ���2.8���׵ľ�ͷ�Ǻܺõġ�
    for code in img.find_qrcodes():
        print(code)
