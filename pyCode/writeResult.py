# coding: utf-8
# 作者: andysun
# 日期：2023-12-26
# 功能：读取bin文件

import os
import time
import datetime
import logging


##创建Logger对象
#logger = logging.getLogger( 'mylogger )
#logger.setLevel(logging.DEBUG)
##创建FiLeHandLer对象
#fh = logging.FileHandler( 'mylog.log')
#fh.setLevel(logging.DEBUG)
##创建Formatter对象
#formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s ')
#fh.setFormatter(formatter)
##将FiLeHandLer对象添加到Logger对象中
#logger.addHandler(fh)



class RstHandler:
    def __init__(self, filepath,bClear):
        self.filepath = filepath  # XML文件路径
        self.file = None
        self.needClear=bClear
        self.startime=time.time()
        self.load_File()
    def load_File(self):   # 加载XML文件
        """
        加载文件。
        """
        try:
            if self.needClear:
                self.file = open(self.filepath, 'w')
                self.file.write('')
                self.file.close()
            self.file = open(self.filepath, 'a' )
        except :
            print(f"读取文件失败：{self.filepath}！")
    def write_StartDateTimeInfo(self,message):
        now = datetime.datetime.now()
        log_line = f"[{now.strftime('%Y-%m-%d %H:%M:%S')}] {message}\n"
        #with open(self.filepath, 'a') as file:
        if self.file : 
            self.file.write(log_line) 
        else:
            print(f"读取文件失败：{self.filepath}！")
    def write_EndDateTimeInfo(self,message):
        now = datetime.datetime.now()
        log_line = f"[{now.strftime('%Y-%m-%d %H:%M:%S')}] {message}\n"
        #with open(self.filepath, 'a') as file:
        elapsed_time = time.time() - self.startime
        log_time=f"总耗时：{elapsed_time}秒\n"
        #
        #print("代码运行耗时：%s" % elapsed_time)
        if self.file : 
            self.file.write(log_time) 
            self.file.write(log_line)
        else:
            print(f"读取文件失败：{self.filepath}！")
    def write_result(self,message):
        if self.file : 
            self.file.write(message) 
        else:
            print(f"读取文件失败：{self.filepath}！")
    
    def unload_File(self):   # 加载XML文件
        if self.file:
            self.file.close()
if __name__ == '__main__':
	pass