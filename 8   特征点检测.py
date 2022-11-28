import sensor, time, image

# Reset sensor
sensor.reset()

# Sensor settings
sensor.set_contrast(3)  # ��������Աȶ� -3~+3
sensor.set_gainceiling(16)  # ���������������
sensor.set_framesize(sensor.VGA)  #  ���÷ֱ���
sensor.set_windowing((320, 240))  # ���ô���
sensor.set_pixformat(sensor.GRAYSCALE)  # ������������ģʽ �Ҷ�

sensor.skip_frames(time = 2000)  # ����2s
sensor.set_auto_gain(False, value=100)  # ����100�ֱ��Ĺ̶�����

#����������
def draw_keypoints(img, kpts):  
    if kpts:
        print(kpts)
        img.draw_keypoints(kpts)
        img = sensor.snapshot()
        time.sleep_ms(1000)

kpts1 = None
#kpts1����Ŀ����������������Դ��ļ��������������ǲ�������ô����
#kpts1 = image.load_descriptor("/desc.orb")
#img = sensor.snapshot()
#draw_keypoints(img, kpts1)

clock = time.clock()

while (True):
    clock.tick()  # ��������ʱ��
    img = sensor.snapshot()  # ����
    if (kpts1 == None):
        #����Ǹտ�ʼ���г�����ȡ�ʼ��ͼ����ΪĿ������������kpts1����Ŀ�����������
        #Ĭ�ϻ�ƥ��Ŀ�������Ķ��ֱ�����С�����������Ǳ���Ŀ������ʱ�Ĵ�С����ģ��ƥ����
        # ע�⣺Ĭ������£�find_keypoints���ش�ͼ���������ȡ�Ķ�����ؼ��㡣
        kpts1 = img.find_keypoints(max_keypoints=150, threshold=10, scale_factor=1.2)
        # image.find_keypoints(roi=Auto,threshold=20,normalized=False,scale_factor=1.5,max_keypoints=100,corner_detector=CORNER_AGAST)
        # roi��ʾʶ���������һ��Ԫ�飨x,y,w,h��,Ĭ����framsesize��Сһ�¡�
        # threshold��0~255��һ����ֵ������������������Ľǵ���������Ĭ�ϵ�AGAST�������⣬�����ֵ�����20��
        #   ��FAST�������⣬�����ֵ�����60��80����ֵԽ�ͣ���õĽǵ�Խ�ࡣ
        # normalized��һ��������ֵ��Ĭ����False������ƥ��Ŀ�������Ķ��ִ�С����nccģ��ƥ��Ч������
        #   �������ΪTrue���ر���������Ķ�����������ƥ��Ŀ��������һ�ִ�С��������ģ��ƥ�䣩�����������ٶȻ����һЩ��
        # scale_factor��һ������1.0�ĸ������������ֵԽ�ߣ�����ٶ�Խ�죬����ƥ��׼ȷ�ʻ��½���һ����1.35~1.5������ѡ�
        # max_keypoints��һ���������ȡ���������������������һ�������������̫�ർ��RAM�ڴ汬������С�����ֵ��
        # corner_detector�����������ȡ���㷨��Ĭ����AGAST�㷨��FAST�㷨����쵫��׼ȷ�ʻ��½���
        draw_keypoints(img, kpts1) 
      
        #������ʱ��Ŀ������
    else:
        #�����ʼ��Ŀ����������ƥ��ʱ��Ĭ������normalized=True��ֻƥ��Ŀ��������һ�ִ�С��
        # NOTE: When extracting keypoints to match the first descriptor, we use normalized=True to extract
        # keypoints from the first scale only, which will match one of the scales in the first descriptor.
        kpts2 = img.find_keypoints(max_keypoints=150, threshold=10, normalized=True)
        #�����⵽��������
        if (kpts2):
            #ƥ�䵱ǰ�ҵ��������������Ŀ�����������ƶ�
            match = image.match_descriptor(kpts1, kpts2, threshold=85)
            #image.match_descriptor(descritor0, descriptor1, threshold=70, filter_outliers=False)������������kptmatch����
            #threshold��ֵ����ƥ���׼ȷ�ȣ��������˵��������ƥ�䡣���ֵԽС��׼ȷ��Խ�ߡ���ֵ��Χ0��100��Ĭ��70
            #filter_outliersĬ�Ϲرա�

            #match.count()��kpt1��kpt2��ƥ��Ľ�����������Ŀ��
            #�������10��֤�������������ƣ�ƥ��ɹ���
            if (match.count()>10):
                # If we have at least n "good matches"
                # Draw bounding rectangle and cross.
                #��ƥ�䵽��Ŀ���������Ļ�ʮ�ֺ;��ο�
                img.draw_rectangle(match.rect())
                img.draw_cross(match.cx(), match.cy(), size=10)

            #match.theta()��ƥ�䵽�������������Ŀ���������ת�Ƕȡ�
            print(kpts2, "matched:%d dt:%d"%(match.count(), match.theta()))
            #������draw_keypoints���������ǵ㡣
            # NOTE: uncomment if you want to draw the keypoints
            #img.draw_keypoints(kpts2, size=KEYPOINTS_SIZE, matched=True)

    # Draw FPS
    #��ӡ֡�ʡ�
    img.draw_string(0, 0, "FPS:%.2f"%(clock.fps()))