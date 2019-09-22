# 使用zxing读取二维码
import zxing

reader = zxing.BarCodeReader()
barcode = reader.decode("baidu.png")
print(barcode.parsed)