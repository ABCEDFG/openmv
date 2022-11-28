import sensor, time, image

# ���ô�����
sensor.reset()

# ����������
sensor.set_contrast(3)
sensor.set_gainceiling(16)
sensor.set_framesize(sensor.VGA)
sensor.set_windowing((320, 240))
sensor.set_pixformat(sensor.GRAYSCALE)

sensor.skip_frames(time = 2000)
sensor.set_auto_gain(False, value=100)

FILE_NAME = "desc"
img = sensor.snapshot()
# ע�⣺������ĵ��鿴��������
# ע��Ĭ������£�find_keypoints���ش�ͼ������ȡ�Ķ�߶ȹؼ��㡣
kpts = img.find_keypoints(max_keypoints=150, threshold=10, scale_factor=1.2)

if (kpts == None):
    raise(Exception("Couldn't find any keypoints!"))

image.save_descriptor(kpts, "/%s.orb"%(FILE_NAME))
img.save("/%s.pgm"%(FILE_NAME))

img.draw_keypoints(kpts)
sensor.snapshot()
time.sleep_ms(1000)
raise(Exception("Done! Please reset the camera"))