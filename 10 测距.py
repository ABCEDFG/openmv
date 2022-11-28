import sensor, image, time

# Ҫʹ��ɫ���ٹ����úܺã���������£���Ӧ�ô���һ���ǳ��ǳ���
# �ǳ����ܿصĻ����������Ǻ㶨�ġ�����
yellow_threshold   = ( 56,   83,    5,   57,   63,   80)
# ��������Ҫ�������������Ը�����ɫ���ݡ�����
# ��֡��������ѡ��һ�������Ը�����ɫ���á�

sensor.reset() # ��ʼ������ͷ��������
sensor.set_pixformat(sensor.RGB565) #ʹ��RGB565��
sensor.set_framesize(sensor.QQVGA) # ʹ��QVGA����ٶȡ�
sensor.skip_frames(10) #����������Ч��
sensor.set_auto_whitebal(False) # ������ص���
clock = time.clock() #����FPS��

K=5000  # Ӧ������ֵ

while(True):
    clock.tick() # ���ٿ���֮�侭���ĺ�������
    img = sensor.snapshot() # ����һ����Ƭ������ͼ��

    blobs = img.find_blobs([yellow_threshold])
    if len(blobs) == 1:
        # ��ˮ����Χ��һ�����Ρ�
        b = blobs[0]
        img.draw_rectangle(b[0:4]) # rect
        img.draw_cross(b[5], b[6]) # cx, cy
        Lm = (b[2]+b[3])/2
        length = K/Lm
        print(length)

    #print(clock.fps()) #ע�⣺����OpenMV Cam�����ٶ�ԼΪ
    # �����ӵ����ļ������һ���Ͽ����ӣ�FPSӦ���ӡ�
