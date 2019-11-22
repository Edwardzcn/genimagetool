#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Flask
from flask import render_template, request,  redirect
from PIL import Image, ImageDraw, ImageFont


app = Flask(__name__)
app.secret_key = 'edwardzcn'
id_dict = {}
"""
这是一个根据学号生成对应号码图片的Flask小项目

"""


@app.route('/')
def home():
    return render_template('index.html', title="Choose Your Number")


@app.route('/genimage/<gen_id>')
def gen_image(gen_id):
    return render_template('genimage.html', gen_id=gen_id)


@app.route('/login', methods=['GET', 'POST'])
def log_in():
    # request:请求对象 --> 获取请求方式、数据
    # 1.判断请求方式
    if request.method == 'POST':
        studentid = request.form.get('studentid')
        if check_length(studentid) is True:
            num, find = check_num(studentid)
            imageWriterRow("./static/images/bg_row.jpg", num)
            imageWriterCol("./static/images/bg_col.jpg", num)
            return redirect('/genimage/'+"%04d" % num)
        else:
            render_template('index.html', idwrong=False)
    return render_template('login.html')


def check_length(studentid):
    # 长度和字符要求
    if len(studentid.strip()) == 10:
        for ch in studentid:
            if ch < '0' or ch > '9':
                return False
        return True
    else:
        return False


# def create_dict(dic_path): {
#     file = open('test.txt', 'r')
#     for line in file:
#         print(line)
#     file.close()
# }


def check_num(studentid):
    # id_dict = create_dict(dic_path)
    find = studentid in id_dict
    length = len(id_dict)
    if find is False:
        id_dict[studentid] = length+1
    return id_dict[studentid], find


def imageWriterRow(filePath, number):
    strnumber = "%04d" % number
    print(strnumber)
    img = Image.open(filePath)
    size = img.size
    # 确定大小
    # fontSize = size[1] / 4
    draw = ImageDraw.Draw(img)
    # ttFont = ImageFont.truetype('ahronbd.ttf', 50)
    ttFont = ImageFont.truetype("msyh.ttc", 120, encoding="unic")
    # ttFont = ImageFont.truetype("arial.ttf", 120, encoding="unic")
    draw.text((size[0]/3*1.9, size[1]/3*1), strnumber,
              fill=(255, 255, 255), font=ttFont)
    img.save("./static/images/gen_row_" + strnumber + ".jpg", quality=95)


def imageWriterCol(filePath, number):
    strnumber = "%04d" % number
    print(strnumber)
    img = Image.open(filePath)
    size = img.size
    # 确定大小
    # fontSize = size[1] / 4
    draw = ImageDraw.Draw(img)
    # ttFont = ImageFont.truetype('ahronbd.ttf', 50)
    ttFont = ImageFont.truetype("msyh.ttc", 60, encoding="unic")
    draw.text((size[0]/3, size[1]/3*1.2), strnumber,
              fill=(255, 255, 255), font=ttFont)
    img.save("./static/images/gen_col_" + strnumber + ".jpg", quality=95)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
