"""
绘制图形样式
fmt = '[marker][line][color]'

np.info(plt.plot)


color颜色表示：
  1. 使用matplotlib内置的颜色缩写
      b: blue
      k: black
  2. 使用颜色的英文单词
  3. 使用颜色的十六进制
       三原色： rgb
       三位表示法：#000(黑色)  -- #fff(白色)
       六位表示法：#000000(黑色)  -- #ffffff(白色)

       rgba = a表示alpha透明通道
       00(透明) - ff(不透明)
       想看见颜色： 不透明
       #rgba
       #rrggbbaa

"""
import numpy as np
import matplotlib.pyplot as plt

# 准备正弦曲线的xy坐标
x = np.linspace(0, np.pi * 2)
y = np.sin(x)

# 将以上的xy绘制通过折线图绘制出来
# plt.plot(x, y, "r-.^")
# plt.plot(x, y, color="pink")
# plt.plot(x, y, c="deepskyblue")
plt.plot(x, y, c="#ff0000ff")

# 为了能够看见绘制的图表， 需要将程序阻塞， 不往下执行
# show方法的作用就是显示图标， 同时程序会被阻塞
plt.show()
