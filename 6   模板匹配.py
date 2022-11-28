import time, sensor, image
from image import SEARCH_EX, SEARCH_DS
#��imgaeģ������SEARCH_EX��SEARCH_DS��ʹ��from import��������SEARCH_EX,
#SEARCH_DS������Ҫ�Ĳ��֣�������imageģ��ȫ�����롣

# ��λ������
sensor.reset()

# ���ô���������
sensor.set_contrast(1)
sensor.set_gainceiling(16)
# ����������ƥ������ֱ���ΪQVGA
sensor.set_framesize(sensor.QQVGA)
# ���������ô����Լ�������ͼ��.
#sensor.set_windowing(((640-80)//2, (480-60)//2, 80, 60))
sensor.set_pixformat(sensor.GRAYSCALE)

# ����ģ��.
# ģ��Ӧ����һ��С�ģ�����32x32���أ��Ҷ�ͼ��
template = image.Image("/template.pgm")
#����ģ��ͼƬ 

clock = time.clock()  #����һ��ʱ�Ӷ���

# ����ģ��ƥ��
while (True):
    clock.tick()  # ��ʼ��������ʱ��
    img = sensor.snapshot()  # ����һ����Ƭ

    # ����ģ�壨ģ�塢��ֵ��[roi�����衢����]��
    # ROI: ����Ȥ����Ԫ�� (x, y, w, h).
    # Step: ʹ�õ�ѭ������ (y+=step, x+=step) ʹ�ø���Ĳ���ʹ�����.
    # ����������image.Search\u EX�������������Ҳ������image.Search\u DS������������
    #
    # Note1: ROI����С��ͼ�񣬴���ģ��.
    # Note2: �����������У�������ROI��������.
    r = img.find_template(template, 0.70, step=4, search=SEARCH_EX) #, roi=(10, 0, 60, 60))
    #find_template(template, threshold, [roi, step, search]),threshold��
    #��0.7�����ƶ���ֵ,roi�ǽ���ƥ����������϶���Ϊ��10��0������80��60�ľ��Σ�
    #ע��roi�Ĵ�СҪ��ģ��ͼƬ�󣬱�frambufferС��
    #��ƥ�䵽��ͼ���ǳ���
    if r:
        img.draw_rectangle(r)  # ����һ������

    print(clock.fps())  # ��ӡ֡��
