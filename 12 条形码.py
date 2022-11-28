import sensor, image, time, math

sensor.reset()
sensor.set_pixformat(sensor.GRAYSCALE)
sensor.set_framesize(sensor.VGA) # 高分辨率！
sensor.set_windowing((640, 80)) # V Res为80==更少的工作（速度为2倍时为40）。
sensor.skip_frames(30)
sensor.set_auto_gain(False)  #必须关闭此选项以防止图像被洗掉。。。
sensor.set_auto_whitebal(False)  # 必须关闭此选项以防止图像被洗掉。。。
clock = time.clock()

# 条形码检测可以在OpenMV Cam的完整640x480分辨率下运行
# OV7725摄像机模块。条形码检测也将在RGB565模式下工作，但在
# 较低的分辨率。也就是说，条形码检测需要更高的分辨率
# 为了工作良好，它应该始终以640x480的灰度运行。。。

def barcode_name(code):
    if(code.type() == image.EAN2):
        return "EAN2"
    if(code.type() == image.EAN5):
        return "EAN5"
    if(code.type() == image.EAN8):
        return "EAN8"
    if(code.type() == image.UPCE):
        return "UPCE"
    if(code.type() == image.ISBN10):
        return "ISBN10"
    if(code.type() == image.UPCA):
        return "UPCA"
    if(code.type() == image.EAN13):
        return "EAN13"
    if(code.type() == image.ISBN13):
        return "ISBN13"
    if(code.type() == image.I25):
        return "I25"
    if(code.type() == image.DATABAR):
        return "DATABAR"
    if(code.type() == image.DATABAR_EXP):
        return "DATABAR_EXP"
    if(code.type() == image.CODABAR):
        return "CODABAR"
    if(code.type() == image.CODE39):
        return "CODE39"
    if(code.type() == image.PDF417):
        return "PDF417"
    if(code.type() == image.CODE93):
        return "CODE93"
    if(code.type() == image.CODE128):
        return "CODE128"

while(True):
    clock.tick()
    img = sensor.snapshot()
    codes = img.find_barcodes()
    for code in codes:
        img.draw_rectangle(code.rect())
        print_args = (barcode_name(code), code.payload(), (180 * code.rotation()) / math.pi, code.quality(), clock.fps())
        print("Barcode %s, Payload \"%s\", rotation %f (degrees), quality %d, FPS %f" % print_args)
    if not codes:
        print("FPS %f" % clock.fps())
