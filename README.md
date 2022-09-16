# Automatic-login-of-campus-network
校园网自动登录（石家庄铁道大学本部）

需要python，自行安装


修改py文件的名称为你的校园网账号-密码，例如 20001001-123456.py
连接校园网
运行文件即可自动登录

若想实现开机自动运行
可以使用bat脚本
例如：
1:你的文件在c盘CampusNetwork文件夹
创建文本文件输入
cd c:\CampusNetwork
start 20001001-123456.py

2.你的文件在非C盘，如D盘CampusNetwork文件夹
创建文本文件输入
d: 
cd D:\CampusNetwork
start 20001001-123456.py


完成输入保存，修改文件后缀为 xx.bat （xx自己起名）
把bat文件放到这个地址 C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup
即可实现开机自启




