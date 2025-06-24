from PIL import Image

img = Image.open("b.jpeg")

r, g, b = img.split()
r.show()
# g.show()
# b.show()