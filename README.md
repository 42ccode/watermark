Readme 文件
项目简介 (Project Introduction)
中文
本项目旨在提供一个简单的图片水印添加工具，通过Python脚本实现批量给指定文件夹中的图片添加水印的功能。用户只需输入想要添加的水印内容，脚本将自动遍历指定文件夹中的所有图片，并为每张图片添加半透明水印。

English
This project aims to provide a simple image watermarking tool, implemented through a Python script that enables batch watermarking of images in a specified folder. Users simply input the desired watermark text, and the script automatically iterates through all images in the specified folder, adding a semi-transparent watermark to each one.

使用说明 (Usage Guide)
中文
准备工作：确保你的环境中已安装Python，并且安装了watermarker库（如果未安装，可以通过pip install watermarker命令安装）。
放置图片：将你想要添加水印的图片放置在同一文件夹下，例如img_1。
运行脚本：将本脚本放置在图片文件夹的同级目录下，运行脚本。脚本将提示你输入水印信息。
输入水印：根据提示输入你想要的水印内容，脚本将自动为所有图片添加水印。
查看结果：水印添加完成后，你可以在图片文件夹中查看带有水印的图片。
English
Preparation：Ensure that Python is installed in your environment, and that the watermarker library is also installed (if not, you can install it via pip install watermarker).
Place Images：Place the images you want to watermark in the same folder, for example img_1.
Run the Script：Place this script in the same directory as the image folder and run it. The script will prompt you to enter the watermark text.
Enter Watermark：Enter the desired watermark text as prompted, and the script will automatically add watermarks to all images.
View Results：Once the watermarking is complete, you can view the watermarked images in the image folder.
注意事项 (Notes)
请确保img_1文件夹中存在图片，否则脚本将不会执行任何操作。
水印的透明度（opacity）在脚本中已设置为0.5，但你可以根据需要修改这个值。
本脚本仅适用于支持由watermarker库处理的图片格式。
贡献者 (Contributors)
感谢所有参与贡献和提出改进建议的人。
此Readme文件提供了项目的中英文介绍、使用说明以及注意事项，旨在帮助用户快速了解和使用该图片水印添加工具。