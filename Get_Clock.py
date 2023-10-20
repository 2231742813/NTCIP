from Tool.FcmsTool import FcmsTool

from Tool.SetLog import logger


class Get_Clock(FcmsTool) :
    def __init__(self, ip) :
        super().__init__(ip)
    def get_clock(self) :
        # 发送数据
        get_clock_data = b'\x30\x32\x02\x01\x00\x04\x0d\x61\x64\x6d\x69\x6e\x69\x73\x74\x72\x61\x74\x6f\x72\xa0\x1e\x02\x01\x01\x02\x01\x00\x02\x01\x00\x30\x13\x30\x11\x06\x0d\x2b\x06\x01\x04\x01\x89\x36\x04\x02\x06\x03\x06\x00\x05\x00'
        logger.info("NTCIP协议获取时间")
        logger.info("发送数据: {}".format(get_clock_data.hex()))
        self.a.send(get_clock_data)
        # 接受返回数据
        msg = self.a.recv(1024)
        print(msg.hex())
        # 断开连接
        self.a.close()

if __name__ == "__main__" :
    Get_Clock(ip = '192.168.1.108').get_clock()
