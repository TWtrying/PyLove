#coding:utf-8
from os import system,path

if path.isfile("config"):
    pass
else:
    f = open('config','w')
    f.close()
print('*******************************')
print("以下是您电脑屏幕的信息:")
system("wmic desktopmonitor get ScreenWidth,ScreenHeight")
print("请输入ScreenHeight:",end='')
h = input()
print("请输入ScreenWidth:",end='')
w = input()
f = open("config",'w')
f.write(str(w)+'\n'+str(h))
print('*******************************')
print(' 配置成功!')
system('pause')