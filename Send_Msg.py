from Tool.FcmsTool import FcmsTool
from Tool.SetLog import logger
import base64
import binascii


class Send_Msg(FcmsTool) :
    def __init__(self, ip) :
        super().__init__(ip)

    def send_msg(self, msg) :
        # print(msg)

        # 假设长度及内容不变 长度53
        # msg_head = b'\x02\x01\x00\x04\x0d\x61\x64\x6d\x69\x6e\x69\x73\x74\x72\x61\x74\x6f\x72\xa3\x26\x02\x01\x0c\x02\x01\x00\x02\x01\x00\x30\x1b\x30\x19\x06\x10\x2b\x06\x01\x04\x01\x89\x36\x04\x02\x03\x05\x08\x01\x03\x03\x01\x04\x05'
        msg_head = b'\x02\x01\x00\x04\x0d\x61\x64\x6d\x69\x6e\x69\x73\x74\x72\x61\x74\x6f\x72\xa3\x26\x02\x01\x0c\x02\x01\x00\x02\x01\x00'
        # 长度20
        len3 = b'\x06\x10\x2b\x06\x01\x04\x01\x89\x36\x04\x02\x03\x05\x08\x01\x03\x03\x01\x04\x05'

        # data1 = b'\x30\x37\x02\x01\x00\x04\x0d\x61\x64\x6d\x69\x6e\x69\x73\x74\x72\x61\x74\x6f\x72\xa3\x23\x02\x02\x00\xf5\x02\x01\x00\x02\x01\x00\x30\x17\x30\x15\x06\x10\x2b\x06\x01\x04\x01\x89\x36\x04\x02\x03\x05\x08\x01\x07\x03\x01\x02\x01\x00'
        data2 = b'\x30\x3f\x02\x01\x00\x04\x0d\x61\x64\x6d\x69\x6e\x69\x73\x74\x72\x61\x74\x6f\x72\xa3\x2b\x02\x02\x00\xd2\x02\x01\x00\x02\x01\x00\x30\x1f\x30\x1d\x06\x0d\x2b\x06\x01\x04\x01\x89\x36\x04\x02\x03\x06\x03\x00\x04\x0c\x00\x0a\xff\x03\x00\x01\x00\x00\x00\x00\x00\x00'
        msg_data = msg.encode('utf-8')
        data_len = len(msg_head) + len(msg_data) + 2 + 2 + 20
        data_len = self.encode_length(data_len)

        len2 = len(msg_data) + len(len3)
        len1 = len2 + 2

        len2 = self.encode_length(len2)
        len1 = self.encode_length(len1)

        # logger.info("NTCIP发送播放表: {}".format(send_msg_data_head.hex()))
        print(data_len)
        print(data_len.hex())
        datas = data_len + msg_head + len1 + len2 + len3 + msg_data
        self.a.send(datas)

        # 接受返回数据
        msg = self.a.recv(1024)
        print(datas.hex())
        print(msg.hex())
        logger.info(datas.hex())
        logger.info(msg.hex())

        # # 假激活播放表
        self.a.send(data2)
        msg = self.a.recv(1024)
        print(data2.hex())
        print(msg.hex())
        logger.info(data2.hex())
        logger.info(msg.hex())

        # self.a.send(data2)
        # msg = self.a.recv(1024)
        # print(data1.decode('utf-8'))


if __name__ == "__main__" :
    # 五位正常
    Send_Msg(ip = '192.168.1.108').send_msg(msg = '888888')
