#����ʾ��
#
#ע�⣺���д�ʾ����ҪSD����
#
#������ʹ��OpenMV Cam����ͼ���ļ���


import sensor, image, pyb

RED_LED_PIN = 1
BLUE_LED_PIN = 3

sensor.reset() #��ʼ������ͷ��������
sensor.set_pixformat(sensor.GRAYSCALE) #�򴫸����Ҷ�
sensor.set_framesize(sensor.B128X128) # ��sensor.qvga����������
sensor.set_windowing((92,112))
sensor.skip_frames(10) # ����������Ч��
sensor.skip_frames(time = 2000)

num = 1 #���ñ���������ţ���һ���˵�ͼƬ���浽s1�ļ��У��ڶ����˵�ͼƬ���浽s2�ļ��У��Դ����ơ�ÿ�θ���������ʱ���޸�numֵ��

n = 20 #����ÿ��������ͼƬ������

#��������n����Ƭ��ÿ���3s����һ�Ρ�
while(n):
    #�����
    pyb.LED(RED_LED_PIN).on()
    sensor.skip_frames(time = 3000) # ���û�׼����ʱ�䡣�ȴ�3s��׼��һ�±��顣

    #�����������
    pyb.LED(RED_LED_PIN).off()
    pyb.LED(BLUE_LED_PIN).on()

    #�����ȡ����ͼƬ��SD��
    print(n)
    sensor.snapshot().save("singtown/s%s/%s.pgm" % (num, n) ) #��example.bmp������������

    n -= 1

    pyb.LED(BLUE_LED_PIN).off()
    print("Done! Reset the camera to see the saved image.")
