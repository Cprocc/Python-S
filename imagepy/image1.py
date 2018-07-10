from PIL import Image
img = Image.open("wqy.jpg")     # 打开一个图片，并返回图片对象
w,h = img.size      # 返回图片宽，高
if h > 100:
    w = int(100/h * w)
    h = int(100 / 2)
img = img.convert('L')    # 转换为灰度，img.show()可查看图片
img = img.resize((w,h))   # 将图片重新以（w,h）尺寸存储
f = open("1.txt", "w")
chars = list("!@#$&*-+")
for y in range(h):
    line = ''
    for x in range(w):
        line += chars[ img.getpixel((x,y)) // 32 ]    # getpixel 获取该位置的像素信息
    f.write("%s%s" % (line, '\n'))
f.close()
print("转换成功")