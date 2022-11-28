import sensor, image, time

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QQVGA)
sensor.skip_frames(time = 2000)
sensor.set_auto_gain(False) # ����ر���ɫ����
sensor.set_auto_whitebal(False) # ����ر���ɫ����
clock = time.clock()

while(True):
    clock.tick()
    img = sensor.snapshot().lens_corr(1.8)
    for c in img.find_circles(threshold = 3500, x_margin = 10, y_margin = 10, r_margin = 10,
            r_min = 2, r_max = 100, r_step = 2):
        area = (c.x()-c.r(), c.y()-c.r(), 2*c.r(), 2*c.r())
        #areaΪʶ�𵽵�Բ�����򣬼�Բ����Ӿ��ο�
        statistics = img.get_statistics(roi=area)#������ɫͳ��
        print(statistics)
        #(0,100,0,120,0,120)�Ǻ�ɫ����ֵ�����Ե������ڵ�������Ҳ����������ɫ������Χ�������ֵ�ڣ���˵���Ǻ�ɫ��Բ��
        #l_mode()��a_mode()��b_mode()��Lͨ����Aͨ����Bͨ����������
        if 0<statistics.l_mode()<100 and 0<statistics.a_mode()<127 and 0<statistics.b_mode()<127:#if the circle is red
            img.draw_circle(c.x(), c.y(), c.r(), color = (255, 0, 0))#ʶ�𵽵ĺ�ɫԲ���ú�ɫ��Բ�����
        else:
            img.draw_rectangle(area, color = (255, 255, 255))
            #���Ǻ�ɫ��Բ�ð�ɫ�ľ��ο����
    print("FPS %f" % clock.fps())

