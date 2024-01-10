# coding: utf-8
# 作者: andysun
# 日期：2023-12-26
# 功能：读取bin文件

import os
import tkinter as tk
from tkinter import messagebox
#import subprocess

class BoxHandler:
    def __init__(self,bAutoOpenLog,sLogFPath):
        self.root = None
        self.msg=''
        self.bopenLog=bAutoOpenLog
        self.sLogFPath=sLogFPath
        self.load()

    def load(self):   # 加载XML文件
        """
        加载XML文件并解析为ElementTree对象。
        """
        try:
            #print("try to read：{self.filepath}")
            self.root = tk.Tk()
        except :
            print(f"root赋值失败！")
    def close_message_box(self):
        messagebox.showinfo("Message Box", self.msg)
        self.root.after(3000,self.root.destroy)# 3000毫秒后关闭弹窗
    def display_message_box(self,msg):
        self.msg=msg
        if self.root:
            self.root.withdraw()#隐藏主窗口
            #self.root.after(0,close_message_box())
            self.root.after(0,self.close_message_box())
            self.root.mainloop()
            if self.bopenLog:
                if self.sLogFPath:
                    print(f"try to open:{self.sLogFPath}") 
                    #subprocess.run([ "open", self.sLogFPath])
                    os.system(f"notepad {self.sLogFPath}") 

if __name__ == '__main__':
	pass