# 精伦iDR210/iDR200联机型身份证阅读器Python接口
这是对精伦iDR210/iDR200的通用二次开发包接口（V4.1）的Python封装，使用ctypes调用精伦提供的动态链接库。  
iDR210的主页位于：`http://www.idr210.cn`。
## 一、安装说明
 - 1. `http://www.idr210.cn/download/jinglunIDR210qudong.html`，下载并安装驱动iDR210驱动；
 - 2. `http://www.idr210.cn/erchikaifa/ercikaifa.html`，获取iDR210的SDK及接口说明；
 - 3. 由于提供的SDK是已编译好的DLL，因此只能通过32位python进行调用；
 - 4. 准备好SDK中的以下DLL：`Sdtapi.dll`，`SavePhoto.dll`，`Dewlt.dll`。
## 二、使用说明
 - 1. 将身份证置于身份证阅读器上；
 - 2. 代码样例：
```
from idr210 import iDR210
idr = iDR210('/path/to/Sdtapi.dll')
# Put your ID card on the card reader
idr.sdtapi.Authenticate()
print(idr.ReadBaseMsg())
```