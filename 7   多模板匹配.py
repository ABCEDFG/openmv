import time, sensor, image
from image import SEARCH_EX, SEARCH_DS
#��imgaeģ������SEARCH_EX��SEARCH_DS��ʹ��from import��������SEARCH_EX, 
#SEARCH_DS������Ҫ�Ĳ��֣�������imageģ��ȫ�����롣

# Reset sensor
sensor.reset()

# ���ô���������
sensor.set_contrast(1)  # ��������Աȶ� -3~+3
sensor.set_gainceiling(16)  # ���������������
# ����������ƥ���ģ������ֱ���ΪQVGA
sensor.set_framesize(sensor.QQVGA)  #���÷ֱ���
# ���������ô����Լ�������ͼ��
#sensor.set_windowing(((640-80)//2, (480-60)//2, 80, 60))
sensor.set_pixformat(sensor.GRAYSCALE)  #�������������ģʽ

# ����ģ��.
# ģ��Ӧ����һ��С�ģ���32x32���أ��Ҷ�ͼ��
templates = ["/0.pgm", "/1.pgm", "/2.pgm", "/6.pgm"] #������ģ��
#����ģ��ͼƬ

clock = time.clock()

# Run template matching
while (True):
    clock.tick()
    img = sensor.snapshot()

    # ����ģ�壨ģ�塢��ֵ��[roi�����衢����]��
    # ����Ȥ����Ԫ�飨x��y��w��h��
    # ���裺ʹ�õ�ѭ�����裨y+=���裬x+=���裩ʹ�ø���Ĳ���ʹ�����.
    # ����������image.Search\u EX�������������Ҳ������image.Search\u DS������������
    #
    # ע1��ROI����С��ͼ���Ҵ���ģ��.
    # ע2�������������У�step��ROI��������.
    for t in templates:
        template = image.Image(t)
        #��ÿ��ģ���������ģ��ƥ��
        r = img.find_template(template, 0.70, step=4, search=SEARCH_EX) #, roi=(10, 0, 60, 60))
    #find_template(template, threshold, [roi, step, search]),threshold��
    #��0.7�����ƶ���ֵ,roi�ǽ���ƥ����������϶���Ϊ��10��0������80��60�ľ��Σ���
    #ע��roi�Ĵ�СҪ��ģ��ͼƬ�󣬱�frambufferС��
    #��ƥ�䵽��ͼ���ǳ���
        if r:
            img.draw_rectangle(r)
            print(t) #��ӡģ������

    #print(clock.fps())