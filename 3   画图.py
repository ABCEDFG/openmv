import sensor, image, time

sensor.reset() # ��ʼ������ͷ
sensor.set_pixformat(sensor.RGB565) # ��ʽΪ RGB565.
sensor.set_framesize(sensor.QQVGA)
sensor.skip_frames(10) # ����10֡��ʹ��������Ч

while(True):
    img = sensor.snapshot()         # ���ղ�����ͼ��
    
    img.draw_line((20, 30, 40, 50))  # ����
    img.draw_line((80, 50, 100, 100), color=(255,0,0))  # ���� ��ɫ
    img.draw_rectangle((20, 30, 41, 51), color=(255,0,0))  # ������
    img.draw_circle(50, 50, 30)  # ��Բ x,y,r
    img.draw_cross(90,60,size=10)  # ��ʮ�ּ� x,y,��
    img.draw_string(10,10, "hello world!")  # д�� x,y,�ַ���  \n����