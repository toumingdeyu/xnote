# -*- coding:utf-8 -*-  
# Created by xupingmao on 2017/03/25
# 

"""报时"""

import os
import time
import xutils

def mac_say(msg):
    os.system("say %s" % msg)

def windows_say(msg):
    import comtypes.client as cc
    # dynamic=True不生成静态的Python代码
    voice = cc.CreateObject("SAPI.SpVoice", dynamic=True)
    voice.Speak(msg)

class handler:

    def GET(self):
        try:
            tm = time.localtime()
            if tm.tm_hour >= 0 and tm.tm_hour <= 6:
                return False
            if tm.tm_hour == 7 and tm.tm_min < 30:
                return False
            if tm.tm_min == 0:
                msg = "现在时间是%s点整" % tm.tm_hour
            else:
                msg = "现在时间是%s点%s分" % (tm.tm_hour, tm.tm_min)
            if tm.tm_hour >= 23:
                msg += "，夜深了，请注意休息"
            if xutils.is_windows():
                return windows_say(msg)
            elif xutils.is_mac():
                return mac_say(msg)
            # voice.Release()
            return dict(code="success", message="")
        except Exception as e:
            return dict(code="fail", message=str(e))
        else:
            pass
        finally:
            pass