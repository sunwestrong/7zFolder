# coding: utf-8
# 作者: andysun
# 日期：2023-12-26
# 功能：读取bin文件

import os

import tkinter as tk
from tkinter.filedialog import *
#import tkinter.filedialog as tkdialog

class TkDialogHandler:
#    def __init__(self,root,initialdir):
    def __init__(self,initialdir):
        #self.root = root
        self.button= None
        #self.msg=''
        #self.xmlfilename = ''#None tk.StringVar()
        #self.imgfilename = ''#None #tk.StringVar()
        #self.dirpath = '' #None #tk.StringVar()
        self.bSelect=False
        self.initialdir=initialdir
        self.load()

    def load(self):   # 加载XML文件
        """
        加载XML文件并解析为ElementTree对象。
        """
        # 创建一个Tkinter窗口
        try:
        #    #print("try to read：{self.filepath}")
        #    #self.root = Tk()
            self.root = Tk()
            self.root.geometry ( '600x600')
            self.root.title( '设置目标')
            self.xmlfilename = tk.StringVar()
            self.imgfilename = tk.StringVar()   
            self.dirpath =  tk.StringVar()   			
        except :
            print(f"root赋值失败！")
        #self.create_Dialog()
        try:
            self.create_Dialog()
        except :
            print(f"Dialog创建失败！")
        try:
        ## 创建一个Button控件
        #    self.button = tk.Button(self.root,text="确定",font=("微软雅黑",12))
        #    #self.button.config(command=self.callback()) ##self.callback()无法响应，只会第一次显示，要改为
        #    self.button.config(command=self.callback)
        #    #self.button= Button(text="确定",font=("微软雅黑",12),command=self.callback)
        #    #self.button.pack()
        #    # 进入消息循环
            self.root.mainloop()   
        except :
            print(f"进入消息循环失败！")

        
    def create_Dialog(self):
        
        # 创建一个Label控件
        #label = Label(self.root,text="请选择您的操作：")
        #label.pack()
         # 打开文件
        #tk.Label(self.root, text='选择XML文件').grid(row=1, column=0, padx=5, pady=5)
        #tk.Entry(self.root, textvariable=self.xmlfilename).grid(row=1, column=1, padx=5, pady=5)
        #tk.Button(self.root, text='打开XML文件', command=self.openXMLFile).grid(row=1, column=2, padx=5, pady=5)
        # # 打开文件
        #tk.Label(self.root, text='选择IMAGE文件').grid(row=2, column=0, padx=5, pady=5)
        #tk.Entry(self.root, textvariable=self.imgfilename).grid(row=2, column=1, padx=5, pady=5)
        #tk.Button(self.root, text='打开IMAGE文件', command=self.openIMAGEFile).grid(row=2, column=2, padx=5, pady=5)        
        # 选择目录
        tk.Label(self.root, text='选择目录').grid(row=1, column=0, padx=5, pady=5) # 创建label 提示这是选择目录
        tk.Entry(self.root, textvariable=self.dirpath).grid(row=1, column=1, padx=5, pady=5) # 创建Entry，显示选择的目录
        tk.Button(self.root, text='打开目录', command=self.openDir).grid(row=1, column=2, padx=5, pady=5) # 创建一个Button，点击弹出打开目录窗口
        self.button=tk.Button(self.root, text='确定', command=self.callback).grid(row=2, column=1, padx=5, pady=5) # 创建一个Button，确认
        ## 进入消息循环
        #self.root.mainloop()
    def openXMLFile(self):
        filepath = askopenfilename(filetypes=[('All Files', '*.xml')],title="打开xml文件",
                                   initialfile='Hi3751V560-slaveboot-emmc.xml',
                                   initialdir=self.initialdir)  # 选择打开什么文件，返回文件名
        if filepath.strip() != '':
            self.xmlfilename.set(filepath)
            #self.xmlfilename=filepath# 设置变量filename的值
        else:
            print("do not choose xml file")

    def openIMAGEFile(self):
        filepath = askopenfilename(filetypes=[('All Files', '*.img')],title="打开img文件",
                                   initialfile='release.img',
                                   initialdir=self.initialdir)
        if filepath.strip() != '':
            self.imgfilename.set(filepath)  # 设置变量filename的值
            #self.imgfilename=filepath
        else:
            print("do not choose xml file")

    def openDir(self):
        fileDir = askdirectory()  # 选择目录，返回目录名
        if fileDir.strip() != '':
            self.dirpath.set(fileDir)  # 设置变量outputpath的值
            #self.dirpath=fileDir
        else:
            print("do not choose Dir")
    #def fileSave():
    #    filenewpath = asksaveasfilename(defaultextension='.txt')  # 设置保存文件，并返回文件名，指定文件名后缀为.txt
    #    if filenewpath.strip() != '':
    #        filenewname.set(filenewpath)  # 设置变量filenewname的值
    #    else:
    #        print("do not save file")
    #
    
    #    return 
    # 点击Button控件时的响应函数

    def StrVal2Str(self,sStrVal):
        if sStrVal!= b'':		    
            strtxt = str(sStrVal.get()).encode('utf-8')
			#print("Not NUll"+strtxt)
        else:
            strtxt=""
			#print("NUll")
        return strtxt
    def callback(self):
        print("您点击了确认！")
        self.bSelect=True
        self.root.destroy()
    def bUserSelect(self):
        return self.bSelect
    def getxmlFilename(self):
        #if self.xmlfilename:
        #    return self.xmlfilename
        #else :
        #     return None
        return self.StrVal2Str(self.xmlfilename)
    def getimgFilename(self):
        #if self.imgfilename:
        #    return self.imgfilename
        #else :
        #     return None
        return self.StrVal2Str(self.imgfilename)
    def getDirPath(self):
        #if self.dirpath:
        #    return self.dirpath
        #else :
        #    return None
        return self.StrVal2Str(self.dirpath)
if __name__ == '__main__':
    pass
    
