@echo off
rem  =================Coded By weixin.sun 2023-12-18=============
rem set nowTime=%DATE:~4,4%%DATE:~9,2%%DATE:~12,2%%TIME:~0,2%%TIME:~3,2%%TIME:~6,2%
SET PYEAR=%DATE:~0,4%
SET PMONTH=%DATE:~5,2%
SET PDAY=%DATE:~8,2%
SET HOUR=%TIME:~0,2%
SET MIN=%TIME:~3,2%
SET SEC=%TIME:~6,2%
SET nowTime=%PYEAR%%PMONTH%%PDAY%_%HOUR%%MIN%%SEC%
set zipExe="C:\Program Files\7-Zip\7z.exe"
echo  %nowTime%"
SET ziplogFname=ziplog.txt
SET noziplogFname=noziplog.txt
if exist %ziplogFname% del %ziplogFname%
if exist %noziplogFname% del %noziplogFname%
echo "start zip on %nowTime%">%ziplogFname%
echo "no need zip on %nowTime%">%noziplogFname%

for /f "delims=" %%i in ('"dir /ad/b/on *.*"') do (
    if exist %%~nxi.zip ( 
	    echo "%%~nxi">> %noziplogFname% 
	) else ( 
	     echo "%%~nxi done">> %ziplogFname% 
		 %zipExe% a -tzip "%%~nxi.zip" "%%~nxi"
		 rem del /f /s /q %%~nxi/*.*
		 rem rd  %%~nxi 
    )
)

echo "Finish"

pause

