【关联程序】
7zip压缩程序官网下载地址：（也可通过腾讯管家等下载）
https://www.7-zip.org/

【功能说明】
调用7z程序，批量压缩当前目录下的各子目录。

【应用场景】
主要用于个人资料的批量压缩备份，尤其是不公开的code档案、个人总结文档等。

【配置说明】
TarDir =                                                             ###目标目录。值为空时，默认执行本程序所在目录。
bNotZipifZFExists=N                                          ### 强制压缩选项。取值为Y：当存在子文件夹目录名.7z时，不进行压缩 ；取值为N:当存在子文件夹目录名.7z时，仍进行压缩。
skipDirName=                                                    ###需跳过的子目录，如开发工具,skipDirName=FFmpeg,Python 。用,区隔，默认为空。
NoLOG =N                                                         ### 是否不输出日志。
RSTFname = result.txt                                        ### 日志文件名。
ClearRST_Log = Y                                               ### 清除日志和结果。取值为Y：每次执行前，清除log文件（即只保存当前执行的结果）；取值为 N:不清除log文件。
LaunchCfgDialogOnOpen= Y                             ### 运行本程序时，是否先弹出选项对话框。取值为Y:压缩前，弹出设置文件夹目录设置选择对话框； 取值为N:不弹出对话框，按ini配置的TarDir进行压缩。
AutoOpenRunLog= N                                        ### 自动打开result.txt文件选项。取值为Y:程序运行完成后，自动打开result.txt文件; 取值为N:不自动打开。
zipExePath=C:\Program Files\7-Zip\7z.exe        ### 7z.exe的默认路径。
JSONSaveDirName=FolderAttr                          ### Json文件（存储被压缩的各子文件夹信息）的备份目录。

【技巧说明】
场景1：
将config.ini的bNotZipifZFExists=Y ，则不会重复压缩子文件提高速度。
程序会自动获取FolderAttr最近的一次备份信息，比较各子目录信息是否发生变化，只有发生变化的子文件夹才进行压缩。

场景2：
config.ini的bNotZipifZFExists=N ，且子目录的7z文件已存在的情况下：
程序会自动获取FolderAttr最近的一次备份信息，比较各子目录信息是否发生变化，只有发生变化的子文件夹才进行压缩。

场景3：
设置skipDirName=不需要压缩的子文件夹列表，可跳过部分子文件（优先级高于bNotZipifZFExists=N）。

【输出结果】
result.txt
各子文件夹的7z档案，如final.7z
包含最新的目标目录下各子文件夹的文件信息的jason文件，如FolderAttr\curFolder.jason
包含目标目录下各子文件夹的文件信息的jason文件历史备份，如FolderAttr\7zSubFolder_2024_01_06.jason

【待优化】
增加密码压缩


 By andysun  2024/01/08