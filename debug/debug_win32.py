# Author: SH
# Data: 2019/3/14
# Status 
# Comment:

import time
from pywinauto import application
app= application.Application().start('notepad.exe')
app.Notepad.MenuSelect('帮助->关于记事本')
time.sleep(2)
# 这里有两种方法可以进行定位“关于记事本”的对话框
about_dlg= app.window_(title_re="关于",class_name="#32770")# 这里可以进行正则匹配title
app.window_(title_re='关于“记事本”').window_(title_re='确定').Click()
ABOUT= '关于“记事本”'
OK= '确定'
# about_dlg[OK].Click()
# app[ABOUT][OK].Click()
app['关于“记事本”']['确定'].Click()
app.Notepad.TypeKeys("my damao")
dig= app.Notepad.MenuSelect("编辑(E)->替换(R)")
Replace= '替换'
Cancle= '取消'
time.sleep(2)
app[Replace][Cancle].Click()
dialogs= app.windows_()


