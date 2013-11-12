#coding:utf-8
import time
import pynotify
import os
def message(message):
	pynotify.init("EyeDefender")
	notice=pynotify.Notification(message)
	notice.show()
	return

s=0
while s<=3600:
   time.sleep(1)
   s+=1
   if s==3600:
   	message(u'Нүдээ амраах цаг боллоо!')
   	s=0
