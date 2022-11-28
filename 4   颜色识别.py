import sensor,image,lcd,time

#����ͷ��ʼ��
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.set_vflip(1) #����ģʽ������������

#lcd��ʼ��
lcd.init()

clock=time.clock()

# ��ɫʶ����ֵ (L Min, L Max, A Min, A Max, B Min, B Max) LABģ��
# �������ֵԪ��������ʶ�� �졢�̡���������ɫ����Ȼ��Ҳ���Ե�����ʶ���ø��á�
thresholds = [(30, 100, 15, 127, 15, 127), # ��ɫ��ֵ
              (30, 100, -64, -8, -32, 32), # ��ɫ��ֵ
              (0, 30, 0, 64, -128, -20)] # ��ɫ��ֵ

while True:

    clock.tick()  #��ʼ׷������ʱ��

    img=sensor.snapshot()  # ����һ����Ƭ

    blobs = img.find_blobs([thresholds[2]]) # 0,1,2�ֱ��ʾ�죬�̣���ɫ��
    if blobs:
        for b in blobs:
            tmp=img.draw_rectangle(b[0:4])  # ����
            tmp=img.draw_cross(b[5], b[6])  # ��ʮ��

    lcd.display(img)     #LCD��ʾͼƬ
    print(clock.fps())   #��ӡFPS��֡����