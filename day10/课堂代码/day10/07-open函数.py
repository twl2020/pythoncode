"""
open(file, mode="r", encoding="cp936"): 打开一个文件并返回流

模式mode:
四种主要的模式：
  1. r: read_only 表示只能读， 默认值
  2. w: writable 表示只能写
     - 如果文件不存在， 会创建文件
     - 如果文件存在， 会覆盖文件
  3. a: append 表示追加， 也只能写
     - 如果文件不存在， 会创建文件
     - 如果文件存在， 在原有文件内容后面继续追加内容
  4. x: create  表示创建文件， 也只能写
      - 如果文件不存在， 会创建文件
      - 如果文件存在， 会报错
 以上四种模式是独立的， 不能共存。

模式中的+号：
  以上的四种主要模式后面是可以跟+号的
  +号表示补充缺失的功能，+号只能补充读数据或者写数据的功能

  r+: r本身具备读数据的功能， +在这里补充就是写数据的功能
  w+: w本身具备写数据的功能， +在这里补充就是读数据的功能
  a+: w本身具备写数据的功能， +在这里补充就是读数据的功能
  x+: w本身具备写数据的功能， +在这里补充就是读数据的功能

模式中设置读写数据的格式：
    t: text文本的意思， 也就是按照字符串格式读写数据， 默认值
    b: binary二进制数据的意思，也就是字节的格式读写数据。 常用于在 图像，音视频等文件上。  万能的

什么样的文件读写数据的时候才能使用t格式呢？？
   只要使用window自带的记事本打开该文件， 数据不乱码就可以使用t格式。

encoding: 表示读写文件的时候使用的字符编码
cp936: 表的是GBK


"""
f = open("test/a.txt", mode="w+t", encoding="UTF-8")
print(f)

f.write("我爱你，python")
# tell()： 返回当前文件中数据的指针位置
print(f.tell())  # 3
# seek(): 设置指针的位置
f.seek(0)
print(f.read())