# coding: utf-8
# 作者: andysun
# 日期：2023-12-26
# 功能：读取bin文件

import os
import configparser

class IniHandler:
    def __init__(self, filepath):
        self.filepath = filepath  # XML文件路径
        self.file = None
        self.load_ini()
    def load_ini(self):   # 加载XML文件
        """
        加载文件。
        """
        try:
            #print("try to read：{self.filepath}")
            #print("try to read：",self.filepath)
            #实例化一个configparser对象
            self.config = configparser.ConfigParser()
            #path为ini文件的存放路径，最好为绝对路径，获取文件绝对路径的方法，另有文详细描述config.read(path,encoding=" utf8")
            self.config.read(self.filepath,encoding=" utf8")
        except :
            print(f"读取文件失败：{self.filepath}！")
    def print_sections(self):
        # 获取ini文件中的所有section
        sections = self.config.sections()
        print("所有section:", sections)
    def getOptions(self,section_name):   # 加载XML文件
        # 获取指定section中的所有option
        options = self.config.options(section_name)
        #print("指定section中的所有option:", options)
        return options
    def getItems(self,section_name):   # 加载XML文件
        # 获取指定section中的所有option
        items = self.config.items(section_name)
        #print("指定section中的所有健值对:", items)
        return items
    def getOptionValues(self,section_name,option_name):   # 加载XML文件
        # 获取指定section中的所有option
        values = self.config.get(section_name,option_name)
        #print(f"指定{section_name}中的指定{option_name}的值:", values)
        return values
if __name__ == '__main__':
	pass