# coding: utf-8
# 作者: andysun
# 日期：2023-12-26
# 功能：检验SMT生成的Image的完整性
#import xml.etree.ElementTree as ET
import os
import sys
import readIni
#import writeLog
import writeResult
import array
import operator
import re
import messageBox
import TkDialog
#import tkinter as tk
from tkinter import messagebox
from ctypes import *
import jasonHandler
import datetime
import shutil
# 主函数
#unit_size_dict={"K":1024,"M":1048576,"G":1073741824}
#unit_size_dict={'1':1,'K':1024,'M':1048576,'G':1073741824}
ini_optionval_dict={'g_TarDir':'','NoLOG':False,'g_LogFname':'','g_RSTFname':'','zipExe':"\"C:\\Program Files\\7-Zip\\7z.exe\"",
                    'bAutoOpenLog':False,'g_bClear':False,'g_bZipAll':False,'skipDirName':[],'bLaunchDialog':False,'JSONSaveDirName':''}
#g_chunk_size = 1 #读取的字节数大小
g_TarDirName=''
#g_SMTImageName=''
#g_XMLFName=''
#g_LogFname=''
#g_RSTFname=''
#g_bClear=False
#g_bCheckAll=False
#g_myLogHandler=None
g_myRstHandler=None
#g_myBoxHandler=None
g_ZipResult=''
g_NotZipResult=''
g_JasonFPath=''
g_JSONSavePath=''
def string_to_int(s):
    #return ord(char)
    return int(s)
    
def char_to_int(char):
    #return ord(char)
    return int(char)
def extract_alnum( string):
    pattern = '[a-zA-Z0-9]+'
    result = re.findall(pattern,string)
    return result
def extract_num( string):
    pattern = '[0-9]+'
    result = re.findall(pattern,string)
    return string_to_int(result[0])

def extract_alpha( string):
    pattern = '[a-zA-Z]+'
    result = re.findall(pattern,string)
    return result
def extract_alpha_toUCase( string):
    pattern = '[a-zA-Z]+'
    s = re.findall(pattern,string)
    #print(string,s)    
    if s:
        result = s[0].upper()
    else:
        result ='1' 
    return result


def file_exists(file_path):
    return os.path.exists(file_path)

def bskipFolders(sFolderName,skipFolders):
    result=False
    #print(sFolderName)
    if ini_optionval_dict['g_bZipAll'] :
        #print("no skip")
        return result
    for item in skipFolders:
        if operator.eq(sFolderName, item):
            return True
    return result
def getBoolenFromINI(myIniHandler,section_name,option_name,bdefval):
    try:
        Opt=myIniHandler.getOptionValues(section_name,option_name)
        Opt=Opt.upper()
        if Opt == "Y":
            return True
        else:
            return False
    except :
        print(f"选项不存在:{option_name}")
        return bdefval
def getListItemFromINI(myIniHandler,section_name,option_name,defList):
    try:
        Opt=myIniHandler.getOptionValues(section_name,option_name)
        #print(Opt)
        return Opt.split(",")

    except :
        print(f"选项不存在:{option_name}")
        return defList
def getFileAttribute(file_path):
    # 获取文件属性
    file_stat = os.stat(file_path)     
    # 获取文件大小
    file_size = file_stat.st_size    
    # 获取文件最后一次访问时间
    access_time = file_stat.st_atime    
    # 获取文件最后一次修改时间
    modify_time = file_stat.st_mtime     
    # 获取文件的权限模式
    mode = file_stat.st_mode    
    # 获取文件的所有者ID
    owner_id = file_stat.st_uid    
    # 获取文件的所有者的用户名
    owner_name = os.getpwuid(owner_id).pw_name
##
def getFolderAttribute(folderList,folder_path):
    my_dict={}
    try:
        # 调用os模块的stat()函数获取文件夹属性
        folder_stats = os.stat(folder_path)
        #my_dict['name']=folder_stats.st_name
        my_dict['name']=os.path.basename(folder_path)      
        my_dict['st_size']=folder_stats.st_size
        #my_dict['st_atime']=folder_stats.st_atime
        #my_dict['st_mtime']=folder_stats.st_mtime        
        #my_dict['st_ctime']=folder_stats.st_ctime
        my_dict['st_mtime']=str(datetime.datetime.fromtimestamp(folder_stats.st_mtime))
        my_dict['st_ctime']=str(datetime.datetime.fromtimestamp(folder_stats.st_ctime))
        #print(datetime.datetime.fromtimestamp(folder_stats.st_mtime))       

##        # 获取文件夹的修改日期时间
##        modification_time = os.path.getmtime(folder_path)
##
##        # 将时间戳转换为可读的日期时间格式
##        modification_time_str = datetime.datetime.fromtimestamp(modification_time)

        
        folderList.append(my_dict)
        
    except FileNotFoundError:
        print("未找到该文件夹")
    return my_dict
		
def printFolderAttribute(folderList):
    for item in folderList:
        print(item) 	
		
def initGlobal():
#    global g_chunk_size
#    global g_TarDirName
#    global g_SMTImageName
#    global g_XMLFName
#    global g_XMLFName
#    global g_RSTFname
#    global g_bClear
#    global g_bCheckAll
#    global g_myLogHandler
    global g_myRstHandler
    #global g_myBoxHandler
    global ini_optionval_dict
    global g_JSONSavePath
    global g_JasonFPath
    iniCfgFPath="config.ini"
    myIniHandler=readIni.IniHandler(iniCfgFPath)    
    #myIniHandler.print_sections()
    #myIniHandler.getOptions('globalconfig')
    #myIniHandler.getItems('globalconfig')
    ini_optionval_dict['g_TarDir'] = myIniHandler.getOptionValues('globalconfig','TarDir')
    if not ini_optionval_dict['g_TarDir']:
        ini_optionval_dict['g_TarDir']=os.getcwd()	
    ini_optionval_dict['NoLOG'] = getBoolenFromINI(myIniHandler,'globalconfig','NoLOG',False)   
    ini_optionval_dict['g_bClear'] = getBoolenFromINI(myIniHandler,'globalconfig','ClearRST_Log',True)
#    ini_optionval_dict['g_LogFname'] = myIniHandler.getOptionValues('globalconfig','LogFname')
    ini_optionval_dict['g_RSTFname'] =myIniHandler.getOptionValues('globalconfig','RSTFname')	
    ini_optionval_dict['g_bZipAll'] = getBoolenFromINI(myIniHandler,'globalconfig','bNotZipifZFExists',False)   	
    ini_optionval_dict['skipDirName'] = getListItemFromINI(myIniHandler,'globalconfig','skipDirName',[''])
    ini_optionval_dict['bLaunchDialog'] = getBoolenFromINI(myIniHandler,'globalconfig','LaunchCfgDialogOnOpen',False)
    ini_optionval_dict['bAutoOpenLog'] = getBoolenFromINI(myIniHandler,'globalconfig','AutoOpenRunLog',False)
    ini_optionval_dict['zipExe'] = myIniHandler.getOptionValues('globalconfig','zipExePath')
    ini_optionval_dict['JSONSaveDirName'] = myIniHandler.getOptionValues('globalconfig','JSONSaveDirName')

#    g_myLogHandler=writeLog.LogHandler(ini_optionval_dict['g_LogFname'],ini_optionval_dict['g_bClear'])
    g_myRstHandler=writeResult.RstHandler(ini_optionval_dict['g_RSTFname'] ,ini_optionval_dict['g_bClear'] )

    g_JSONSavePath = os.path.join(os.getcwd(),ini_optionval_dict['JSONSaveDirName']) 
    if not os.path.exists(g_JSONSavePath):
        os.mkdir(g_JSONSavePath)
    g_JasonFPath = os.path.join(g_JSONSavePath,"curFolder.jason")

	
def is_list_empty(lst):
    if len(lst) == 0:
        return True
    else:
        return False
def ReleaseResource():
    if g_myRstHandler:
        g_myRstHandler.unload_File()
def writeResultToFile():
    if ini_optionval_dict['NoLOG']:
        ReleaseResource()
        return 
    msg=''
    if g_ZipResult :
        msg=msg+"压缩如下文件夹：\n"+g_ZipResult+"\n"
    if g_NotZipResult:
        msg=msg+"未压缩如下文件夹（zip档已存在)：\n"+g_NotZipResult+"\n"
    if not is_list_empty(ini_optionval_dict['skipDirName']):
        msg=msg+"跳过如下的文件夹：\n"+str(ini_optionval_dict['skipDirName'])+"\n"		

    g_myRstHandler.write_result(msg)    
    g_myRstHandler.write_EndDateTimeInfo("压缩结束!")
    ReleaseResource()
    sLogFPath=os.getcwd()+"\\"+ini_optionval_dict['g_RSTFname'] 
    g_myBoxHandler=messageBox.BoxHandler(ini_optionval_dict['bAutoOpenLog'],sLogFPath)
    g_myBoxHandler.display_message_box(msg)


    
def LaunchCfgDialog():
    if not ini_optionval_dict['bLaunchDialog']:
        print("not launch dialog")
        return True

    myTkDialogHandler=TkDialog.TkDialogHandler(ini_optionval_dict['g_TarDir'])
    while True:
        if myTkDialogHandler.bUserSelect():
            userdirpath = myTkDialogHandler.getDirPath()
            if userdirpath != "":
                #str_utf8=str(userdirpath).encode('utf-8')
                #str_utf8.decode('utf-8')
                ini_optionval_dict['g_TarDir']= userdirpath.decode('utf-8')
            #print(ini_optionval_dict['g_TarDir'])
            #root.destroy()
            break
        #else:
            #print("wait")
        
    return True


#def createzipCmd(DirName):
def zipFolder(DirName,path,zipath):
    #zipExe="\"C:\\Program Files\\7-Zip\\7z.exe\""
    zipExe="\""+ini_optionval_dict['zipExe']+"\""
    try:
        sCmd=f"{zipExe} a -t7z {zipath} {path}"
        print (sCmd)
        os.system(sCmd) 
    except :
        msg="压缩失败："+DirName+"\n"
        print(msg)
        g_myRstHandler.write_result(msg)
def getRecentJsonFile():
    feature=os.path.basename(ini_optionval_dict['g_TarDir'])
    #file_names = []
    latest_filename=''
    latest_modified_time=0
    # 创建一个指定时间的时间戳
    specified_time_int = int(datetime.datetime(2000, 9, 30).timestamp())
    latest_modified_time = datetime.datetime.fromtimestamp(specified_time_int)
    for root, dirs, files in os.walk(g_JSONSavePath):
        for file in files:
            if feature in file:
                #file_names.append(file)
	            # 获取文件的修改时间并转换为datetime格式
                #modified_time = datetime.utcfromtimestamp(os.stat(file).st_mtime)
                path = os.path.join(g_JSONSavePath, file)   
                modified_time = datetime.datetime.fromtimestamp(os.stat(path).st_mtime)
                # 更新最新的文件名和修改时间
                if latest_modified_time is None or modified_time > latest_modified_time:
                    latest_filename = file
                    latest_modified_time = modified_time			
        return latest_filename			
#为避免文件同名，而实际路径不同,可考虑在jason文件中，存完整的目标目录的完整路径。     
def backJasonResult():        
    dt = datetime.datetime.now()
    #timestamp = dt.timestamp()
    #dt_tomorrow = dt + datetime.timedelta(days=1)
    #dt_str = dt.strftime("%Y-%m-%d %H:%M:%S")
    dt_str = dt.strftime("%Y_%m_%d")
    #dt.year
    target_file = os.path.basename(ini_optionval_dict['g_TarDir'])+"_"+dt_str+".jason"
    target_Path= os.path.join(g_JSONSavePath,target_file) 
    shutil.copyfile(g_JasonFPath, target_Path)
def bfolderChange(JRecentData,curFoldAttr):
    if not JRecentData:
        return True
    if not curFoldAttr:
        return False    
    for data in JRecentData:  
        if data['name'] == curFoldAttr['name']:  
            if (data['st_size'] != curFoldAttr['st_size']) or (data['st_mtime'] !=  curFoldAttr['st_mtime']) or (data['st_ctime'] !=  curFoldAttr['st_ctime']) :
                return True           
            else:
                return False
            
    return True

def process():
    global g_ZipResult
    global g_NotZipResult     

    g_NotZipResult=''
    g_ZipResult=''
    if not file_exists(ini_optionval_dict['zipExe']):
        msg="压缩程序不存在，请检查ini配置。7z程序的默认路径为"+"\"C:\\Program Files\\7-Zip\\7z.exe\""+"\n"
        ReleaseResource()
        messagebox.showinfo('出错啊', msg)
        return 
    g_myRstHandler.write_StartDateTimeInfo("压缩开始")
    JHandler=jasonHandler.JasonHandler(g_JasonFPath,True)

    skipDirName=ini_optionval_dict['skipDirName']
    sRecentJFName=getRecentJsonFile()
    sRecentJFPath = os.path.join(g_JSONSavePath, sRecentJFName) 
    JRecentHandler=jasonHandler.JasonHandler(sRecentJFPath,False)
    JRecentData=JRecentHandler.readdata_json()
    msg="比对文件:"+sRecentJFName+"\n"
    print(msg)
    g_myRstHandler.write_result(msg)	
    TarDir=ini_optionval_dict['g_TarDir']
    names = os.listdir(TarDir)
    print(ini_optionval_dict['g_TarDir'])
    myfolderList=[]
    curFoldAttr={}
    #print(str(names))
    for name in names:
        zipFname=name+".7z"
        path = os.path.join(TarDir, name)
        zipath = os.path.join(TarDir, zipFname)
        if os.path.isdir(path):  
            print(name, " is dir")
            curFoldAttr=getFolderAttribute(myfolderList,path)
            if bskipFolders(name,skipDirName):
                #g_NotZipResult=g_NotZipResult+name+","
                continue
            else:
                if ini_optionval_dict['g_bZipAll']:
                    g_ZipResult=g_ZipResult+name+","            	
                    zipFolder(name,path,zipath)
                else:
                    
                    if file_exists(zipath):
                        if bfolderChange(JRecentData,curFoldAttr):
                            g_ZipResult=g_ZipResult+name+","            	
                            zipFolder(name,path,zipath)                             
                        else:                       
                            g_NotZipResult=g_NotZipResult+name+","   
                    else:
                        g_ZipResult=g_ZipResult+name+","            	
                        zipFolder(name,path,zipath)                        
                     
        #if os.path.isfile(path):  # 文件
        #    print(name, " is file")	
    JHandler.write_json_to_file(myfolderList)
    printFolderAttribute(myfolderList)
    writeResultToFile()
    JHandler.unload_File()
    JRecentHandler.unload_File()
    backJasonResult()
def main():
    initGlobal()
     
    if LaunchCfgDialog() :
        process()
if __name__ == '__main__':
    main()
