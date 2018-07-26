from ctypes import *
class iDR210:
    fields = ['name', 'gender', 'folk', 'birthday', 'address', 'code', 'agency', 'expire_start', 'expire_end']
    def __init__(self, sdtapi):
        try:
            self.sdtapi = WinDLL(sdtapi)
            if not self.sdtapi.InitComm(1001):
                raise IOError
        except Exception as e:
            raise e

    def ReadBaseMsg(self):
        msg = create_string_buffer(b'\x00'*256)
        if self.sdtapi.ReadBaseMsg(msg, None):
            ret = dict(zip(self.fields, list(filter(None,msg.raw.decode('gbk').strip().split('\x00')))))
            with open('photo.bmp', 'rb') as f:
                ret['photo'] = f.read()
            return ret
        else:
            return {}

if __name__ == '__main__':
    import sys
    import time
    idr = iDR210(sys.argv[1])
    while True:
        while not idr.sdtapi.Authenticate():
            time.sleep(0.1)
        ret = idr.ReadBaseMsg()
        if ret:
            del ret['photo']
            print(ret)
    
