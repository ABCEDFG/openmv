import sensor, time, image, pyb  

sensor.reset() # Initialize the camera sensor.
sensor.set_pixformat(sensor.GRAYSCALE) # or sensor.GRAYSCALE
sensor.set_framesize(sensor.B128X128) # or sensor.QQVGA (or others)
sensor.set_windowing((92,112))
sensor.skip_frames(10) # Let new settings take affect.
sensor.skip_frames(time = 5000) #�ȴ�5s



#SUB = "s1"
NUM_SUBJECTS = 6 #ͼ����в�ͬ������һ��6��
NUM_SUBJECTS_IMGS = 20 #ÿ����20������ͼƬ

# ���㵱ǰ������
img = sensor.snapshot()
#img = image.Image("singtown/%s/1.pgm"%(SUB))
d0 = img.find_lbp((0, 0, img.width(), img.height()))
#d0Ϊ��ǰ������lbp����
img = None
pmin = 999999
num=0

def min(pmin, a, s):
    global num
    if a<pmin:
        pmin=a
        num=s
    return pmin

for s in range(1, NUM_SUBJECTS+1):
    dist = 0
    for i in range(2, NUM_SUBJECTS_IMGS+1):
        img = image.Image("singtown/s%d/%d.pgm"%(s, i))
        d1 = img.find_lbp((0, 0, img.width(), img.height()))
        #d1Ϊ��s�ļ����еĵ�i��ͼƬ��lbp����
        dist += image.match_descriptor(d0, d1)#����d0 d1������ͼ���뱻�����������������ȡ�
    print("Average dist for subject %d: %d"%(s, dist/NUM_SUBJECTS_IMGS))
    pmin = min(pmin, dist/NUM_SUBJECTS_IMGS, s)#���������ԽС�����������������������Ƹ�ƥ�䡣
    print(pmin)

print(num) # numΪ��ǰ��ƥ����˵ı�š�