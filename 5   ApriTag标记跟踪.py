import sensor, image, time, math

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QQVGA) # ����ֱ��ʴ�ö࣬�ڴ��������
sensor.skip_frames(30)
sensor.set_auto_gain(False)  # ����رմ�ѡ���Է�ֹͼ��ϴ��...
sensor.set_auto_whitebal(False)  # ����رմ�ѡ���Է�ֹͼ��ϴ��...
clock = time.clock()

while(True):
    clock.tick()  # ��ʼ��������ʱ��
    img = sensor.snapshot()  # ����һ����Ƭ
    for tag in img.find_apriltags(): # Ĭ��ΪTAG36H11������ "families"  ���� roi �ڵ�����AprilTag
        img.draw_rectangle(tag.rect(), color = (255, 0, 0))  # ����
        img.draw_cross(tag.cx(), tag.cy(), color = (0, 255, 0))  # ��ʮ��
        degress = 180 * tag.rotation() / math.pi  # ����Ƕ�
        print(tag.id(),degress)  # �������ͽǶ�