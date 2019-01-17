# -*- coding: utf-8 -*-

#通过指定群聊的好友的头像，创建一个全村希望的头像

import itchat
import math
import PIL.Image as Image
import os
import sys
import random
import time

#这里是要设置的东西：
chatroomName=input("请输入群名：")#群聊名称
alpha = 0.3 #合成图片的 透明度比例

itchat.auto_login()

def map(chatroomName):
    num = 0

    chatrooms = itchat.get_chatrooms(update=True)
    for item in chatrooms:
        print (item["NickName"])

    chatrooms = itchat.search_chatrooms(name=chatroomName)
    if chatrooms is None:
        print(u'没有找到群聊：' + chatroomName)
    else:
        if not os.path.exists("./" + chatroomName):
            os.mkdir("./" + chatroomName)
            
        chatroom = itchat.update_chatroom(chatrooms[0]['UserName'])

        counter = 0
        for friend in chatroom['MemberList']:
            img = itchat.get_head_img(userName=friend["UserName"],chatroomUserName=chatrooms[0]['UserName'])
            fileImage = open("./" + chatroomName + "/" + str(counter) + ".jpg", 'wb')
            counter = counter + 1
            try:
                fileImage.write(img)
            except:
                try:
                    print (friend["NickName"] + "  error.")
                except:
                    print (friend["UserName"] + "  error.")
            fileImage.close()
            num += 1

w = 640


# 头像拼接图
def createImg(chatroomName):
    x = 0
    y = 0
    imgs = os.listdir(chatroomName)
    random.shuffle(imgs)
    # 创建640*640的图片用于填充各小图片
    newImg = Image.new('RGBA', (w, w))
    # 以640*640来拼接图片，math.sqrt()开平方根计算每张小图片的宽高，

    width = int(math.sqrt(w * w / len(imgs)))
    # 每行图片数
    numLine = int(w / width)

    if numLine * numLine < len(imgs):
        numLine = numLine+1 

    i = 0
    while i < numLine * numLine:
        if i < len(imgs):
            try:
                img = Image.open(chatroomName + "/" + imgs[i]);
            except Exception as err:
                print(err)
                i = i+1
                continue
        else:
            try:
                img = Image.open(chatroomName + "/" + imgs[i % len(imgs)]);
            except Exception as err:
                print(err)
                i = i+1
                continue

        i = i + 1
        # 缩小图片
        img = img.resize((width, width), Image.ANTIALIAS)
        # 拼接图片，一行排满，换行拼接
        newImg.paste(img, (x * width, y * width))
        x += 1
        if x >= numLine:
            x = 0
            y += 1

        newImg.save("all.png")


# 皮一下
def QuanCunXiWang():
    icon1 = Image.open("全村底图.png")
    icon2 = Image.open("all.png")

    newim2 = Image.blend(icon1, icon2, alpha)
    newim2.save(chatroomName+'.png', "PNG")


def create(chatroomName):        

    map(chatroomName)
    createImg(chatroomName)
    QuanCunXiWang()
    if __name__ == '__main__':

        if not os.path.exists("./"+chatroomName):
            os.makedirs("./"+chatroomName)

def re_exe(n,inc): 
    for i in range(n):
        start = time.perf_counter()
        create(chatroomName)
        end = time.perf_counter()
        dur = end-start
        print("time cost{:.2f}".format(dur))
        print("代码主体来源GiHub之vullagehope项目-joe-zxh，添加微信非好友功能，添加键入功能，添加计时功能-inorimisasagi")
        time.sleep(inc)
        

re_exe(100,60)
        
        
        


