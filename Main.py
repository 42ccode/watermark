from watermarker.marker import add_mark
import os

files = os.listdir('img_1')  # 传如文件夹路径
mark = input("请输入您要添加的水印信息:")
for file in files:
    add_mark(f'img_1/{file}', mark=mark, opacity=0.5)  # mark为水印信息
