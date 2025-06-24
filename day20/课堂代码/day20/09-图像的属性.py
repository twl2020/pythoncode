from PIL import Image


im = Image.open("b.jpeg")
print(im.mode)
print(im.format)
print(im.size)