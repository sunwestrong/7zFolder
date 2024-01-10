# coding: utf-8
# 作者: andysun
# 日期：2023-12-26
# 功能：读取bin文件

import os
import time
import datetime
import json



class JasonHandler:
    def __init__(self, filepath,bClear):
        self.filepath = filepath  # XML文件路径
        self.rfile = None
        self.wfile = None		
        self.needClear=bClear
        self.load_File()
    def load_File(self):   # 加载XML文件
        """
        加载文件。
        """
        try:
            if self.needClear:
                self.wfile = open(self.filepath, 'w')
                self.wfile.write('')
                self.wfile.close()
            self.wfile = open(self.filepath, 'a' )
            self.rfile = open(self.filepath, 'r' )
        except :
            print(f"读取文件失败：{self.filepath}！")

    def write_json_to_file(self,json_data):
        if self.wfile : 
            json.dump(json_data, self.wfile)
            self.wfile.write('\n')
        else:
            print(f"读取文件失败：{self.filepath}！")
    def readdata_json(self):
        data=None
        if self.rfile:
            #data = pd.read_json(file_path)
            data = json.load(self.rfile)  
        else:
            print(f"读取文件失败：{self.filepath}！")
 
        return data
    
    def unload_File(self):   # 加载XML文件
        if self.wfile:
            self.wfile.close()
        if self.rfile:
            self.rfile.close()
if __name__ == '__main__':
	pass