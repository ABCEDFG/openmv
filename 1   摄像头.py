import sensor#����й�Ԫ����ģ��

# ��������ͷ
sensor.reset()#��ʼ���й�Ԫ��
sensor.set_pixformat(sensor.RGB565)#����Ϊ��ɫ
sensor.set_framesize(sensor.QVGA)#����ͼ��Ĵ�С
sensor.skip_frames()#����n����Ƭ���ڸ������ú�����һЩ֡���ȴ��й�Ԫ�����ȶ���

# һֱ����
while(True):
    img = sensor.snapshot()#����һ����Ƭ��imgΪһ��image����